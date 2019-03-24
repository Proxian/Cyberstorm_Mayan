######################################################################
# Name:    Dawson Markham
# Date:    3/24/2019
# Program: Binary Decoder
# Descritption: Program takes 7-bit and 8-bit binary input and decodes
#		into ANSCII characters.
######################################################################
import sys

# 7-Bit Decoder
def Bit_7():
	# Set an empty string
	decoded = ""
	
	# Go through input in groups of seven characters, convert to appropiate character and add to string
	for i in range(0, len(binary), 7):
		temp =  binary[i:i+7]
		decoded = decoded + chr(int(temp, base=2))

	# Display decoded string
	print decoded

# 8-Bit Decoder
def Bit_8():
	# set an empty string
	decoded = ""    

	# Go through input in groups of 8 characters, convert to appropriate character and add to string
	for i in range(0, len(binary), 8):
		temp =  binary[i:i+8]
		decoded = decoded + chr(int(temp, base=2))

	# Display decoded string
        print decoded

########
# MAIN
########

# Take user input
binary = sys.stdin.read().rstrip()

# Check if 7-Bit Decoder can be used
if ((len(binary) % 7) == 0 ):
	Bit_7()

# Check if 8-Bit Decoder can be used
if ((len(binary) % 8) == 0 ):
	Bit_8()
