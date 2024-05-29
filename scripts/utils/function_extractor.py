import inspect
import json
from typing import get_type_hints
import xml.etree.ElementTree as ET
import re
def get_type_name(t):
    name = str(t)
    if "list" in name or "dict" in name:
        return name
    else:
        return t.__name__

def serialize_function_to_json(func):
    signature = inspect.signature(func)
    type_hints = get_type_hints(func)

    function_info = {
        "name": func.__name__,
        "description": func.__doc__,
        "parameters": {
            "type": "object",
            "properties": {}
        },
        "returns": type_hints.get('return', 'void').__name__
    }

    for name, _ in signature.parameters.items():
        param_type = get_type_name(type_hints.get(name, type(None)))
        function_info["parameters"]["properties"][name] = {"type": param_type}
    return json.dumps(function_info, indent=2)
# def get_all_functions_from_module(module):
#     members = inspect.getmembers(module)
#     functions = [member[1] for member in members if inspect.isfunction(member[1])]
#     return functions

def extract_function_calls(completion):
    completion = completion.strip()
    pattern = r"(<multiplefunctions>(.*?)</multiplefunctions>)"
    match = re.search(pattern, completion, re.DOTALL)
    if not match:
        return None
    
    multiplefn = match.group(1)
    root = ET.fromstring(multiplefn)
    functions = root.findall("functioncall")
    return [json.loads(fn.text) for fn in functions]
