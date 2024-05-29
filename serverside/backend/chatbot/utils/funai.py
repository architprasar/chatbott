import openai


openai.api_key = "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"

def ask_llm(prompt,functions):
    fn = """{"name": "function_name", "arguments": {"arg_1": "value_1", "arg_2": value_2, ...}}"""
    chat_prompt = f"""system
You are a helpful assistant with access to the following functions:

{functions}

To use these functions respond with:
<multiplefunctions>
    <functioncall> {fn} </functioncall>
    <functioncall> {fn} </functioncall>
    ...
</multiplefunctions>

Edge cases you must handle:
- If there are no functions that match the user request, you will respond with the way to get that solution solved through internet
user
{prompt}
assistant"""

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  
        temperature=0.5,
        messages=[
            {"role": "system", "content": chat_prompt}
        ],
        max_tokens=150
    )

    completion = response.choices[0].message.content
    return completion



    