def parse_value(value: str):
    """
    Parse the input value based on its format and return the appropriate Python type with a type tag.
    Args:
        value (str): The input string to parse in the format type.value1,value2,etc.
    Returns:
        dict: A dictionary with the parsed value and its associated type.
    """
    parsed_correctly = False
    parsed_data = None

    while not parsed_correctly:
        if "." not in value:
            print(
                "Formato inválido. El valor debe estar en el formato 'tipo.valor1,valor2,...'"
            )
            value = input("Reingrese el valor en el formato correcto: ")
            continue

        type_hint, raw_value = value.split(".", 1)

        if type_hint == "string":
            parsed_data = {"_type": "string", "value": raw_value}
            parsed_correctly = True
        elif type_hint == "int":
            parsed_data = {"_type": "int", "value": int(raw_value)}
            parsed_correctly = True
        elif type_hint == "float":
            parsed_data = {"_type": "float", "value": float(raw_value)}
            parsed_correctly = True
        elif type_hint == "tuple":
            values: list = raw_value.split(",")
            cleaned_values = list(map(lambda v: v.strip(), values))
            parsed_data = {"_type": "tuple", "value": tuple(cleaned_values)}
            parsed_correctly = True
        elif type_hint == "list":
            values = raw_value.split(",")
            cleaned_values = list(map(lambda v: v.strip(), values))
            parsed_data = {"_type": "list", "value": cleaned_values}
            parsed_correctly = True
        elif type_hint == "set":
            values = raw_value.split(",")
            cleaned_values = set(map(lambda v: v.strip().lower(), values))
            parsed_data = {"_type": "set", "value": cleaned_values}
            parsed_correctly = True
        elif type_hint == "matrix":
            rows = raw_value.split(";")
            matrix = list(map(lambda row: row.split(","), rows))
            parsed_data = {"_type": "matrix", "value": matrix}
            parsed_correctly = True
        else:
            print(f"Tipo '{type_hint}' no soportado.")
            value = input("Reingrese el valor en el formato correcto: ")

    return parsed_data
