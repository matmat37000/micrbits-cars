from microbit import *

# def setServoSpeed(pin, direction, speed):
#   pin.set_analog_period(20)
#   if (speed >= 0 and speed <= 100):
#     if direction is 1 or direction is -1:
#       #clockwise: 1.5 ms to 1 ms | anticlockwise: 1.5ms to 2 ms (0 to 100%)
#       speed_ms = speed * direction * 0.5 / 100 + 1.5
#       pin.write_analog(1023 * speed_ms / 20)
#     else:
#       raise ValueError("continuous servomotor has no direction: '" + str(direction) + "'")
#   else:
#     raise ValueError("continuous servomotor speed is out of range: '" + str(speed) + "'")
# 
# setServoSpeed(pin2, 1, 100)

def setServoAngle(pin, angle):
  if (angle >= 0 and angle <= 180):
    pin.write_analog(int(0.025*1023 + (angle*0.1*1023)/180))
  else:
    raise ValueError("Servomotor angle have to be set between 0 and 180")

# setServoAngle(pin2, 180)

while True:
    setServoAngle(pin2, 180)
#     pin2.write_analog(1023)