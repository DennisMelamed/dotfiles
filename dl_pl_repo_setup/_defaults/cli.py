from pytorch_lightning.utilities.cli import LightningCLI
from pytorch_lightning import LightningDataModule, LightningModule

common_params = {'parser_mode': 'omegaconf'}

cli = LightningCLI(LightningModule,
                   LightningDataModule,
                   subclass_mode_model=True,
                   subclass_mode_data=True,
                   save_config_overwrite=True,
                   parser_kwargs={
                       'fit': common_params,
                       'validate': common_params,
                       'predict': common_params,
                       'test': common_params,
                   })
