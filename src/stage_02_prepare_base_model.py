

from src.utils.all_utils import read_yaml,create_directory
from src.utils.model import get_VGG_16_model
import argparse
import pandas as pd
import os
from tqdm import tqdm
import shutil
import logging


logging_str = "[%(asctime)s:%(levelname)s:%(module)s]:%(message)s"
log_dir ="logs"
os.makedirs(log_dir,exist_ok=True)
logging.basicConfig(filename=os.path.join(log_dir,"runnig_logs.log"),level=logging.INFO,format=logging_str,filemode="a")

def prepare_base_model(config_path,params_path):
    config = read_yaml(config_path)
    param = read_yaml(params_path)

    artifacts = config["artifacts"]
    artifacts_dir = artifacts["ARTIFACTS_DIR"]


    base_model_dir = artifacts["BASE_MODEL_DIR"]
    base_model_name = artifacts["BASE_MODEL_NAME"]

    base_model_dir_path = os.path.join(artifacts_dir,base_model_dir)

    create_directory([base_model_dir_path])

    base_model_path = os.path.join(base_model_dir_path,base_model_name)





if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config","-c",default="config/config.yaml")
    args.add_argument("--params","-p",default="params.yaml")
    parsed_args = args.parse_args()
    try:
        logging.info(">>>>>>>>>> stage 01 started")
        # get_data(config_path=parsed_args.config)
        logging.info("stage 01 is completed ! all the data is saved in local directory >>>>>>>>>")
    except Exception as e:
        logging.exception(e)
        raise e


