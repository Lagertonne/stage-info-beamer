#!/usr/bin/python3

import socket
import time
import RPi.GPIO as GPIO
import simpleaudio as sa

wave_obj = sa.WaveObject.from_wave_file("Horn.wav")

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

bl = 2
br = 3

GPIO.setup(bl, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(br, GPIO.IN, GPIO.PUD_UP)

UDP_IP = "127.0.0.1"
UDP_PORT = 4444

NODE_NAME = ""
BL_ON = NODE_NAME + "/buzzer:bl_on"
BL_OFF = NODE_NAME + "/buzzer:bl_off"
BR_ON = NODE_NAME + "/buzzer:br_on"
BR_OFF = NODE_NAME + "/buzzer:br_off"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    if GPIO.input(bl) == False:
        sock.sendto(BL_ON.encode(), (UDP_IP, UDP_PORT))
        print("Buzzer Left On.\n")
        play_obj = wave_obj.play()
        play_obj.wait_done()
        time.sleep(1.5)
        sock.sendto(BL_OFF.encode(), (UDP_IP, UDP_PORT))
        print("Buzzer Left Off.\n")
    if GPIO.input(br) == False:
        sock.sendto(BR_ON.encode(), (UDP_IP, UDP_PORT))
        print("Buzzer Right On.\n")
        play_obj = wave_obj.play()
        play_obj.wait_done()
        time.sleep(1.5)
        sock.sendto(BR_OFF.encode(), (UDP_IP, UDP_PORT))
        print("Buzzer Right off.\n")



