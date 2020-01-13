import RPi.GPIO as GPIO
import time
led = 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(led,GPIO.OUT)
GPIO.output(led,GPIO.HIGH)
time.sleep(0.5)
GPIO.output(led,GPIO.LOW)
        
        
