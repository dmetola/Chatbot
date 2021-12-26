from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("Randall")
# trainer = ChatterBotCorpusTrainer(chatbot)
# trainer.train('chatterbot.corpus.english')

def user_input():
    name = "Randall"
    prompt = "(Say 'goodbye' to end the conversation.)\n"
    prompt += "You: "
    message = ''
    while True:
        message = input(prompt)
        if message == 'goodbye':
            print(f"{name}: Goodbye")
            break
        if message == "What's your name?":
            print(f"{name}: My name is Randall")
            message = input(prompt)
        if message == "What is your name?":
            print(f"{name}: My name is Randall")
            message = input(prompt)
        response = chatbot.get_response(message)
        print(f"{name}: {response}")

user_input()   
