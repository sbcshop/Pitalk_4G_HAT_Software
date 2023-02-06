# Pitalk 4G HAT

<img src ="https://github.com/sbcshop/Pitalk_4G_HAT_Software/blob/main/images/Pi%20talk.png" />

The PiTalk 4G HAT is a handy, low-power Raspberry Pi HAT that features multi-communication functionalities such as GSM, GPRS, TCP, etc. It allows your Pi to easily make phone calls, send messages, connect to wireless networks, and so on. It is the most convenient IoT HAT that works with all variants of Raspberry Pi (model A, B and Zero). The users can also connect PiTalk with other iOS and Android devices as well. It is primarily designed to offer connection to your IoT projects and applications without requiring a Wi-Fi network or ethernet connections. 

## Key Features Of EG25-G:

* Supply voltage: 3.3–4.3 V.
* **LTE Features:**
  *  Support up to non-CA Cat 4 FDD and TDD.
  * Support 1.4/3/5/10/15/20 MHz RF bandwidth.
  * Support MIMO in DL direction.
  * LTE-FDD: Max. 150 Mbps (DL), Max. 50 Mbps (UL).
  * LTE-TDD: Max. 130 Mbps (DL), Max. 30 Mbps (UL).
  
* **UMTS Features:**
  * Support 3GPP R8 DC-HSDPA, HSPA+, HSDPA, HSUPA and WCDMA.
  * Support QPSK, 16-QAM and 64-QAM modulation.
  * DC-HSDPA: Max. 42 Mbps (DL).
  * HSUPA: Max. 5.76 Mbps (UL).
  * WCDMA: Max. 384 kbps (DL), Max. 384 kbps (UL).

* **GSM Features:**
  * Support GPRS multi-slot class 33 (33 by default).
  * Coding scheme: CS-1, CS-2, CS-3 and CS-4.
  * Max. 107 kbps (DL), Max. 85.6 kbps (UL).
  
* **Internet Protocol Features:** 
  * Support TCP/UDP/PPP/FTP/FTPS/HTTP/HTTPS/NTP/PING/QMI/NITZ/SMTP/SSL/MQTT/CMUX/SMTPS/FILE/MMS* protocols.
  * Support PAP (Password Authentication Protocol) and CHAP (Challenge Handshake Authentication Protocol) protocols which are usually used for PPP connections.

* **SMS:**
  * Text and PDU modes
  * Point-to-point MO and MT
  * SMS cell broadcast
  * SMS storage: ME by default

* For more key features of EG25-G Module [click here](https://github.com/sbcshop/Pitalk_4G_HAT_Software/blob/main/Quectel_EG25-Standard_Specification.pdf)

<img src ="https://github.com/sbcshop/Pitalk_4G_HAT_Software/blob/main/images/PiTalkPinouts.png" />


## Setup PiTalk 4G HAT with RPi 

To Start working with our PiTalk 4G HAT, set-up your Raspberry Pi or RockPi by flashing their os file and boot it, for this [click here](https://rockpi.eu/Rockpi4/downloads).

* After setup your Pi board, attach the PiTalk 4 HAT on it and boot by providing compatible power supply.
* Now, open the command prompt and type the following command to clone the current repository in your Pi-board.
```
git clone https://github.com/sbcshop/Pitalk_4G_HAT_Software.git
```

* After, downloading this repository you will see two directory in it. One is of ***Example code*** and 2nd one is of ***Library*** file.
* Now, open the both Example and Library directory. To open these files make sure you have python installed in your Pi board.
* In examples Directory there are some example codes to use the different functionality of PiTalk HAT you have ***move out the example file*** which you want to run from the ***Examples directory*** and after that run the code by make some editing if require.


## Setup PiTalk 4G  Via USB

<img src ="https://github.com/sbcshop/Pitalk_4G_HAT_Software/blob/main/images/Pitalk%20usb.jpg" />

* We have also provided the USB feature in our PiTalk 4G HAT to use this HAT as dongle. For this you have to to install its ***USB driver*** provided in this Repository. For this download and unzip the zip file of it and ***install*** in your computer system.

* After setup it, insert SIM card and attach 4G antenna to it and plugin it in your system via USB type-C cable and press the ***PWRKEY*** button for 3-4seconds to activate the module, ***NETLIGHT*** will start blinking. If everything goes well it will connect as a cellular network in your system. You can also open the device manager to see ***COM Port of Quectel*** device showing as in below image:

<img src ="https://github.com/sbcshop/PiTalk_4G_Dongle_Software/blob/main/images/Scr6.png" />

<img src ="https://github.com/sbcshop/PiTalk_4G_Dongle_Software/blob/main/images/Scr7.png" />

* After the succesfull connection to your PiTalk 4G HAT board you will be able to use your cellular network to connect with internet. 


## Documentation

* [PiTalk-4G HAT Hardware](https://github.com/sbcshop/Pitalk_4G_HAT_Hardware)
* [Getting Started with Raspberry Pi](https://www.raspberrypi.com/documentation/computers/getting-started.html)
* [Raspberry Pi Pico Official website](https://www.raspberrypi.com/documentation/microcontrollers/)
* [Raspberry Pi Datasheet](https://www.raspberrypi.com/documentation/computers/compute-module.html)
* [Raspberry Hardware Design](https://www.raspberrypi.com/documentation/computers/compute-module.html)
* [Raspberry Pi](https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html)

## Our Other GSM Based Products:

* [**PiTalk**]()
* [**PiTalk 2G HAT**](https://github.com/sbcshop/Pitalk_2G_HAT_Software)
* [**PiTalk 4G Dongle**]()
* [**PiTalk 4G HAT**](itself)


## Related Products

* [PiTalk](https://shop.sb-components.co.uk/products/pitalk-modular-smartphone-for-raspberry-pi?variant=12516562436179)

 ![PiTalk](https://cdn.shopify.com/s/files/1/1217/2104/products/PiTalk_-_Modular_SmartPhone_for_Raspberry_Pi_5.png?v=1528805795&width=400)

## Product License

This is ***open source*** product. Kindly check LICENSE.md file for more information.

Please contact support@sb-components.co.uk for technical support.
<p align="center">
  <img width="360" height="100" src="https://cdn.shopify.com/s/files/1/1217/2104/files/Logo_sb_component_3.png?v=1666086771&width=350">
</p>
