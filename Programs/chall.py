#!/usr/bin/python2.7

password = "G,o,u,r,d,Go,ou,ur,rd"
timings = ",".join(['0.95', '0.40', '0.74', '0.35', '0.15', '0.16', '0.97', '0.27', '0.89'])

#password = ""
#temp = ""
#try:
#    while temp != "EOF":
#        temp = raw_input()
#        password += temp + "\n"
#except:
#    pass
#password = password[:-4]
#timings = raw_input()
print timings
password = password.split(",")
intervals = password[len(password)/2 + 1:]
password = password[:len(password)/2 + 1]
#password = "".join(password)


timings = timings.split(",")
timings = [float(a) for a in timings]
keyhold = timings[:len(timings)/2 + 1]
keyinterval = timings[len(timings)/2 + 1:]

#print password
#print intervals
#print keyhold
#print keyinterval

from pynput.keyboard import Key, Controller
from time import sleep
from random import uniform
from threading import Thread

keyboard = Controller()

mystr = "This is supposed to be a fake string"

def presskey(index):
    global keyboard, password, keyhold
    keyboard.press(password[index])
    sleep(float(keyhold[c]))
    keyboard.release(password[index])

sleep(2)
for c in range(len(password)):
#    t = Thread(target=presskey, args=(c,))
#    t.start
    keyboard.press(password[c])
    keyboard.release(password[c])
    if c != len(password) - 1:
        sleep(float(keyinterval[c]))
