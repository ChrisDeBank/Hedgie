#-------------------------------------------------------------------------------
# PIR Test Bed
#-------------------------------------------------------------------------------

#PIR output connected to GPIO2 (Physical Pin 3)

from gpiozero import MotionSensor

pir = MotionSensor(4)
pir.wait_for_motion()
print("Motion Detected!!")
