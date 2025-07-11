import sys


def exit_program(exit_status: int) -> None:
    match exit_status:
        case 0:
            message = "All data has been printed..."
        case 1:
            message = "Error connecting to Github..."
        case 2:
            message = "Please enter a Username..."
        case 3:
            message = "Unknown GitHib type..."
        case _:
            message = "Unknown error number.."
    print(message)
    print("Exiting the program...")
    sys.exit(exit_status)
