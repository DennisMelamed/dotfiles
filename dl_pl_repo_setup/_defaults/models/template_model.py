import torch
import torch.nn as nn
import torch.nn.functional as F
import pytorch_lightning as pl


class TemplateNet(pl.LightningModule):

    def __init__(
        self,
        experiment_directory: str = "./experiments/default_experiment/",
    ):
        super().__init__()

        self.net = nn.Identity()
        self.loss = nn.MSELoss()
        self.experiment_directory = experiment_directory

    def forward(self, x):
        output = self.net(x['input'])
        return {"output": output}

    def configure_optimizers(self):
        optimizer = None

        return {
            "optimizer": optimizer,
        }

    def common_step(self, batch, batch_idx, mode='train'):
        y_hat = self(batch)
        loss = self.loss(y_hat['output'], batch['target'])
        losses = {}
        losses[f"{mode}/loss"] = loss
        self.log_dict(losses, sync_dist=True)

        return loss

    def training_step(self, batch, batch_idx):
        return self.common_step(batch, batch_idx, 'train')

    def validation_step(self, batch, batch_idx):
        return self.common_step(batch, batch_idx, 'val')

    def test_step(self, batch, batch_idx):
        return self.common_step(batch, batch_idx, 'test')

    def predict_step(self, batch, batch_idx, dataloader_idx=None):
        y_hat = self(batch)
        results = y_hat['output']
        return results


if __name__ == "__main__":
    model = TemplateNet()
    batch_size = 8
    image_size = (3, 640, 460)
    test_in = {
        "input": torch.rand(batch_size, *image_size),
        "target": torch.rand(batch_size, *image_size),
    }
    print(f"input shape: {test_in['input'].shape}")
    test_out = model(test_in)
    print(f"output shape: {test_out['output'].shape}")
    loss = model.training_step(test_in, 0)
    print(f"loss: {loss}")
