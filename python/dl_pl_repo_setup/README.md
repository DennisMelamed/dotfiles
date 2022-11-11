- To set up a new repo: `python setup.py /path/to/repo`
- To resolve protobuf issue on macos, downgrade protobuf version: `pip install protobuf==3.19.4`


All training here is based around pytorch lightning configs like the one in _defaults/configs/default_config.yaml

So to train that experiment, you'd call python cli.py fit --config ./configs/default_config.yaml. To test/predict, replace `fit` with the relevant verb.  Key features of the config file are experiment directory (where all generated files like checkpoints, predictions, tensorboard logs, etc) go, class path to the model you're training,  and class path to the datamodule you're using. If you haven't used lightning before, a datamodule is just a way of organizing training/val/test/predict dataloaders, and the model file also encompasses the training/val/test/predict code for the model it defines.

Config files should be able to use variable interpolation. For example, the checkpoint directory for Lightning is set to a subdir of the directory you define as your experiment_directory.
