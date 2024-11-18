import time, os, shutil, sys

# Check if the operating system is Windows ("nt" = Windows)
if os.name == "nt":
    # msvcrt: Windows-specific library for low-level console operations
    import msvcrt
    # ctypes: Library for calling Windows API functions
    import ctypes

    # Get access to Windows kernel to configure the console
    kernel32 = ctypes.windll.kernel32
    # Configure console mode:
    # GetStdHandle(-11): Gets the output console handle
    # SetConsoleMode(..., 7): Enables ANSI sequence processing for colors
    # Value 7 enables: ENABLE_PROCESSED_OUTPUT (1) | ENABLE_WRAP_AT_EOL_OUTPUT (2) | ENABLE_VIRTUAL_TERMINAL_PROCESSING (4)
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
else:
    print("This program is only compatible with Windows.")

def exit() -> None:
    print()
    log("Saliendo del programa...")

def ellipsis() -> None:
    """
    Prints an ellipsis animation to the console.
    
    Implementation details:
    - print(): Prints an initial blank line
    - counter: Counter that controls number of dots (1 to 2)
    - while counter < 3: Loop that executes 2 times
    - print("."*counter, end="", flush=True):
        * "."*counter: Multiplies the dot by current counter
        * end="": Prevents automatic line break
        * flush=True: Forces immediate display to console
    - time.sleep(1): Pauses execution for 1 second
    - print("\b", end="", flush=True):
        * \b: Moves cursor back one position
        * Erases previous dot
    - counter += 1: Increments counter
    - print(): Prints final blank line
    """
    print()
    counter = 1
    while counter < 3:
        print("."*counter, end="", flush=True)
        time.sleep(1)
        print("\b", end="", flush=True)
        counter += 1
    print()


def log(*args) -> None:
    """
    Prints the provided arguments to the console.
    It contains logic to print the arguments in a readable format, color,
    and animation.
    """
    for arg in args:
        print(arg, end="", flush=True)
        time.sleep(0.05)
    print()

def error(*args) -> None:
    """
    Prints the provided arguments to the console in red.

    Implementation details:
    - *args: Allows receiving multiple arguments of any type
    - for arg in args: Iterates over each received argument
    - print(): Function to print to console with the following elements:
        * \033[91m: ANSI sequence that sets red color
        * str(arg): Converts the argument to string for printing
        * \033[0m: ANSI sequence that resets color to default
        * end="": Prevents automatic line break
        * flush=True: Forces immediate display to console
    - time.sleep(0.05): Pauses execution for 0.05 seconds to create animation effect
    - final print(): Adds a line break at the end
    """
    for arg in args:
        print("\033[91m" + str(arg) + "\033[0m", end="", flush=True)
        time.sleep(0.05)
    print()

def warning(*args) -> None:
    """
    Prints the provided arguments to the console in yellow.

    Implementation details:
    - *args: Variable length argument list that allows passing multiple arguments
    - for arg in args: Iterates through each argument passed to the function
    - print(): Function to output text with the following parameters:
        * \033[93m: ANSI escape sequence that sets text color to yellow
        * str(arg): Converts argument to string for printing
        * \033[0m: ANSI escape sequence that resets text color to default
        * end="": Prevents automatic newline after print
        * flush=True: Forces immediate output to console without buffering
    - time.sleep(0.05): Adds 50ms delay between characters for animation effect
    - final print(): Adds newline after all arguments are printed
    """
    for arg in args:
        print("\033[93m" + str(arg) + "\033[0m", end="", flush=True)
        time.sleep(0.05)
    print()

