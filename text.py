import random
import time

from naoqi import ALProxy
from optparse import OptionParser

NAO_IP = "192.168.1.41"
NAO_PORT = 9559

PLAYER = "Player"
NAO = "NAO Robot"


DIALOGUE_WIN = [x.strip() for x in open("win.txt", "r").readlines()]
DIALOGUE_LOSE = [x.strip() for x in open("lose.txt", "r").readlines()]
DIALOGUE_TURN = [x.strip() for x in open("turn.txt", "r").readlines()]

is_console = False

loser = None

tts = None
leds = None
motion = None
posture = None

is_neurotic = False
counter = 0


def posture(name):
	global is_console
	if not is_console:
		global posture
		posture.goToPosture(name, 0.5)