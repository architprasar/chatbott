from funai import ask_llm
from function_extractor import serialize_function_to_json,get_all_functions_from_module,extract_function_calls
from functions import amazon_functions
def function_runner(query):
    available_functions = get_all_functions_from_module(amazon_functions)
    print(available_functions)
    for function in available_functions:
        print(function)
    
    
    # result = ask_llm(query)
    # functions = extract_function_calls(result)

    # if isinstance(functions, list):  # Check if the result is a list of functions
    #     for function in result:
    #         print(function["name"])
    #         print(function["arguments"])
    # else:
    #     print(result)
function_runner("hello")