import subprocess as s 
import time
i = 0
while i < 1: #infinite loop
	time.sleep(10)
	s.call(['notify-send', 'John', 'Take a break'])
	
