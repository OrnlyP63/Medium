import pandas as pd
import numpy as np
import torch

def set_time_data(currency_metrics: pd.DataFrame):
  metrics = currency_metrics.copy()
  metrics['time'] = pd.to_datetime(metrics['time'])
  metrics = metrics.set_index('time')

  return metrics

def set_asset_return(currency_metrics: pd.DataFrame):
  metrics = currency_metrics.copy()
  if 'returns' in metrics.columns:
    return metrics
  else:
    log_prices = np.log(metrics['PriceUSD'])
    metrics['returns'] = log_prices.diff()
    return metrics.dropna()
  
def set_asset_log_mvrv(currency_metrics: pd.DataFrame):
  metrics = currency_metrics.copy()
  if 'log_mvrv' in metrics.columns:
    return metrics
  else:
    log_prices = np.log(metrics['CapMVRVCur'])
    metrics['log_mvrv'] = log_prices.diff()
    return metrics.dropna()
  
def set_asset_log_nvt(currency_metrics: pd.DataFrame):
  metrics = currency_metrics.copy()
  if 'log_nvt' in metrics.columns:
    return metrics
  else:
    log_prices = np.log(metrics['NVTAdj'])
    metrics['log_nvt'] = log_prices.diff()
    return metrics.dropna()

def create_data(df: pd.DataFrame, train_size = 0.8):
    X_data = df.loc[:, ['log_mvrv', 'log_nvt']]
    y_data = df.loc[:, ['returns']]

    # Split into train and test sets (80% train, 20% test)
    split_idx = int(len(X_data) * train_size)
    X_train, X_test = X_data[:split_idx], X_data[split_idx:]
    y_train, y_test = y_data[:split_idx], y_data[split_idx:]

    # Convert to PyTorch tensors
    X_train = torch.tensor(X_train.values, dtype=torch.float32)
    y_train = torch.tensor(y_train.values, dtype=torch.float32).view(-1, 1)
    X_test = torch.tensor(X_test.values, dtype=torch.float32)
    y_test = torch.tensor(y_test.values, dtype=torch.float32).view(-1, 1)

    return X_train, X_test, y_train, y_test
