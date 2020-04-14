# Good Morning Py

A simple script that animates a message welcoming you to the day—with ominous foreshadowing.

```
import time
import sys

morning = '\n\nGood morning, Reotch.'
breathe = '\nTake a deep breath and let\'s get this day going.\n'
end_of_line = '\nEnd of line\n\n'

def delay_print(message):
	for char in message:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(0.05)
	time.sleep(1.5)
	
delay_print(morning)
delay_print(breathe)
delay_print(end_of_line)
```
