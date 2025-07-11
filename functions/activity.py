import json


def process_data(data: str) -> dict:
    """
    Processes activity data and returns a dictionary of event types per repository.

    Parameters:
        data (str): A string containing JSON data with events, where each event includes
                    repository information and an event type.

    Returns:
        dict: A nested dictionary where the keys are repository names, and values
              are another dictionary of event types with their occurrence counts.

    Example:
        >>> data = '[
        ...     {"repo": {"name": "repo1"}, "type": "issue"},
        ...     {"repo": {"name": "repo2"}, "type": "push"},
        ...     {"repo": {"name": "repo1"}, "type": "pull_request"}
        ... ]'
        >>> process_data(data)
        {
            'repo1': {'issue': 1, 'pull_request': 1},
            'repo2': {'push': 1}
        }
    """
    # create empty dictionary for the events
    events: dict = {}

    # parse the json file
    for event in data:

        # git repo & type
        event_repo = event["repo"]["name"]
        event_type = event["type"]

        # append to dictionary or create entry if not found
        if events.get(event_repo) == None:
            events.update({event_repo: {}})
            events[event_repo].update({event_type: 1})
        elif events.get(event_repo) != None:
            events[event_repo][event_type] = events[event_repo].get(event_type, 0) + 1

    # return the dictionary with the data
    return events
