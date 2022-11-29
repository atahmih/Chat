from Chat import Chat, reflections
from Pairs import pairs

eliza_chatbot = Chat(pairs, reflections)

##Refer to Lib -> nltk -> util.py for modifications
def eliza_chat():
    pre_input = input()
    if pre_input == 'Hi':
        print("Hello. My name is NAO.\nHow are you feeling today?")
        user_input = ""
        quit="quit"
        while user_input != quit:
                user_input = quit
                try:
                    user_input = input(">")
                except EOFError:
                    print(user_input)
                if user_input:                    
                    while user_input[-1] in "!.":
                        user_input = user_input[:-1]               
                    reply = eliza_chatbot.converse(user_input)
                    print(reply)
  
        



def demo():
    eliza_chat()

if __name__ == "__main__":
    demo()