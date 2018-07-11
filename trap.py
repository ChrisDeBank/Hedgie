#-------------------------------------------------------------------------------
# Complete Camera Trap Program
#-------------------------------------------------------------------------------
#PIR output connected to GPIO4 (Physical Pin 7)

from picamera import PiCamera
import time
from gpiozero import MotionSensor

pir = MotionSensor(4)
camera = PiCamera()
#camera.resolution(640,480)

file_name = 'foo.h264'

#pir.wait_for_motion()
#print("Motion Detected!!")

#camera.rotation = 180
#camera.start_preview()
#sleep(10)
#camera.stop_preview()

#camera.capture('foo.jpg')

while(True)
	pir.wait_for_motion()
	file_name = time.strftime("%y%m%d") + "_" + time.strftime("%H%M%S") + ".h264"
	camera.start_recording(file_name)
	camera.wait_recording(60)
	camera.stop_recording()


#print(file_name)


