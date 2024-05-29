

import openai

# Set your OpenAI API key
openai.api_key = 'sk-proj-CwqKG9kVjdNcHJzYPKNbT3BlbkFJY10LuFXiQH1UwaAneexB'

def call_openai(prompt):
    try:
        # Call the OpenAI API to get a completion for the prompt
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            stream=True,
        )
        
        # Extract and return the generated text from the API response
        return response.choices[0].text.strip()
    except Exception as e:
        # Handle any API call errors
        print("Error calling OpenAI API:", e)
        return None

# Example prompt
prompt_text = "Once upon a time, in a far-off kingdom, there was a brave knight"

# Call the OpenAI API with the prompt and print the response
response_text = call_openai(prompt_text)
if response_text:
    print("Response from OpenAI:")
    print(response_text)

try:
    # Execute the user's code using exec()
    exec(user_code)
except Exception as e:
    # Handle any exceptions that occur during execution
    print("An error occurred:", e)