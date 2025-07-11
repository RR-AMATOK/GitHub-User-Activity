def pascal_to_words(word: str) -> str:
    """Args:
        word (str): A PascalCase string to be converted. For example, 'CamelCaseString'.

    Returns:
        str: A space-separated string where each word starts with a capital letter.
             For example, 'Camel Case String'.

    Example:
        >>> pascal_to_words('CamelCaseString')
        'Camel Case String'
    """
    word = "".join(
        map(
            lambda x: x if (x.islower() or word.index(x) == 0) else " " + x,
            word,
        )
    )
    return word


def format_print(prefix: str, text: str, length: int = 80) -> None:
    """
    Prints a formatted string with padding.

    Args:
        prefix (str): The prefix to add before the text.
        text (str): The main text content to display.
        length (int, optional): The total desired length of the output line. Defaults to 80.

    Returns:
        None
    """
    output_string = f"{prefix}{text}"
    padding_length = length - len(output_string)
    padding_dots = "." * padding_length
    print(f"{output_string}{padding_dots}")
