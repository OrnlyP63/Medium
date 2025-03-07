import torch
import torch.nn as nn
from torch.utils.data import Dataset

# Define pinball loss function
def pinball_loss(y_pred, y_true, quantile=0.5):
    errors = y_true - y_pred
    loss = torch.max(quantile * errors, (quantile - 1) * errors)
    return loss.mean()

# Define Quantile Regression Model
class QuantileTimeSeriesNN(nn.Module):
    def __init__(self, input_dim):
        super(QuantileTimeSeriesNN, self).__init__()
        self.fc1 = nn.Linear(input_dim, 32)
        self.fc2 = nn.Linear(32, 16)
        self.fc3 = nn.Linear(16, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        return self.fc3(x)


class CryptoDataset(Dataset):
    def __init__(self, X, y):
        self.X = X
        self.y = y
        
    def __len__(self):
        return len(self.y)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

def conformal_score(y_low, y_high, y_true):
    return torch.max(y_low - y_true, y_true - y_high)