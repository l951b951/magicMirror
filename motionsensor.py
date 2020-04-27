import RPi.GPIO as GPIO
import time
import subprocess
import os
import threading

pir_sensor = 11

GPIO.setmode(GPIO.BOARD)

GPIO.setup(pir_sensor, GPIO.IN)

current_state = 0

try:
    while True:
        time.sleep(0.1)
        current_state = GPIO.input(pir_sensor)
        if current_state == 1:
            t = threading.Timer(30.0, subprocess.call, [['/home/pi/MagicMirror/levistopmm']])
            t.start()
            subprocess.run(['/home/pi/MagicMirror/levistartmm'])

except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
