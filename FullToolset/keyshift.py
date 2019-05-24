
### LIBRARIES ###
import sys
import string

### CONSTANTS ###


# the alphabet
ucase = string.ascii_uppercase
lcase = string.ascii_lowercase
allletters = string.ascii_letters
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\|;:'" + "\\" + ",<.>/? "
otheralphabet = "Teflon'sabcdghijkmpqrtuvwxyzABCDEFGHIJKLMNOPQRSUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\|;:\",<.>/? "

key = ""
mydict = ""

if len(sys.argv) == 2:
    try:
        inputfile = open(sys.argv[1], "r")
        myfile = inputfile.read()
        inputfile.close()
    except:
        print "Could not open file {}".format(sys.argv[1])
        exit(1)
elif len(sys.argv) == 3:
    try:
        inputfile = open(sys.argv[1], "r")
        myfile = inputfile.read()
        inputfile.close()
    except:
        print "Could not open file {}".format(sys.argv[1])
        exit(1)
    key = sys.argv[2]
else:
    print "Usage: python keyshift.py <inputfile> (key)"
    exit(0)

try:
    dictionary = open("dictionary.txt", "r")
    mydict = dictionary.read()
    dictionary.close()
except:
    print "Could not find 'dictionary.txt' in current directory!"
    print "Using {} as the key".format(key)

if mydict == "" or key != "":
    tmpalphabet = alphabet
    for i in key:
        tmpalphabet = tmpalphabet.replace(i, "")
        "".replace(i, "")
    otheralphabet = key + tmpalphabet
    newtext = ""
    for i in myfile:
        if i in alphabet:
            newtext += alphabet[otheralphabet.index(i)]
    print newtext
    
else:
    for key in mydict.split("\n"):
        key = "".join(sorted(set(key), key=key.index))
        tmpalphabet = alphabet
        for i in key:
            tmpalphabet = tmpalphabet.replace(i, "")
        otheralphabet = key + tmpalphabet
        newtext = ""
        for i in myfile:
            if i in alphabet:
                newtext += alphabet[otheralphabet.index(i)]
        txtsize = len(newtext.split(" "))
        checksize = 0
        for i in newtext.split(" "):
            if i in mydict.split("\n"):
                checksize += 1
        if checksize >= txtsize*0.5:
            print "KEY={}".format(key)
            print newtext
