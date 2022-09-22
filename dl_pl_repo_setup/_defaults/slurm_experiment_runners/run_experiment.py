import ubelt as ub
import fire
import yaml


class SlurmOperator:

    def __init__(self, dry_run=False, cpus_p_task=None, mem=None, email=None):

        slurm_config_path = ub.Path(
            ub.util_path.expandpath(__file__)).parent / "slurm_defaults.yaml"
        with open(slurm_config_path, 'r') as slurm_config_file:
            slurm_config = yaml.load(slurm_config_file, yaml.SafeLoader)
            self.cpus_p_task = slurm_config['cpus_per_task']
            self.mem = slurm_config['mem']
            self.email = slurm_config['email']
        if cpus_p_task is not None:
            self.cpus_p_task = cpus_p_task
        if mem is not None:
            self.mem = mem
        if email is not None:
            self.email = email

        self.dry_run = dry_run

    def fit(self, experiment_name: str):
        self._common_experiment(experiment_name, 'fit')

    def test(self, experiment_name: str):
        self._common_experiment(experiment_name, 'test')

    def predict(self, experiment_name: str):
        self._common_experiment(experiment_name, 'predict')

    def _common_experiment(self, experiment_name: str, mode: str = 'fit'):
        experiment_name = experiment_name.replace("/", "-")
        print("\n[EXPERIMENT]")
        print("Dry Run: ", self.dry_run)
        print("Name: ", experiment_name)

        repo_root = ub.Path(ub.util_path.expandpath(__file__)).parent.parent
        print("Repo root: ", repo_root)

        config_location = f"{repo_root}/configs/{experiment_name}.yaml"
        run_string = f"python cli.py {mode} --config {config_location}"

        with open(config_location, 'r', encoding='utf-8') as config_file:
            config_yaml = yaml.load(config_file, yaml.SafeLoader)
            experiment_location = repo_root / ub.Path(
                config_yaml['model']['init_args']['experiment_directory'])
            ub.ensuredir(experiment_location)
            print(f"Experiment directory: {experiment_location}")
            bash_script_location = experiment_location / f"run_{experiment_name}_{mode}ing.sh"
            print(f"Sbatch script: {bash_script_location}")

            if config_yaml['trainer']['accelerator'] == 'gpu':
                n_gpus = config_yaml['trainer']['devices']
            else:
                print(
                    f"You did not specify gpu as an accelerator in config.\nThis script may not be necessary, try using `{run_string}` directly"
                )
                quit()
            print("\n[SLURM]")
            print(f"GPUS: {n_gpus}")
        print(f"Memory: {self.mem}")
        print(f"CPUs: {self.cpus_p_task}")
        print(f"Email: {self.email}")

        with open(bash_script_location, 'w') as sbatch_file:
            sbatch_file.write(f"""
#!/bin/bash

#SBATCH --job-name="{mode}_{experiment_name}"
#SBATCH --partition=community
#SBATCH --cpus-per-task={self.cpus_p_task}
#SBATCH --gres=gpu:{n_gpus}
#SBATCH --mem {self.mem}
#SBATCH --requeue
#SBATCH --output {experiment_location}/{mode}.stdout
#SBATCH --mail-user={self.email}
#SBATCH --mail-type=END,FAIL,REQUEUE

cd "{repo_root}"
source ./*_venv/bin/activate
echo "starting"
srun {run_string}""")

        if not self.dry_run:
            try:
                ub.cmd(f"sbatch {bash_script_location}")
            except:
                print(
                    f"slurm/sbatch may not be available on your system.\nTry running with: {run_string}"
                )


if __name__ == "__main__":
    fire.Fire(SlurmOperator)
