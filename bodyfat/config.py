# willcontain parts that we need to the project files for the dataset
# and features we build for the project.
# This file will be imported in the main script to use the variables.

# Path to the dataset file
# DATASET_PATH = "data/bodyfat.csv"

import os
import random
from pathlib import Path
import numpy as np
from box import ConfigBox
from ruamel.yaml import YAML

"""
ConfigBox is a class within the box module that enhances the handling of string 
manipulation typically encountered in configuration files.

The ruamel.yaml library is a YAML parser and emitter for Python.
It supports roundtrip preservation of comments, sequence/map flow style, and map key order.
Specifically, it allows you to load and dump YAML files while preserving comments and other formatting details.
"""

# Load the configuration file 
class Config:
    class Path:
        APP_HOME = Path(os.getenv("APP_HOME", Path(__file__).parent.parent)) # os.getenv() method returns the value of the environment variable key if it exists in the location/file "APP_HOME". 
                                                                            # If the key is not found, it returns the default value specified in the second argument.
        """
        In summary, this code snippet allows you to access the parent directory of the Python script or module, 
        which can be useful for various purposes, such as locating configuration files, importing modules from a specific directory, 
        or organizing project files
        """ 
        ARTEFACTS_DIR = APP_HOME / "artefacts"
        DATA_DIR = ARTEFACTS_DIR / "data"
        FEATURES_DIR = ARTEFACTS_DIR / "features"
        MODELS_DIR = APP_HOME / "models"
        EXPERIMENTS_DIR = APP_HOME / "experiments"
     
        
def load_config(file_path: Path = Config.Path.APP_HOME/"params.yaml") -> ConfigBox:
    yaml = YAML(typ="safe")
    return ConfigBox(yaml.load(file_path.open(encoding="utf-8")))


"""
The purpose of this function seems to be related to setting a random seed for reproducibility.
By specifying a seed value, you can ensure that random processes (such as random number generation) produce the same 
results across different runs of your code
"""
def seed_everything(seed: int = load_config().random.seed):  #tales/picks a seed from the params.yaml file
    random.seed(seed)
    np.random.seed(seed)
 
