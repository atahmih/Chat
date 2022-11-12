# from nltk.chat.util import reflections
from Chat import Chat, reflections
from Pairs import pairs
#reflections is a pre-defined set of queries and answers eg I am and You are

#The pairs define a query and response list for the conversation. 
# Include the pairs of queries and replies it gives
#It uses Regex to get input and replies it as output

eliza_chatbot = Chat(pairs, reflections)

##Refer to Lib -> nltk -> util.py for modifications
def eliza_chat():
    print("Psychiatrist\n---------")
    print("Talk to the program by typing in plain English, using normal upper-")
    print('and lower-case letters and punctuation.  Enter "quit" when done.')
    print("=" * 72)
    print("Hello. My name is Eliza.\nHow are you feeling today?")
    
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