import torch
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from torchvision.datasets import ImageFolder


def get_mean_and_std(dataset_path, batchsize, image_size):
    dataset_transforms = transforms.Compose([transforms.Resize((image_size,image_size)),transforms.ToTensor()])
    dataset = ImageFolder(root=dataset_path,transform=dataset_transforms)
    data_loader = DataLoader(dataset=dataset, batch_size=batchsize)
    
    channels_sum, channels_squared_sum, num_batches = 0, 0, 0
    for data, _ in data_loader:
        channels_sum += torch.mean(data, dim=[0,2,3])
        channels_squared_sum += torch.mean(data**2, dim=[0,2,3])
        num_batches += 1
    mean = channels_sum/num_batches
    std = (channels_squared_sum/num_batches - mean**2)**0.5
    
    return mean, std
    