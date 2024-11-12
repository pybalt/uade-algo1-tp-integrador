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
        time.sleep(0.1)
    print()

def error(*args) -> None:
    """
    Prints the provided arguments to the console in red.
    """
    for arg in args:
        print("\033[91m" + str(arg) + "\033[0m", end="", flush=True)
        time.sleep(0.1)
    print()

def warning(*args) -> None:
    """
    Prints the provided arguments to the console in yellow.
    """
    for arg in args:
        print("\033[91m" + str(arg) + "\033[0m", end="", flush=True)
        time.sleep(0.1)
    print()

