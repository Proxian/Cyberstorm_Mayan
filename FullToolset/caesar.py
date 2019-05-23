
### LIBRARIES ###
import sys
import string

### CONSTANTS ###

# Loop?
LOOP = True
ROT = 0

# the alphabet
ucase = string.ascii_uppercase
lcase = string.ascii_lowercase
allletters = string.ascii_letters
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\|;:'\",<.>/? "
alphabet = ' -,;:!?/.' + "'" + '"()[]$&#%012345789aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxyYzZ'

if len(sys.argv) == 2:
    try:
        inputfile = open(sys.argv[1], "r")
        myfile = inputfile.read()
    except:
        print "Could not open file {}".format(sys.argv[1])
        exit(1)
elif len(sys.argv) == 3:
    try:
        inputfile = open(sys.argv[1], "r")
        myfile = inputfile.read()
    except:
        print "Could not open file {}".format(sys.argv[1])
        exit(1)
    if sys.argv[2].isdigit():
        ROT = int(sys.argv[2])
    else:
        print "{} is noot a usable number for shift".format(sys.argv[2])
else:
    print "Usage: python caesar.py <inputfile> (ROT#)"
    exit(0)

if LOOP or ROT != 0:
    for i in range(len(alphabet)):
        newalphabet = ""
        for j in range(len(alphabet)):
            newalphabet += alphabet[(j+i) % len(alphabet)]
        newtext = ""
        for k in myfile:
            if k in alphabet:
                newtext += alphabet[newalphabet.index(k)]
            elif k == '\n':
                pass
            else:
                newtext += k
        print newtext
else:
    newalphabet = ""
    newtext = ""
    for i in range(len(alphabet)):
        newalphabet += alphabet[(i+ROT) % len(alphabet)]
    for k in myfile:
        if k in alphabet:
            newtext += alphabet[newalphabet.index(k)]
        elif k == '\n':
            pass
        else:
            newtext += k
    print newtext
