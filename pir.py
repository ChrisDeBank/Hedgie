#-------------------------------------------------------------------------------
# PIR Test Bed
#-------------------------------------------------------------------------------

#PIR output connected to GPIO4 (Physical Pin 7)

from gpiozero import MotionSensor

pir = MotionSensor(4)
pir.wait_for_motion()
print("Motion Detected!!")
