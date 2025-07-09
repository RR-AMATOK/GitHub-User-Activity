import sys


def exit_program(exit_status: int) -> None:
    match exit_status:
        case 0:
            message = "Data for Github User updated..."
        case 1:
            message = "Error connecting to Github..."
        case _:
            message = "Unknown error number.."
    print(message)
    print("Exiting the program...")
    sys.exit(exit_status)
