import subprocess
import time

#try:
#print ('starting mm')
#print ('try killing'),
#subprocess.run(['./levistopmm']),
#except:
 #   print ('levi error'),
#else:
  #  print ('no error'),
#finally:    
 #   time.sleep(5),
  #  print ('killing'),
   # subprocess.run(['./levistopmm'])
#p=subprocess.Popen(['npm', 'start', '>/dev/null', '2>&1'])
#print ('awake')
#time.sleep(15)
#p.kill()
#time.sleep(5)
#print ('done')
#p=subprocess.Popen(['npm', 'start', '>/dev/null', '2>&1'])
#pid=p.pid
#print ('awake')
#time.sleep(15)
#print ('before kill')
#subprocess.call(['kill', '-9', str(pid)])
#print ('after kill')
#time.sleep(5)
#print ('done')
import threading

print ('I live')
t = threading.Timer(30.0, subprocess.call, [['./levistopmm']])
print ('countdown')
t.start()
#p=subprocess.Popen(['npm', 'start', '>/dev/null', '2>&1'])
print ('now running mm')
subprocess.run(['./levistartmm'])
