#!/usr/bin/python

 ####################################################################
#                                                                   #
#   Authors: Justin Berthelot, Dawson Markham, Matthew Eldridge     #
#   Ryan Utley, Caleb Snook, Emily Rumfola, Valentin Le Gall        #
#   Github link: https://github.com/Proxian/Cyberstorm_Mayan/       #                                                                #
#                                                                   #
#   Date: 03 / 21 / 19                                              #
#   Description: A programmatic mathematically based method of      #
#                implementing the Vigenere Cipher.                  #
#                                                                   #
####################################################################


### LIBRARIES ###
import string
from sys import stdin,stdout,argv

### GLOBALS ###
lower = string.ascii_lowercase
upper = string.ascii_uppercase

### FUNCTIONS ###

# Prints a generic help screen
def PrintHelp():
    print "Usage: './NAMEOFFILE -option key'"
    print "\tOptions:"
    print "\t\t-e : encode with key"
    print "\t\t-d : decode with key"
    print "\t\t-h : display this screen"
    print "\n\tEX: './NAMEOFFILE -d MyKey'\n"

# Vigenere encoding of given data with a given key
#   Algorithm: (index(data) + index(key)) % 26
def EncodeData(data, key):
    # keep track of the index of the key as we loop over the data
    keysize = (len(key) - 1)
    keyindex = 0
    # initialize a string to add to later
    newdata = ""

    # Loop over each character in the data
    for letter in data:
        # Non-alphabetical character in key
        if not(key[keyindex].isalpha()):
            # get to the next alphabetical character
            while not(key[keyindex].isalpha()):
                if keyindex != keysize:
                    keyindex += 1
                else:
                    keyindex = 0
        # lowercase character in data
        if letter in lower:
            # lowercase key
            if key[keyindex] in lower:
                newdata += lower[((lower.index(letter) + lower.index(key[keyindex])) % len(lower))]
            # uppercase key
            elif key[keyindex] in upper:
                newdata += lower[((lower.index(letter) + upper.index(key[keyindex])) % len(lower))]
        # uppercase character in data
        elif letter in upper:
            # uppercase key
            if key[keyindex] in upper:
                newdata += upper[((upper.index(letter) + upper.index(key[keyindex])) % len(upper))]
            # lowercase key
            elif key[keyindex] in lower:
                newdata += upper[((upper.index(letter) + lower.index(key[keyindex])) % len(upper))]
        # Non-alphabetical character in data
        else:
            newdata += letter
            # next iteration (do not increment keyindex)
            continue
        # get the next character
        if keyindex != keysize:
            keyindex += 1
        else:
            keyindex = 0
            
    # return encoded data
    return newdata;

# Vigenere encoding of given data with a given key
#   Algorithm: (26 + index(data) - index(key)) % 26
#    (26 handles the negative numbers)
def DecodeData(data, key):
    # keep track of the index of the key as we loop over the data
    keysize = (len(key) - 1)
    keyindex = 0
    # initialize a string to add to later
    newdata = ""
    
    # Loop over each character in the data
    for letter in data:
        # Non-alphabetical character in key
        if not(key[keyindex].isalpha()):
            # get to the next alphabetical character
            while not(key[keyindex].isalpha()):
                if keyindex != keysize:
                    keyindex += 1
                else:
                    keyindex = 0
        
        # lowercase character in data
        if letter in lower:
            # lowercase key
            if key[keyindex] in lower:
                newdata += lower[((26 + lower.index(letter) - lower.index(key[keyindex])) % len(lower))]
            # uppercase key
            elif key[keyindex] in upper:
                newdata += lower[((26 + lower.index(letter) - upper.index(key[keyindex])) % len(lower))]
        # uppercase character in data
        elif letter in upper:
            # uppercase key
            if key[keyindex] in upper:
                newdata += upper[((26 + upper.index(letter) - upper.index(key[keyindex])) % len(upper))]
            # lowercase key
            elif key[keyindex] in lower:
                newdata += upper[((26 + upper.index(letter) - lower.index(key[keyindex])) % len(upper))]
        # Non-alphabetical character in data
        else:
            newdata += letter
            # next iteration (do not increment keyindex)
            continue
        # get the next character
        if keyindex != keysize:
            keyindex += 1
        else:
            keyindex = 0
            
    # return decoded data
    return newdata;

#Main function
# manages user input and tokens
def Main():
    # only take 3 argument input
    if (len(argv) == 3):
        # encoding
        if (argv[1] == "-e"):
            # get user input
            data = raw_input()
            # possible error in assigning EOFError to data variable
            try:
                # loop
                while data != chr(4):
                    # print encoded input with the key
                    print EncodeData(data, argv[2])
                    # grab the next input
                    data = raw_input()
            # If at EOF, act like nothing happened
            except EOFError:
                pass
        # decoding
        elif (argv[1] == "-d"):
            # get user input
            data = raw_input()
            # possible error in assigning EOFError to data variable
            try:
                # loop
                while data != chr(4):
                    # print encoded input with the key
                    print DecodeData(data, argv[2])
                    # grab the next input
                    data = raw_input()
            # If at EOF, act like nothing happened
            except EOFError:
                pass
        # help option
        elif (argv[1] == "-h"):
            PrintHelp();
        # if no options, tell the user what to do
        else:
            print "Usage: './NAMEOFFILE -option key'"
    # wrong number of arguments
    else:
        print "Usage: './NAMEOFFILE -option key'"
        exit(1)

### MAIN PROGRAM ###
Main()
