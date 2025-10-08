# arrange_conf.py

from config import MODEL_gpt_3, MODEL_gpt_4, MODEL_llama, MODEL_local,MODEL_gpt_5_mini, folder_path_reg, folder_path_reg_md, dataset_path_reg, folder_path_ad_md, folder_path_ad, dataset_path_ad
import os
import json
import logging
from pathlib import Path

def get_log_directory(directory: str, model) -> str:
    # Normalize incoming directory (tolerate missing/trailing slash)
    dkey = str(directory).rstrip('/')

    dir_map = {
        'vrdu2/registration-form/few_shot-splits': 'reg',
        'vrdu2/ad-buy-form/few_shot-splits': 'ad',
    }

    model_map = {
        MODEL_gpt_3: 'gpt3.5_outputs',
        MODEL_gpt_4: 'gpt4_outputs',
        MODEL_llama: 'llama3_70b_outputs',
        MODEL_local: 'local_outputs',
        MODEL_gpt_5_mini: 'gpt5_mini_outputs'
    }

    if dkey not in dir_map:
        raise ValueError(f"Directory not recognized for logging configuration: {directory!r}")
    if model not in model_map:
        raise ValueError(f"Model not recognized for logging configuration: {model!r}")

    out_path = Path(model_map[model]) / dir_map[dkey]
    out_path.mkdir(parents=True, exist_ok=True)

    return out_path.as_posix() + '/'


def get_output_directory(directory, model) -> str:
    dkey = directory.rstrip('/')

    # Map dataset directory -> short subfolder
    dir_map = {
        'vrdu2/registration-form/few_shot-splits': 'reg',
        'vrdu2/ad-buy-form/few_shot-splits': 'ad',
    }

    # Map model constant -> model output root
    model_map = {
        MODEL_gpt_3: 'gpt3.5_outputs',
        MODEL_gpt_4: 'gpt4_outputs',
        MODEL_llama: 'llama3_70b_outputs',
        MODEL_local: 'local_outputs',
        MODEL_gpt_5_mini: 'gpt5_mini_outputs'
    }

    if dkey not in dir_map:
        raise ValueError(f"Directory not recognized for logging configuration: {directory!r}")
    if model not in model_map:
        raise ValueError(f"Model not recognized for logging configuration: {model!r}")

    # Build the full path
    out_path = Path(model_map[model]) / dir_map[dkey]

    # Ensure it exists
    out_path.mkdir(parents=True, exist_ok=True)

    # Return with trailing slash to match prior behavior
    return out_path.as_posix() + '/'


def get_data_paths(directory):
    folder_path = ""
    dataset_path = ""
    dtype = ""
    
    if directory == 'vrdu2/registration-form/few_shot-splits/':
        folder_path = folder_path_reg
        dataset_path = dataset_path_reg
        dtype = 'reg'
        return folder_path, dataset_path, dtype
    elif directory == 'vrdu2/ad-buy-form/few_shot-splits/':
        folder_path = folder_path_ad
        dataset_path = dataset_path_ad
        dtype = 'ad'
        return folder_path, dataset_path, dtype
    else:
        print("Directory not recognized")
        return "", "", ""
    



