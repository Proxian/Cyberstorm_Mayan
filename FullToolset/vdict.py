import sys

# the alphabet
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\|;:'\",<.>/? "
alphabet = " -,;:!?/.'" + '"' + "()[]$&#%012345789aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxyYzZ"


if len(sys.argv) == 2:
    try:
        inputfile = open(sys.argv[1], "r")
        myfile = inputfile.read()
        inputfile.close()
    except:
        print "Could not open file {}".format(sys.argv[1])
        exit(1)
else:
    print "Usage: python vdict.py <inputfile>"
    exit(0)

try:
    dictionary = open("dictionary.txt", "r")
    mydict = dictionary.read()
    dictionary.close()
except:
    print "Could not find 'dictionary.txt' in current directory!"
    print "Using {} as the key".format(key)

# Loop over each character in the data
for key in mydict.split("\n"):
    # keep track of the index of the key as we loop over the data
    if key == "":
        continue
    keysize = len(key)
    keyindex = 0
    # initialize a string to add to later
    newdata = ""
    for letter in myfile:
        if not key[keyindex] in alphabet:
            # get to the next alphabetical character
            while not key[keyindex] in alphabet:
                if keyindex != keysize:
                    keyindex += 1
                else:
                    keyindex = 0
        if letter in alphabet:
            newdata += alphabet[((alphabet.index(letter) - alphabet.index(key[keyindex])) % len(alphabet))]
        else:
            newdata += letter
            # next iteration (do not increment keyindex)
            continue
        # get the next character
        if keyindex+1 != keysize:
            keyindex += 1
        else:
            keyindex = 0
    txtsize = len(newdata.split(" "))
    checksize = 0
    for i in newdata.split(" "):
        if i in mydict.split("\n"):
            checksize += 1
    if checksize >= txtsize*0.5:
        print "KEY={}".format(key)
        print newdata
