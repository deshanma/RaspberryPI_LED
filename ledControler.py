import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(21,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
count = 0
GPIO.setup(4,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)

GPIO.output(18,GPIO.HIGH)
time.sleep(0.4)
GPIO.output(18,GPIO.LOW)
count2 = count + 1

GPIO.output(21,GPIO.HIGH)
time.sleep(0.4)
GPIO.output(21,GPIO.LOW)


GPIO.output(12,GPIO.HIGH)
time.sleep(0.4)
GPIO.output(12,GPIO.LOW)

GPIO.output(22,GPIO.HIGH)
time.sleep(0.4)
GPIO.output(22,GPIO.LOW)

GPIO.output(23,GPIO.HIGH)
time.sleep(0.4)
GPIO.output(23,GPIO.LOW)

GPIO.output(4,GPIO.HIGH)
time.sleep(0.4)
GPIO.output(4,GPIO.LOW)

GPIO.output(12,GPIO.HIGH)
time.sleep(0.4)
GPIO.output(12,GPIO.LOW)
