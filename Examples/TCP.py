import RPi.GPIO as GPIO
import serial
import time
from Library import PiTalk_4G


Port = 80      #Enter Port
ServerIP = ''  #Enter your server IP
APN = 'airtelgprs.com' #Enter your APN 

                
tcp  = PiTalk_4G.eg25().TCP(ServerIP, Port, APN,5)                  #Uncomment this code line to use funtionality of tcp

