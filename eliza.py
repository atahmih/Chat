from Chat import Chat, reflections
from Pairs import pairs

eliza_chatbot = Chat(pairs, reflections)

#Vocabulary initializes the list of words that can be recognized for SpeechReg
#It is built during the trial run with the users and imported during the speech reg

vocabulary = []

def eliza_chat():
    pre_input = raw_input("Welcome to NAO. Type Hi to begin\n")
    if pre_input == 'Hi':
        print("Hello. My name is NAO.\nHow are you today?")
        user_input = ""
        quit="quit"
        while user_input != quit:
                user_input = quit
                try:
                    user_input = raw_input(">")
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