import json

from dotenv import dotenv_values

from .exit import exit_program

# loading environment (shared & secrets)
config = {
    **dotenv_values("./environment/.env.shared"),
}


def save(data: dict) -> None:
    # Writing back to json
    with open(config["PATH_DATA"], "w") as f:
        json.dump(data, f)
        exit_program(0)
