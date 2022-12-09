from Chat import Chat, reflections
from Pairs import pairs

from naoqi import ALProxy

robotIP = "192.168.2.251"
robotPort = 9559

tts = ALProxy("ALTextToSpeech", robotIP, robotPort)
posture = ALProxy("ALRobotPosture", robotIP, robotPort)
asr = ALProxy("ALSpeechRecognition", robotIP, robotPort) 

eliza_chatbot = Chat(pairs, reflections)

# The following function changes NAO's position between sitting and sitting relaxed
# after every two counts
def chosenPosture(counter):
    if counter%2 == 0:
        posture.goToPosture('SitRelax', 1.0)
    else:
        posture.goToPosture('Sit', 1.0)


asr.setVocabulary(vocabulary, False)

def eliza_chat():
    count = 0
    print('Welcome to NAO. To start, type Hi')
    pre_input = raw_input()
    if pre_input == 'Hi':
        asr.subscribe("Test_ASR") #Subscribe to the Speech recognition with user Test_ASR
        print("Hello. My name is NAO.\nHow are you today?")
        tts.say("Hello. My name is NAO.\nHow are you today?")
        user_input = ""
        quit="quit" or "Quit"
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
                    #print(reply)
                    tts.say(reply)
                    chosenPosture(count)
                    count += 1
        #end while            
        posture.goToPosture('SitRelax', 1.0)
        asr.unsubscribe("Test_ASR") #Unsuscribe from the speech recognition

def demo():
    eliza_chat()


if __name__ == "__main__":
    demo()