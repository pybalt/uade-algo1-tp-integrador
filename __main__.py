import app
import database

if _name_ == "_main_":
    """
    The code below this if statement defines the interaction with the user.
    """
    database.fill_directory()  # Llenar el directorio al iniciar la aplicación
    print("Bienvenidos a la base de datos no relacional de Base Builders!")
    print("Para continuar, presione una tecla")
    app.start()