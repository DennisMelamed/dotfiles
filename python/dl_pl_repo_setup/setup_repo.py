import a
import ubelt as ub
import fire
import shutil
import venv


def setup(target_dir: str):
    target_dir = ub.Path(target_dir)
    print("copying files...")
    shutil.copytree("_defaults", target_dir, dirs_exist_ok=True)
    print("creating virtual env...")
    venv.create(
        target_dir / f"{target_dir.name}_venv",
        with_pip=True,
    )

    print("installing base pip dependencies to venv...")
    cmd_str = f'. ./{target_dir.name}_venv/bin/activate && ./{target_dir.name}_venv/bin/pip install -r requirements.txt'
    ub.cmd(cmd_str, verbose=1, shell=True, cwd=target_dir)
    print("done")


if __name__ == '__main__':
    fire.Fire(setup)
