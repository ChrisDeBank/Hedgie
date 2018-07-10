#-------------------------------------------------------------------------------
# PIR Test Bed
#-------------------------------------------------------------------------------

#PIR output connected to GPIO2 (Physical Pin 3)

import gpiozero import MotionSensor

pir = MotionSensor(2)

pir.wait_for_motion()
print("Motion Detected!!)
