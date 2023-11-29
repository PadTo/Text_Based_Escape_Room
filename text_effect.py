import time


def type_effect(text, delay=0.03):
    """
    Print text with a typewriter effect.

    Args:
    text (str): The text to be printed with the effect.
    delay (float, optional): The delay in seconds between each character. Default is 0.05.
    """
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


type_effect("Hello")
