#!/usr/bin/python

 ########################################################################
#                                                                       #
#   Authors: Justin Berthelot, Dawson Markham, Matthew Eldrige,         #
#   Ryan Utley, Caleb Snook, Emily Rumfola, Valentin Le Gall            #
#   Github link: https://github.com/Proxian/Cyberstorm_Mayan/           #
#                                                                       #
#   Date: 03 / 21 / 19                                                  #
#   Description: Binary Decoder (7 and 8 bit), Vigenere Cipher,         #
#                   and TimeLock programs with returnable functions.    #
#                                                                       #
########################################################################

### LIBRARIES ###
from sys import stdout
import string
import time
import hashlib
from ftplib import FTP

### GLOBALS ###
lower = string.ascii_lowercase
upper = string.ascii_uppercase
VALID_TIME = 60 # TimeLock Time

### FUNCTIONS ###

# 8-bit binary conversion
def Bin8Bit(data):
    bindata = ""
    # Loops over the data in 8-bit increments
    for i in range(0,len(data),8):
        # prints the ASCII equivalent character
        bindata += chr(int(data[i:i+8], 2))
    return bindata;
        
# 7-bit binary conversion
def Bin7Bit(data):
    bindata = ""
    # Loops over the data in 7-bit increments
    for i in range(0,len(data),7):
        # prints the ASCII equivalent character
        bindata += chr(int(data[i:i+7], 2))
    return bindata;

# Vigenere encoding of given data with a given key
#   Algorithm: (index(data) + index(key)) % 26
def VigenereEncode(data, key):
    global lower, upper
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
def VigenereDecode(data, key):
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

# Function gets the number of seconds from a date string ("YYYY MM DD HH mm ss")
def getSec(date_time):

    # Split string into list
    list_date  = date_time.split()

    # Convert date to number of seconds and convert back to date in local time
    time_sec  = time.mktime((int(list_date[0],10), int(list_date[1],10), int(list_date[2],10), int(list_date[3],10), int(list_date[4],10), int(list_date[5],10), 0, 0, 0))
    time_date = time.localtime(time_sec)

    # If date given is changed by daylight saving time, correct the change
    if time_date.tm_isdst:
        time_sec -= 3600*time_date.tm_isdst
    
    # Return the number of seconds
    return time_sec

# Function gets time difference, creates hash and forms code
def timelock(epoch_time, current_time, real_time = False):
    global VALID_TIME

    # Get 'current' time
    if real_time:
        current_time = time.time()
    else:
        current_time = getSec(TEST_TIME)
            
    # Calculate elapsed time and create string to the current minute in seconds
    elapsed = current_time - epoch_time
    elapsed_str = '{}'.format(int(elapsed - elapsed % VALID_TIME))

    # Create double hash of time found
    hash_str = hashlib.md5(hashlib.md5(elapsed_str).hexdigest()).hexdigest() 

    # Initialize Variables
    num_code = ""	 # Store the numeric characters of the code
    letter_code = "" # Store the alpha characters of the code

    # Search for the first two alpha characters of the hash and save them
    for i in range(0,len(hash_str)):
        # Save position
        last_pos = i
        # Check if alpha
        if (hash_str[i].isalpha()):
            letter_code += hash_str[i]
        # Check how many characters have been found
        if (len(letter_code) == 2):
            break
    
    # Reset counter
    i = 0

    # Search for numeric characters needed to fill code
    for i in range(len(hash_str)-1,0,i-1):
        # If not alpha, then numeric
        if (not hash_str[i].isalpha()):
            # Append current hash character 
            num_code += hash_str[i]
        # Check if the code can be filled
        if (len(num_code) + len(letter_code) == 4): 
            break

    # If the code can not be filled, resume alpha search and append to end of num_code until code can be filled
    if (len(num_code) + len(letter_code) != 4):
        # Reset counter
        i = 0
        for i in range(last_pos+1, len(hash_str)):
            if (hash_str[i].isalpha()):		   # Check if alpha
                num_code += hash_str[i]
            if (len(num_code) +len(letter_code) == 4): # Check if code can be filled
                break

    # Create code and display
    code = letter_code+num_code

    # Room for any additions (hash_str is hash)
    
    
    return code


### MAIN ###

