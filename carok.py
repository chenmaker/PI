import RPi.GPIO as GPIO
import picamera
import time
c = 1
var = 1
while var >0 :
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(23,GPIO.OUT)
    GPIO.setwarnings(False)
    time.sleep(0.000002)
    GPIO.output(23,1)
    time.sleep(0.000005)
    GPIO.output(23,0)
    GPIO.setup(23,GPIO.IN)
    while GPIO.input(23)==0:
        starttime=time.time()
    while GPIO.input(23)==1:
        endtime=time.time()   
    duration=endtime-starttime
    distance=duration*34000/2
    time.sleep(0.001)
    print('cm='+str(distance))
   #print distance
    if distance < 20:
        while c > 0 :
            from pygame import mixer
            mixer.init()
            mixer.music.load('OK.mp3')
            mixer.music.play()
            with picamera.PiCamera() as camera:
               camera.resolution =(720,720)
               camera.start_preview()
               camera.start_recording(str(c)+'.h264')
               camera.wait_recording(1)
               camera.stop_recording()
               #time.sleep(5)
               c += 1
               print('c='+str(c))
               break               
    var += 1
    print('var='+str(var))
