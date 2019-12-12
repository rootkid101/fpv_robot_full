try:
  import usocket as socket
except:
  import socket

import machine
from machine import Pin
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = '<ENTER SSID>'
password = '<ENTER PASSWORD'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

p05 = machine.Pin(5)
dir_a = Pin(0, Pin.OUT)
pwm_a = machine.PWM(p05)

p04 = machine.Pin(4)
dir_b = Pin(2, Pin.OUT)
pwm_b = machine.PWM(p04)

pwm_a.freq(500)
pwm_b.freq(500)

#servo
p12 = machine.Pin(12)
servo = machine.PWM(p12, freq=50)