def pause_program() -> None:
    """
    Pauses the program until the user presses Enter. Displays a prompt "[Enter] para continuar" 
    at the bottom of the console in a different color without adding a new empty line.

    Implementation details:
    - Uses shutil.get_terminal_size() to get console dimensions (height and width)
    - ANSI escape sequences used:
        * \033[s: Saves current cursor position
        * \033[?25l: Hides cursor
        * \033[{height};1H: Moves cursor to last line, first column
        * \033[2K: Clears current line
        * \033[93m: Sets text color to bright yellow
        * \033[0m: Resets text color
        * \033[u: Restores saved cursor position
        * \033[?25h: Shows cursor
    - msvcrt.getch(): Windows-specific function to read keyboard input
    - Handles:
        * Enter key (b'\r'): Continues program execution
        * Ctrl+C (b'\x03'): Raises KeyboardInterrupt
    - Ensures cursor is always visible even if interrupted
    """
    # Get terminal dimensions
    size = shutil.get_terminal_size()
    height = size.lines
    width = size.columns

    try:
        # Save position and hide cursor
        print("\033[s\033[?25l", end='', flush=True)

        # Move cursor to last line, column 1
        print(f"\033[{height};1H", end='', flush=True)

        # Clear the line
        print("\033[2K", end='', flush=True)

        # Print message in bright yellow
        print("\033[93m[Enter] para continuar\033[0m", end='', flush=True)

        # Wait for Enter key
        if os.name == 'nt':
            while True:
                key = msvcrt.getch()
                if key == b'\r':  # Enter key
                    break
                elif key == b'\x03':  # Ctrl+C
                    raise KeyboardInterrupt

        # Clear message line
        print(f"\033[{height};1H\033[2K", end='', flush=True)

        # Restore position and show cursor
        print("\033[u\033[?25h", end='', flush=True)

    except KeyboardInterrupt:
        # Ensure cursor is visible on interrupt
        raise SystemExit

def show_options_menu(options: list[str], title: str = "Select an option") -> str:
    """
    Displays an interactive menu with keyboard navigation using ANSI escape codes and Windows-specific functionality.

    Technical Details:
    - ANSI Escape Sequences Used:
        * \033[?25l - Hides the cursor during menu navigation
        * \033[?25h - Shows the cursor when menu exits
        * \033[1;36m - Sets text to bright cyan with bold formatting
        * \033[32m - Sets text to green color (for selected option)
        * \033[0m - Resets all text formatting to default

    - Windows-Specific Implementation (os.name == 'nt'):
        * msvcrt.getch() - Gets keyboard input without requiring Enter key
        * Key Code Handling:
            - b'\x03' - Ctrl+C key combination for interrupting
            - b'\xe0' - Special prefix for arrow keys
            - b'H' - Up arrow key for moving selection up
            - b'P' - Down arrow key for moving selection down
            - b'\r' - Enter key for confirming selection

    - Terminal Management:
        * os.system('cls'/'clear') - Clears terminal screen based on OS
        * shutil.get_terminal_size() - Gets current terminal dimensions
        * Title Formatting:
            - Centers title text in terminal width
            - Creates decorative separator lines
        * Menu Display:
            - Shows all options vertically
            - Highlights selected option in green
            - Updates display on arrow key navigation

    Parameters:
    - options (list[str]): List of menu options to display
    - title (str): Menu title to show at top, defaults to "Select an option"

    Returns:
    - str: The text of the selected option
    - ("exit()", False) if Ctrl+C is pressed

    Raises:
    - KeyboardInterrupt: When user presses Ctrl+C
    - Other exceptions are re-raised after ensuring cursor visibility
    """
    index = 0
    options_count = len(options)

    def draw_menu():
        os.system('cls' if os.name == 'nt' else 'clear')
        # Create decorative line with terminal width
        width = shutil.get_terminal_size().columns
        separator = "=" * width
        
        # Print centered title with formatting
        print(separator)
        print(f"\033[1;36m{title.center(width)}\033[0m")  # Bright cyan and bold
        print(separator + "\n")
        
        for i, option in enumerate(options):
            if i == index:
                print(f" \033[32m{option}\033[0m")
            else:
                print(f"{option}")

    def get_character():
        if os.name == 'nt':
            return msvcrt.getch()

    try:
        # Hide cursor at start
        print("\033[?25l", end='', flush=True)
        
        while True:
            draw_menu()
            key = get_character()

            if os.name == 'nt':
                if key == b'\x03':  # Ctrl+C
                    raise KeyboardInterrupt
                if key == b'\xe0':  # Arrow key prefix
                    key = msvcrt.getch()
                    if key == b'H':  # Up arrow
                        index = (index - 1) % options_count
                    elif key == b'P':  # Down arrow
                        index = (index + 1) % options_count
                elif key == b'\r':  # Enter key
                    # Show cursor before returning
                    print("\033[?25h", end='', flush=True)
                    return options[index]

    except KeyboardInterrupt:
        # Ensure cursor is shown even on interrupt
        return "exit()", False
    except Exception as e:
        # Ensure cursor is shown on any error
        print("\033[?25h", end='', flush=True)
        raise e