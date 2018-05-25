import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)

count = 0
while count < 9:
    print("open")
    GPIO.output(18,GPIO.HIGH)
    time.sleep(0.2)
    print(count)
    count += 1
    GPIO.output(18,GPIO.LOW)
    print("close")
    time.sleep(0.2)
