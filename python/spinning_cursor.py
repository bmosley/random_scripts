import sys
import time
import itertools

spinner = itertools.cycle(['-', '\\', '|', '/'])

for _ in range(50):
    sys.stdout.write(next(spinner))   # write the next character
    sys.stdout.flush()                # flush stdout buffer (actual character display)
    sys.stdout.write('\b')
    time.sleep(.1)