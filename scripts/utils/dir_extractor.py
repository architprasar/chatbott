import os
import inspect
import importlib.util
from function_extractor import serialize_function_to_json

def extract_functions_from_file(dir_path, file_name):
    file_path = os.path.join(dir_path, file_name)
    
    if not os.path.exists(file_path):
        print(f"File '{file_name}' not found in directory '{dir_path}'.")
        return [], []

    # Import the module dynamically
    spec = importlib.util.spec_from_file_location(file_name.split('.')[0], file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    functions = []
    function_names = []

    # Get all functions using inspect
    for name, obj in inspect.getmembers(module):
        if inspect.isfunction(obj):
            functions.append(obj)
            function_names.append(name)

    return functions, function_names

# Example usage:
dir_path = 'C:/Users/91788/Desktop/genverse/scripts/utils/functions'
file_name = 'amazon_functions.py'
functions, function_names = extract_functions_from_file(dir_path, file_name)

print(serialize_function_to_json(functions[0]))
print("Functions extracted from file:", function_names)
