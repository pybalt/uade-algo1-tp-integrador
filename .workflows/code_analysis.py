import ast
import re
import sys

def analyze_code(code, check):
    tree = ast.parse(code)
    results = {
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
    }
    
    # AST Analysis
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
        elif isinstance(node, ast.Set):
            results["sets"] = True
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
            elif isinstance(node.func, ast.Attribute):
                if node.func.attr in ['read', 'write', 'open']:
                    results["file_operations"] = True
        elif isinstance(node, ast.Try):
            results["exceptions"] = True

    # Regex Analysis
    if re.search(r'\bimport\s+re\b', code):
        results["regex"] = True
    
    # Recursion check
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
    
    return results[check]

# Run the analysis on the specified file
if __name__ == "__main__":
    with open("your_code.py", "r") as file:
        code = file.read()

    check = sys.argv[1]  # Element to check passed as an argument
    if analyze_code(code, check):
        print(f"{check} detected")
        sys.exit(0)  # Success
    else:
        print(f"{check} not detected")
        sys.exit(1)  # Failure
