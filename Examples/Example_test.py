import RPi.GPIO as GPIO
import serial
import time
from PiTalk_4G import eg25

phone_number = '9118520507' #Enter your mobile number
time = 100                  #Enter call duration time
text_message = 'Hello from EG25' #Enter your text message want to send

Port = 80      #Enter Port
ServerIP = ''  #Enter your server IP
APN = 'airtelgprs.com' #Enter your APN 

#calling = eg25().Call(phone_number, time)  #Uncomment this function line to use call functionality


#Send_msg = eg25().SendSMessage(phone_number, text_message) #Uncomment this code line to send text message

#rcv_msg = eg25().ReceiveMessage()                         #Uncomment this code line to recieve message/recent information about sim card activities

#tcp  = eg25().TCP(ServerIP, Port, APN,5)                  #Uncomment this code line to use funtionality of tcp

gps = eg25().gps_positioning()                         #Uncomment this code line to get gps positining 
