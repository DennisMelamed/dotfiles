import torch


class TemplateDataset(torch.utils.data.Dataset):

    def __init__(self, ):
        pass

    def __len__(self):
        return 10

    def __getitem__(self, idx):
        input = torch.rand(3, 640, 640)
        target = torch.rand(3, 640, 640)

        return {
            "input": input,
            "target": target,
        }


if __name__ == "__main__":
    ds = TemplateDataset()
    test_sample = ds[0]
    for k, v in test_sample.items():
        print(k, v.shape)
