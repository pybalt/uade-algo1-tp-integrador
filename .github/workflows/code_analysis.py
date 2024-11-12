import ast
import re
import sys
import os

def analyze_code(code):
    tree = ast.parse(code)
    results = {
        "lists": False,
        "dictionaries": False,
        "tuples": False,
        "slicing": False,
        "strings": False,
        "sets": False,
        "recursion": False,
        "lambda_functions": False,
        "map": False,
        "filter": False,
        "reduce": False,
        "exceptions": False,
        "file_operations": False,
        "regex": False,
        "unit_tests": False,
    }
    for node in ast.walk(tree):
        if isinstance(node, ast.Dict):
            results["dictionaries"] = True
        elif isinstance(node, ast.Tuple):
            results["tuples"] = True
        elif isinstance(node, ast.Subscript):
            if isinstance(node.slice, ast.Slice):
                results["slicing"] = True
        elif isinstance(node, ast.Str):
            results["strings"] = True
        elif isinstance(node, ast.List):
            results["lists"] = True
        elif isinstance(node, ast.Lambda):
            results["lambda_functions"] = True
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                if node.func.id == 'map':
                    results["map"] = True
                elif node.func.id == 'filter':
                    results["filter"] = True
                elif node.func.id == 'reduce':
                    results["reduce"] = True
                elif node.func.id == "set":
                    results["sets"] = True
                elif node.func.id in ['read', 'write', 'open']:
                    results["file_operations"] = True
        elif isinstance(node, ast.Try):
            results["exceptions"] = True
        elif isinstance(node, ast.Import):
            if "re" in [alias.name for alias in node.names]:
                results["regex"] = True
            if "unittest" in [alias.name for alias in node.names]:
                results["unit_tests"] = True

    def is_recursive(function_def):
        function_name = function_def.name
        for node in ast.walk(function_def):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                if node.func.id == function_name:
                    return True
        return False
    
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            if is_recursive(node):
                results["recursion"] = True
    
    return results

def analyze_directory(directory):
    final_results = {
        "lists": False,
        "dictionaries": False,
        "tuples": False,
        "slicing": False,
        "strings": False,
        "sets": False,
        "recursion": False,
        "lambda_functions": False,
        "map": False,
        "filter": False,
        "reduce": False,
        "exceptions": False,
        "file_operations": False,
        "regex": False,
        "unit_tests": False,
    }

    for root, _, files in os.walk(directory):
        if ".github" in root:
            continue
        for file in files:
            if file.endswith(".py"):
                with open(os.path.join(root, file), "r") as f:
                    code = f.read()
                    file_results = analyze_code(code)
                    for key in final_results:
                        final_results[key] = final_results[key] or file_results[key]

    return final_results

if __name__ == "__main__":
    directory = "."
    check = sys.argv[1]
    results = analyze_directory(directory)

    if results[check]:
        print(f"{check} detected")
        sys.exit(0)
    else:
        print(f"{check} not detected")
        sys.exit(1)
