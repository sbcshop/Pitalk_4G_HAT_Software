import RPi.GPIO as GPIO
import serial
import time
from Library import PiTalk_4G


rcv_msg = PiTalk_4G.eg25().ReceiveMessage()                         #Uncomment this code line to recieve message/recent information about sim card activities

