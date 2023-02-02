import RPi.GPIO as GPIO
import serial
import time
from Library import PiTalk_4G


phone_number = ''         #Enter your mobile number
time = 100                  #Enter call duration time



calling = PiTalk_4G.eg25().Call(phone_number, time)  #Uncomment this function line to use call functionality
