import time

def exit() -> None:
    print("Saliendo del programa...")


def log(*args) -> None:
    """
    Prints the provided arguments to the console.
    It contains logic to print the arguments in a readable format, color,
    and animation.
    """
    for arg in args:
        print(arg, end="", flush=True)
        time.sleep(0.5)
    print()

def error(*args) -> None:
    """
    Prints the provided arguments to the console in red.
    """
    for arg in args:
        print("\033[91m", arg, "\033[0m", end="", flush=True)
        time.sleep(0.5)
    print()

def warning(*args) -> None:
    """
    Prints the provided arguments to the console in yellow.
    """
    for arg in args:
        print("\033[93m", arg, "\033[0m", end="", flush=True)
        time.sleep(0.5)
    print()

