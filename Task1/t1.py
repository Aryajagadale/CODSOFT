# Define a dictionary of predefined rules for the chatbot
chatbot_responses = {
    "hello": "Hello! How can I help you today?",
    "hi": "Hi there! What can I do for you?",
    "how are you": "I'm just a computer program, but I'm here to assist you.",
    "bye": "Goodbye! Have a great day.",
    "what's your name": "I don't have a name, but you can call me Chatbot.",
    "what can you do": "I can answer your questions and assist with tasks.",
    "help": "Sure, I can help with a variety of topics. Just ask me anything!",
    "thank you": "You're welcome! If you have more questions, feel free to ask.",
    "tell me a joke": "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "tell me a fact": "Sure, here's a random fact: Honey never spoils.",
    "tell me a riddle": "I have keys but open no locks, I have space but no room, You can enter, but you can't go inside. What am I?",
    "weather": "I'm sorry, I can't provide real-time weather information. You can check a weather website or app for the current conditions.",
    "news": "I'm sorry, I can't provide real-time news updates. You can check a news website or app for the latest headlines.",
    "who are you": "I'm Chatbot, a computer program designed to assist and answer questions.",
    "where are you from": "I exist in the digital realm, so I don't have a physical location.",
    "default": "I'm sorry, I don't understand. Can you please rephrase that?"
}

# Function to get a response from the chatbot
def get_response(user_input):
    # Convert the user input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Check if the user input matches any predefined rules
    if user_input in chatbot_responses:
        return chatbot_responses[user_input]
    else:
        return chatbot_responses["default"]

# Main loop for the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = get_response(user_input)
    print("Chatbot: " + response)
