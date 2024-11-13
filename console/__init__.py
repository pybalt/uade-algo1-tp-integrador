import time, os, shutil, sys

if os.name == "nt":
    import msvcrt
    import ctypes

    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
else:
    import termios
    import tty

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
        time.sleep(0.05)
    print()

def error(*args) -> None:
    """
    Prints the provided arguments to the console in red.
    """
    for arg in args:
        print("\033[91m" + str(arg) + "\033[0m", end="", flush=True)
        time.sleep(0.05)
    print()

def warning(*args) -> None:
    """
    Prints the provided arguments to the console in yellow.
    """
    for arg in args:
        print("\033[91m" + str(arg) + "\033[0m", end="", flush=True)
        time.sleep(0.05)
    print()

def pause_program() -> None:
    """
    Pauses the program until the user presses Enter. Displays a prompt "[Enter] para continuar" 
    at the bottom of the console in a different color without adding a new empty line.
    """
    # Obtener tamaño de la terminal
    size = shutil.get_terminal_size()
    height = size.lines
    width = size.columns

    try:
        # Guardar posición y ocultar cursor
        print("\033[s\033[?25l", end='', flush=True)  # Guardar posición y ocultar cursor

        # Mover cursor a la última línea, columna 1
        print(f"\033[{height};1H", end='', flush=True)

        # Limpiar la línea
        print("\033[2K", end='', flush=True)

        # Imprimir el mensaje en color amarillo brillante
        print("\033[93m[Enter] para continuar\033[0m", end='', flush=True)

        # Esperar a que el usuario presione Enter
        if os.name == 'nt':
            while True:
                key = msvcrt.getch()
                if key == b'\r':  # Tecla Enter
                    break
                elif key == b'\x03':  # Ctrl+C
                    raise KeyboardInterrupt
        else:
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                while True:
                    key = sys.stdin.read(1)
                    if key in ['\r', '\n']:  # Tecla Enter
                        break
                    elif key == '\x03':  # Ctrl+C
                        raise KeyboardInterrupt
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

        # Limpiar la línea del mensaje
        print(f"\033[{height};1H\033[2K", end='', flush=True)

        # Restaurar posición y mostrar cursor
        print("\033[u\033[?25h", end='', flush=True)  # Restaurar posición y mostrar cursor

    except KeyboardInterrupt:
        # Asegurarse de mostrar el cursor incluso si hay una interrupción
        raise SystemExit

def show_options_menu(options: list[str], title: str = "Select an option") -> str:
    """
    Displays an interactive menu that allows the user to select an option using the keyboard arrow keys.
    Allows exiting the menu by pressing Ctrl+C.

    Parameters:
    - options (list[str]): List of available options to select.
    - title (str): Title of the menu.

    Returns:
    - str: The option selected by the user.

    Raises:
    - KeyboardInterrupt: If the user presses Ctrl+C.
    """
    index = 0
    options_count = len(options)

    def draw_menu():
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{title}:\n")
        for i, option in enumerate(options):
            if i == index:
                print(f"\033[32m{option}\033[0m")
            else:
                print(f"  {option}")

    def get_character():
        if os.name == 'nt':
            return msvcrt.getch()
        else:
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                character = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return character

    try:
        # Ocultar el cursor al inicio
        print("\033[?25l", end='', flush=True)
        
        while True:
            draw_menu()
            key = get_character()

            if os.name == 'nt':
                if key == b'\x03':  # Ctrl+C
                    raise KeyboardInterrupt
                if key == b'\xe0':  # Prefijo de flecha
                    key = msvcrt.getch()
                    if key == b'H':  # Flecha arriba
                        index = (index - 1) % options_count
                    elif key == b'P':  # Flecha abajo
                        index = (index + 1) % options_count
                elif key == b'\r':  # Tecla Enter
                    # Mostrar el cursor antes de retornar
                    print("\033[?25h", end='', flush=True)
                    return options[index]
            else:
                if key == '\x03':  # Ctrl+C
                    raise KeyboardInterrupt
                if key == '\x1b':  # Inicio de secuencia de escape
                    key += get_character()
                    key += get_character()
                    if key == '\x1b[A':  # Flecha arriba
                        index = (index - 1) % options_count
                    elif key == '\x1b[B':  # Flecha abajo
                        index = (index + 1) % options_count
                elif key == '\n':  # Tecla Enter
                    # Mostrar el cursor antes de retornar
                    print("\033[?25h", end='', flush=True)
                    return options[index]

    except KeyboardInterrupt:
        # Asegurarse de mostrar el cursor incluso si hay una interrupción
        return "exit()", False
    except Exception as e:
        # Asegurarse de mostrar el cursor en caso de cualquier error
        print("\033[?25h", end='', flush=True)
        raise e