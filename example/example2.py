import time
import pigpio

# $env:GPIOZERO_PIN_FACTORY = "pigpio"
# $env:PIGPIO_ADDR = "raspberrypi.local"


pi = pigpio.pi()

if not pi.connected:
   exit(0)

state = True
while True:
   print("Turning:", state)
   pi.write(14, 1 if state else 0)
   state = not state
   time.sleep(2)


pi.stop()
