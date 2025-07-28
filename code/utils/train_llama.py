import os
import time
import logging
import hydra
from omegaconf import DictConfig, OmegaConf
import pandas as pd
from sklearn.model_selection import train_test_split
import torch
import transformers
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, TrainingArguments, Trainer, get_linear_schedule_with_warmup, set_seed
from qwen_classifier import *
from utils import *


os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["WANDB_DISABLED"] = "true"
logger = set_logger()


@hydra.main(version_base=None, config_path="../configs", config_name="conf_llama_v0")
def main(cfg):
    set_seed(cfg.seed)
    tokenizer = AutoTokenizer.from_pretrained(
        cfg.model.model_name,
        use_fast=False,
    )
    tokenizer.add_eos_token = True
    tokenizer.padding_side = "right"
    
    df = prepare_data(cfg)
    if cfg.debug:
        df = df.sample(100)
        cfg.training.per_device_train_batch_size = 1
        
    
    return


if __name__ == "__main__":
    main()
