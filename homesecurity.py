########################
# Shazin Sadakath      #
#######################

import RPi.GPIO as GPIO
import time
import telegram
from subprocess import call

sensor = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)

previous_state = False
current_state = False

chat_id = -1
token = "token"

bot = telegram.Bot(token=token)

while True:
	time.sleep(5)
	previous_state = current_state
	current_state = GPIO.input(sensor)
	#print("Current State : %s" % current_state)
	if current_state != previous_state:
		new_state = "HIGH" if current_state else "LOW"
		print("GPIO pin %s is %s" % (sensor, new_state))
		if new_state == "HIGH":
			print("Detected Activity")
			call(["fswebcam", "image.jpg"])
			bot.sendMessage(chat_id=chat_id, text="Some activity detected for the past 5 seconds!")
			bot.sendPhoto(chat_id=chat_id, photo=open("/home/pi/image.jpg"))
	
