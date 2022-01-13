import os
from src.utils.common import read_config
from src.utils.data_mgmt import get_data
from src.utils.model import create_model, save_model
#from src.utils.callbacks import get_callbacks
import argparse
import argparse

def training(config_path):
    config=read_config(config_path)
    print(config)
if __name__== '__main__':
    args=argparse.ArgumentParser()
    args.add_argument("--config","-c",default="config.yaml")
    parased_args=args.parse_args()
    training(config_path=parased_args.config)
