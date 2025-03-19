# # pip install -U g4f
# import g4f


# messages = [{"role": "system ", 
#              "content": " You are the AI WahWah virtual assistant. " + " The one with latest version of MKML technology"},
#             {"role": "system", "content": "Coded by MKML corporation technology"},
#             {"role": "system", 
#              "content": "use modules like webbrowser, pyautogui, time,pyperclip, random, mouse, wikipedia, keyboard, datatime, tkinter, pyqt5 etc"},
#             {"role": "user", "content": "open google chrome"},
#             {"role": "assistant", 
#              "content": "```python\nimport webbrowser\nwebbrowser.open('https://www.google.com')```"}
#             ]
 
# def ChatGpt(message:str):
#     # assert message == ""
#     global messages
    
#     messages.append({"role": "user", "content": message})

#     response = g4f.ChatCompletion.create(
#         model = "llama-3.3-70b",
#         provider = g4f.Provider.bing,
#         messages= messages,
#         stream = True,
#     )
#     ms= ""
#     for message in response:
#         ms += message
#         print(message, end="", flush=True)
#     # print()
#     messages.append({"role": "assistant", "content": ms})
#     return ms   

# ChatGpt("How are you?")     

import logging
from transformers import pipeline

# Suppress device setup messages from the transformers library
logging.getLogger("transformers").setLevel(logging.ERROR)

# Load the GPT-2 model (you can choose another model if needed)
generator = pipeline("text-generation", model="gpt2", device=0)  # -1 means CPU usage

# Define your chat function
def ChatGpt(message: str):
    try:
        # Generate a response using Hugging Face's GPT-2
        response = generator(message, max_length=100, num_return_sequences=1, pad_token_id=50256, truncation=True)
        
        # Get only the generated text (excluding the prompt)
        ms = response[0]['generated_text']
        
        # Print the result
        print(ms[len(message):], end="", flush=True)
        
        return ms[len(message):]  # Return the generated text
    
    except Exception as e:
        print(f"Error: {e}")
        return "An error occurred."

# Test the function
response = ChatGpt("Who are you?")
print(f"Response: {response}")



