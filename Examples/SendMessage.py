import RPi.GPIO as GPIO
import serial
import time
from Library import PiTalk_4G


phone_number = '' #Enter your mobile number
text_message = 'Hello from EG25' #Enter your text message want to send



Send_msg = PiTalk_4G.eg25().SendSMessage(phone_number, text_message) #Uncomment this code line to send text message

