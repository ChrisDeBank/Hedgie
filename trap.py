#-------------------------------------------------------------------------------
# Complete Camera Trap Program
#-------------------------------------------------------------------------------
#PIR output connected to GPIO4 (Physical Pin 7)

from picamera import PiCamera
from time import sleep
from gpiozero import MotionSensor

pir = MotionSensor(4)
camera = PiCamera()

pir.wait_for_motion()
print("Motion Detected!!")

camera.rotation = 180
camera.start_preview()
sleep(10)
camera.stop_preview()

#camera.capture('foo.jpg')