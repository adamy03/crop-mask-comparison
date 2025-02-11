"""
Script to evaluate an individual model
"""
import os
import sys

# Change the working directory to the directory of this script
os.chdir(os.path.dirname(os.path.realpath(__file__)))
sys.path.append("..")

from src.utils import models_dir  # noqa: E402
from src.pipeline_funcs import run_evaluation  # noqa: E402

if __name__ == "__main__":
    model_name = "Ethiopia_Tigray_2021"
    model_ckpt_path = models_dir / f"{model_name}.ckpt"
    _, metrics = run_evaluation(model_ckpt_path)
    print(metrics)
