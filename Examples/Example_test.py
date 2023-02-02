import RPi.GPIO as GPIO
import serial
import time
from Library import PiTalk_4G


phone_number = '' #Enter your mobile number
time = 100                  #Enter call duration time
text_message = 'Hello from EG25' #Enter your text message want to send

Port = 80      #Enter Port
ServerIP = ''  #Enter your server IP
APN = 'airtelgprs.com' #Enter your APN 

#calling = PiTalk_4G.eg25().Call(phone_number, time)  #Uncomment this function line to use call functionality


#Send_msg = PiTalk_4G.eg25().SendSMessage(phone_number, text_message) #Uncomment this code line to send text message

#rcv_msg = PiTalk_4G.eg25().ReceiveMessage()                         #Uncomment this code line to recieve message/recent information about sim card activities

#tcp  = PiTalk_4G.eg25().TCP(ServerIP, Port, APN,5)                  #Uncomment this code line to use funtionality of tcp

gps = PiTalk_4G.eg25().gps_positioning()   
