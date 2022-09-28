import pytorch_lightning as pl
import torch
from torch.utils.data import random_split, DataLoader
from data.template_dataset import TemplateDataset


class TemplateDataModule(pl.LightningDataModule):

    def __init__(
        self,
        train_batch_size: int = 1,
        test_batch_size: int = 1,
        train_num_workers: int = 1,
        test_num_workers: int = 1,
        train_val_split=0.8,
    ):
        super().__init__()

        self.train_batch_size = train_batch_size
        self.test_batch_size = test_batch_size
        self.train_num_workers = train_num_workers
        self.test_num_workers = test_num_workers
        self.train_val_split = train_val_split

    def prepare_data(self):
        pass

    def setup(self, stage=None):

        if stage == "fit" or stage is None:
            full_dataset = TemplateDataset()

            train_split_size = int(self.train_val_split * len(full_dataset))
            self.train, self.val = random_split(
                full_dataset,
                [train_split_size,
                 len(full_dataset) - train_split_size])
            print("train size ", len(self.train))
            print("val size ", len(self.val))

        if stage == "test" or stage is None:
            self.test = TemplateDataset()

        if stage == 'predict' or stage is None:
            self.predict = TemplateDataset()

    def train_dataloader(self):
        return DataLoader(
            self.train,
            batch_size=self.train_batch_size,
            num_workers=self.train_num_workers,
        )

    def val_dataloader(self):
        return DataLoader(
            self.val,
            batch_size=self.train_batch_size,
            num_workers=self.train_num_workers,
        )

    def test_dataloader(self):
        return DataLoader(self.test,
                          batch_size=self.test_batch_size,
                          num_workers=self.test_num_workers)

    def predict_dataloader(self):
        return DataLoader(self.predict,
                          batch_size=self.test_batch_size,
                          num_workers=self.test_num_workers)


if __name__ == "__main__":
    pl.utilities.seed.seed_everything(seed=0, workers=True)
    dm = TemplateDataModule()

    dm.setup()
    train_dl = dm.train_dataloader()

    for tidx, test_sample in enumerate(train_dl):
        print(tidx)
        for k, v in test_sample.items():
            print(k, v.shape)
