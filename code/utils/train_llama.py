import os
import time
import logging
import hydra
from omegaconf import DictConfig, OmegaConf
import pandas as pd
import torch


@hydra.main(config_path="../configs", config_name="conf_llama_v0")
def main(cfg):
    set_seed(cfg.seed)
    return


if __name__ == "__main__":
    main()
