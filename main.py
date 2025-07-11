import json
import sys

from dotenv import dotenv_values

import functions as func
import utilities as utils

# loading environment (shared & secrets)
config = {**dotenv_values("./environment/.env.shared")}


def main() -> None:
    try:
        github_user = sys.argv[1]
    except IndexError:
        print("No user passed.")
        utils.exit_program(2)

    # run the api call
    data_json = func.get_data(github_user=github_user)

    # Process the dictionary
    github_events = func.process_data(data_json)
    # print(github_events)

    # Printing activity to the terminal
    for repos in github_events:
        utils.format_print("Repository: ", repos)
        for events in github_events[repos]:
            num_events = github_events[repos].get(events)
            # print(repos, events, github_events[repos].get(events))
            match events:
                case "CommitCommentEvent":
                    utils.format_print(" - ", f"Submitted {num_events} commit comments")
                case "CreateEvent":
                    utils.format_print(" - ", f"Created {num_events} Git branches")
                case "DeleteEvent":
                    utils.format_print(" - ", f"Deleted {num_events} Git branches")
                case "ForkEvent":
                    utils.format_print(" - ", f"Forked {num_events} repositories")
                case "GollumEvent":
                    utils.format_print(
                        " - ", f"Created/Updated {num_events} wiki pages"
                    )
                case "IssueCommentEvent":
                    utils.format_print(
                        " - ",
                        f"Had {num_events} of activities related to an issue or pull request comment",
                    )
                case "IssuesEvent":
                    utils.format_print(
                        " - ", f"Had {num_events} of activities related to an issue"
                    )
                case "MemberEvent":
                    utils.format_print(
                        " - ",
                        f"Had {num_events} of activities related to a repository collaboration",
                    )
                case "PublicEvent":
                    utils.format_print(
                        " - ",
                        f"Changed {num_events} repositories from private to public",
                    )
                case "PullRequestEvent":
                    utils.format_print(" - ", f"Created {num_events} of pull requests")
                case "PullRequestReviewEvent":
                    utils.format_print(" - ", f"Reviewed {num_events} of pull requests")
                case "PullRequestReviewCommentEvent":
                    utils.format_print(
                        " - ", f"Created {num_events} of pull requests comments"
                    )
                case "PullRequestReviewThreadEvent":
                    utils.format_print(
                        " - ", f"PArticipated in {num_events} of pull requests threads"
                    )
                case "PushEvent":
                    utils.format_print(
                        " - ", f"Pushed {num_events} changes to a repo branch"
                    )
                case "ReleaseEvent":
                    utils.format_print(" - ", f"Created {num_events} of releases")
                case "SponsorshipEvent":
                    utils.format_print(" - ", f"Sponsored {num_events} listings")
                case "WatchEvent":
                    utils.format_print(" - ", f"Stared {num_events} of repositories")
                case _:
                    utils.exit_program(3)
        print()
    utils.exit_program(0)


if __name__ == "__main__":
    main()
