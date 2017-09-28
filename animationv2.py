import time
import sys

string = "this is a test"

# setup string
sys.stdout.write(string)
sys.stdout.flush()

for i in range(0, 100):
    sys.stdout.write("\b" * len(string))
    time.sleep(0.1) # do real work here
    # update the bar
    sys.stdout.write(string[:(i % len(string))].lower() + string[(i % len(string)):].capitalize())
    sys.stdout.flush()

sys.stdout.write("\n")