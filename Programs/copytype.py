from pynput.keyboard import Key, Controller
from time import sleep
from termios import tcflush, TCIFLUSH
from sys import stdin, stdout

password = raw_input()
timings = raw_input()
#print "password: " + password
#print "timings:  " + timings

password = password.split(",")
lit_password = password[:len(password)/2+1]
lit_password = "".join(lit_password)

#print lit_password

timings = timings.split(",")

timings = [float(a) for a in timings]
keypress = timings[:len(timings)/2+1]
key	= password[:len(password)/2+1]
keyinterval  = timings[len(timings)/2+1:]
keypair = password[len(password)/2+1:]

#print "Key Press:     {}".format(keypress)
#print "Key Intervals: {}".format(keyinterval)

keyboard = Controller()

for k in range(0, len(lit_password)):
	if (keyinterval[k] > 0):
		keyboard.press(key[k])
		sleep(keypress[k])
		keyboard.release(key[k])
		if (k != (len(lit_password)-1)):
			sleep(keyinterval[k])

tcflush(stdout, TCIFLUSH)
print

