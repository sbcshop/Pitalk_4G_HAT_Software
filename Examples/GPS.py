import RPi.GPIO as GPIO
import serial
import time
from Library import PiTalk_4G




gps = PiTalk_4G.eg25().gps_positioning()   