This script set up a slurm sbatch script in a given experiment folder and run training/testing/predicting.
Outputs are also saved to the experiment folder. Synatx for use is:
```
python run_experiment.py {fit,test,predict} experiment_name
```

where `experiment_name` should correspond to the config filename (the `.yaml` stored in `configs`)
The number of gpus to request from slurm is extracted from the config file for training.

Defaults are in `slurm_defaults.yaml` for the number of cpus and memory to request, and the email you'd like to recieve slurm notifications at. These can either be changed in the yaml file, or set with the `--cpus_p_task`, `--mem`, and `--email` flags

It is assumed there is a single `{something}_venv` python virtual environment folder in the root directory of the repo root location.
