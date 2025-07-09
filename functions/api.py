import os
import sys

# SCRIPT_DIR gets the absolute directory path of this script file
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))

# sys.path.append() adds the parent directory of SCRIPT_DIR to Python's module search path.
# This allows for importing modules from the parent directory as if they were in this directory.
sys.path.append(os.path.dirname(SCRIPT_DIR))

import requests
from dotenv import dotenv_values

import utilities as utils
from utilities.exit import exit_program

# loading environment (shared & secrets)
config = {
    **dotenv_values("./environment/.env.shared"),
    # **dotenv_values("./environment/.env.secrets")
}


def get_data(github_user: str, endpoint: str = config["ENDPOINT"]) -> str:
    _url = f"{config["URL"]}{github_user}/{endpoint}"

    # Access the API and saving the data to the json data
    response = requests.get(_url)
    try:
        response.raise_for_status()
        data = response.json()
        utils.save(data)
    except requests.exceptions.HTTPError as e:
        print(e.args[0])
        utils.exit_program(1)
