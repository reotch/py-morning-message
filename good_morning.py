# a simple welcome to the day
# import time and sys
import time
import sys

# String variables
morning = '\n\nGood morning, Reotch.' 
breathe = '\nTake a deep breath and let\'s get this day going.\n'
end_of_line = '\nEnd of line\n\n'

# function to delay printing letters in a line and provide a longer break after being called
def delay_print(message):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(1.5)

delay_print(morning)
delay_print(breathe)
delay_print(end_of_line)
