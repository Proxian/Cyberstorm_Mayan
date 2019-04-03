#####################################################################
# Name:    Dawson Markham
# Date:    3/24/2019
# Program: Vigenere Cipher
# Descritption: Program ecncrypts or decrypts user input using a 
#		vigenere cipher with a user specified key. Encryption/
#               Decryption mode set by user in the first argument.
#		i.e python2 VigenereCipher.py -e key
#		    OR
#		i.e python2 VigenereCipher.py -d key < input file
######################################################################
import sys

# Encryption Function
def encryption():
	# Infinite Loop
	while(1):
		# Take user input
		text = sys.stdin.readline().rstrip()
		
		# If input is empty, break 
		if (text == ""):
			break

		# Initialize varibales
		cipher = ""
		place = 0

		# Go through the input
		for i in range(0, len(text)):
			# Check if character is a letter
			if (text[i].isalpha()):
				# Add appropriate cipher character (case is kept)
				if (text[i].isupper()):
					cipher = cipher + chr(((ord(text[i]) - 65 + (ord(key[place].upper()) - 65)) % 26) + 65)
				elif (text[i].islower()):
					cipher = cipher + chr(((ord(text[i]) - 97 + (ord(key[place].lower()) - 97)) % 26) + 97)
				
				# Increment place counter
				place += 1
				# Place should always remain within the length of the key
				place = place % len(key)

			# If the character is not a letter, no change
			else:
				cipher = cipher + text[i]
		
		# Display cipher
		print cipher

# Decryption Function
def decryption():
	# Infinite Loop
	while(1):
		# Take user input
		cipher = sys.stdin.readline().rstrip()

		# If input is empty, break
		if (cipher == ""):
			break

		# Initialize variables
	        text = ""
        	place = 0

		# Go through input
        	for i in range(0, len(cipher)):
			# Check if character is a letter
	        	if (cipher[i].isalpha()):
				# Add appropriate plaintext character (case is kept)
				if (cipher[i].isupper()):
					text = text + chr(((26 + ord(cipher[i]) - 65 - (ord(key[place].upper()) - 65)) % 26) + 65)
                		elif (cipher[i].islower()):
                        		text = text + chr(((26 + ord(cipher[i]) - 97 - (ord(key[place].lower()) - 97)) % 26) + 97)
                		
				# Increment place counter
				place += 1
				# Place should always remain within the length of the key
                		place = place % len(key)
        		
			# If the character is not a letter, no change
			else:
                		text = text + cipher[i]
		
		# Display plaintext
		print text

#########
# MAIN
#########

# Take given arguments
mode = sys.argv[1]
key = sys.argv[2]

# If -e, run the encryption function
if (mode == '-e'):
	encryption()

# If -d, run the decryption function
if (mode == '-d'):
	decryption()
