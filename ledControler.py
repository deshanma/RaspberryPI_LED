import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(21,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)

GPIO.output(18,GPIO.HIGH)
time.sleep(4)
GPIO.output(18,GPIO.LOW)

GPIO.output(21,GPIO.HIGH)
time.sleep(4)
GPIO.output(21,GPIO.LOW)

GPIO.output(12,GPIO.HIGH)
time.sleep(1)
GPIO.output(12,GPIO.LOW)

