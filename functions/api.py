import requests
from dotenv import dotenv_values

import utilities as utils
from utilities.exit import exit_program

# loading environment (shared & secrets)
config = {**dotenv_values("./environment/.env.shared")}


def get_data(github_user: str, endpoint: str = config["ENDPOINT"]) -> dict:
    """
    Fetches data from a specified GitHub API endpoint for a given user.

    Args:
        github_user (str): The username of the GitHub user.
        endpoint (str, optional): The API endpoint to fetch data from. Defaults to the value of
                                  'ENDPOINT' in the environment configuration.

    Returns:
        dict: The JSON response data from the API request.

    Raises:
        SystemExit: If an HTTP error occurs during the API request, exits the program with status code 1.
    """
    _url = f"{config["URL"]}{github_user}/{endpoint}"

    # Access the API and saving the data to the json data
    response = requests.get(_url)
    try:
        response.raise_for_status()
        return response.json()
        # utils.save(data) # no need to save data anymore
    except requests.exceptions.HTTPError as e:
        print(e.args[0])
        utils.exit_program(1)
