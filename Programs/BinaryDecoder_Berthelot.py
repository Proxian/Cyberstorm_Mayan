#!/usr/bin/python

 ####################################################################
#                                                                   #
#   Authors: Justin Berthelot,                                      #
#   Github link: https://github.com/Proxian/Cyberstorm_Mayan/       #
#                                                                   #
#   Date: 03 / 21 / 19                                              #
#   Description: Translates 7-bit and 8-bit binary to ASCII         #
#                                                                   #
####################################################################

### LIBRARIES ###
from sys import stdout



### FUNCTIONS ###

# Determines the bit-type for binary input
def BinBitType(binary_message):
    # Get the size of the message
    size = len(binary_message)
    # Only use numeric values
    if binary_message.isdigit():
        # Type 1 - Either 7-bit or 8-bit
        if not ((size+7) % 7) and not ((size+8) % 8):
            return 1;
        # Type 2 - 7-bit
        elif not ((size+7) % 7):
            return 2;
        # Type 3 - 8-bit
        elif not ((size+8) % 8):
            return 3;
        # Unknown bit; treat as error
        else:
            print "Not a recoginizable binary number!"
            exit(1)
    # Non-number value; treat as error
    else:
        print "Not a numeric value!"
        exit(1)

# 8-bit binary conversion
def Bin8Bit(data):
    # Loops over the data in 8-bit increments
    for i in range(0,len(data),8):
        # prints the ASCII equivalent character
        stdout.write(chr(int(data[i:i+8], 2)))
        
# 7-bit binary conversion
def Bin7Bit(data):
    # Loops over the data in 7-bit increments
    for i in range(0,len(data),7):
        # prints the ASCII equivalent character
        stdout.write(chr(int(data[i:i+7], 2)))
        
# Either 7-bit or 8-bit binary
#  (prints both)
def BinNBit(data):
    
    Bin7Bit(data)
    # Add a newline for clean formatting
    stdout.write('\n')
    Bin8Bit(data)

# Handles user input and data direction
def Main():
    # Get user input
    binary_data = raw_input()
    # Determine binary bit-number
    bin_type = BinBitType(binary_data)

    # Either 7-bit or 8-bit binary
    #  (prints both)
    if bin_type == 1:
        BinNBit(binary_data)
        
    # 7-bit binary
    elif bin_type == 2:
        Bin7Bit(binary_data)

    # 8-bit binary
    else:
        Bin8Bit(binary_data)


### MAIN ###
Main()
