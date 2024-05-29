import openai
import json
import xml.etree.ElementTree as ET
import re

import inspect
import json
from typing import get_type_hints
from amznscraper.searchresults import get_data
CONTEXT =[]
openai.api_key = "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"

def get_product_from_amazon(product_name:str)->None:
    """use this function to search product that can be a recommendation on amazon.
    this function call is very helpful as it can be used to give the user a direct link to amazon product
    """
    pass



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
def generate_hermes(query,function=True):
    fn = """{"name": "function_name", "arguments": {"arg_1": "value_1", "arg_2": value_2, ...}}"""
  

    prompt2 = f"""
    You are a helpful fashion assistant
    you are to recommend products that aligns to the user query 
    alwas give the response in under 100 words maximum points with little explanation
    user query
    {query}
    below is the chat between you and the user for context
        {CONTEXT}
    """
    response = openai.chat.completions.create(
        model="gpt-4o",  # Choose the appropriate OpenAI model
        messages=[
            {"role": "system", "content": prompt2}
        ],
        max_tokens=150
    
    )
    
    
    prompt1 = f"""system

now you are to create a function call that can be used to search products that can be a recommendation on amazon based on your previous recommendations
previous recommendations: {response.choices[0].message.content}
note: if the previous message is just a message not an outfit recommendation return nothing i.e it is just a greeting or a suggestion 
you have acess to following functions

{serialize_function_to_json(get_product_from_amazon)}



To use these functions respond with:
<multiplefunctions>
    <functioncall> {fn} </functioncall>
</multiplefunctions>



assistant"""

    response_function = openai.chat.completions.create(
        model="gpt-4o",  # Choose the appropriate OpenAI model
        messages=[
            {"role": "system", "content": prompt1}
        ],
        max_tokens=1500
    
    )
    obj = {}
    completion = response.choices[0].message.content
    functions = extract_function_calls(completion)
    CONTEXT.append({"user":prompt2,"assistant":completion.strip()})
    if functions:
        if isinstance(functions, list):  # Check if the result is a list of functions
            for function in functions:
                print(function["name"])
                print(function["arguments"])
    else:
        obj["chat"] = response.choices[0].message.content
        
        
    completion = response_function.choices[0].message.content
    functions = extract_function_calls(completion)
    
    call_data = []
    CONTEXT.append({"user":prompt2,"assistant":completion.strip()})
    data = []
    if functions:
        if isinstance(functions, list):  # Check if the result is a list of functions
            for function in functions:
                d = get_data(function["arguments"]["product_name"])
                if len(d)>0:
                    data.append(d)
    
        
    if len(data)>0:
        obj["function_data"] = data

    return obj

prompts = [
    "suggest me some outfits",    
]

for prompt in prompts:
    result = generate_hermes(prompt)

    if isinstance(result, list):  # Check if the result is a list of functions
        for function in result:
            print(function["name"])
            print(function["arguments"])
    else:
        print(result)

    print("="*100)