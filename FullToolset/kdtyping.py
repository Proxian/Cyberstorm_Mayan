from pynput.keyboard import Key, Controller
from time import sleep
from termios import tcflush, TCIFLUSH
from sys import stdin, stdout

# String to type in
password = ",".join(['T', 'i', 'm', 'o', 'f', 'e', 'y', 'e', 'v', 'Ti', 'im', 'mo', 'of', 'fe', 'ey', 'ye', 'ev'])
# Timings and interval timings
timings = ",".join(['0.46', '0.88', '0.11', '0.46', '0.83', '0.26', '0.62', '0.23', '0.93', '0.61', '0.74', '0.41', '1.00', '0.63', '0.76', '0.27', '0.37'])

# Make a list of the characters
password = password.split(",")
lit_password = password[:len(password)/2+1]
#keypair = password[len(password)/2+1:]
lit_password = "".join(lit_password)

# Make a list of the timings
timings = timings.split(",")

# Change them to floats
timings = [float(a) for a in timings]

# Get key-press times
keypress = timings[:len(timings)/2+1]
# Get key-interval times
keyinterval  = timings[len(timings)/2+1:]

# Initialize the controller
keyboard = Controller()

# Delay
sleep(6)

# Loop over the characters
for k in range(0, len(lit_password)):
        # press the key
	keyboard.press(key[k])
        # hold it down for a select amount of time
	sleep(keypress[k])
	# release the key
	keyboard.release(key[k])
	# time to sleep between releasing one key and pressing another
	if (k != (len(lit_password)-1)):
		sleep(keyinterval[k])

# Flush the output
tcflush(stdout, TCIFLUSH)
print
