import subprocess
import time
import threading

print ('I live')
t = threading.Timer(10.0, subprocess.call, [['./levistopmm']])
print ('countdown')
t.start()
print ('now running mm')
subprocess.run(['./levistartmm'])
