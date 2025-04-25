# This script is a simple chatbot that translates user input to English,
# 'source venv/bin/activate' to activate the virtual environment before running this script

import ollama
from translator import translate_to_standard, translate_to_slang

# Initialize the chatbot
def chat_with_bot(user_input):
    # Translate slang to standard Swahili before sending to the model
    translated_input = translate_to_standard(user_input)
    
    # Get the response from LLaMA model (chatbot)
    response = ollama.chat(model='llama3.2', messages=[
        {'role': 'user', 'content': translated_input}
    ])
    
    # Get the bot's response
    bot_reply = response['message']['content']
    
    # Translate bot reply back to slang if needed
    translated_reply = translate_to_slang(bot_reply)
    
    return translated_reply

# Start conversation loop
if __name__ == "__main__":
    while True:
        user_message = input("You: ")
        
        if user_message.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break

        bot_response = chat_with_bot(user_message)
        print("Bot:", bot_response)

