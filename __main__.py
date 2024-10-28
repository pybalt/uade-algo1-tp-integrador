import app
import database

if __name__ == "__main__":
    directory = database.initialize_directory()  
    print("Bienvenidos a la base de datos no relacional de Base Builders!")
    print("Para continuar, presione una tecla")
    app.start(directory)  