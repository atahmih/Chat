import time
from naoqi import ALProxy


robotIP = "192.168.2.251"
robotPort = 9559

# Creates a proxy on the speech-recognition module
asr = ALProxy("ALSpeechRecognition", robotIP, robotPort)

asr.setLanguage("English")

# Example: Adds "yes", "no" and "please" to the vocabulary (without wordspotting)
vocabulary = ["yes", "no", "please"]
asr.setVocabulary(vocabulary, False)

# Start the speech recognition engine with user Test_ASR
asr.subscribe("Test_ASR")
print 'Speech recognition engine started'
phrase = WordRecognized()
print(word)
# time.sleep(20)
asr.unsubscribe("Test_ASR")