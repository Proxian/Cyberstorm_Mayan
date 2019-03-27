import sys

def enCode(key, plainText):
	keyPos = 0
	cypherText = ""
	if (debug):
		print("key: " + str(key))
	for i in range(len(plainText)):
		if (not plainText[i].isalpha()):
			cypherText += plainText[i]
		else:
			if(plainText[i].islower()):
				toZeroP = a
				l = True
			else:
				toZeroP = A
				l = False
			toZeroK = [A, a][key[keyPos%len(key)].islower()]
			if (debug):
				print("chart[",ord(key[keyPos%len(key)]) - toZeroK,"][",ord(plainText[i]) - toZeroP,"]")
			#convert key and text characters to indecies for chart matrix
			c = chart[ord(key[keyPos%len(key)]) - toZeroK][ord(plainText[i]) - toZeroP]
			#append with respect to original case
			cypherText += [c,c.lower()][l]
			keyPos += 1
	return cypherText

def deCode(key, cypherText):
	keyPos = 0
	plainText = ""
	if (debug):
		print("key: " + str(key))
	for i in range(len(cypherText)):
		if (not cypherText[i].isalpha()):
			plainText += cypherText[i]
		else:
			if(cypherText[i].islower()):
				toZeroP = a
				l = True
			else:
				toZeroP = A
				l = False
			toZeroK = [A, a][key[keyPos%len(key)].islower()]
			#convert key to index and search for cypher character; return index & add to 'A'
			c = chr(A+chart[ord(key[keyPos%len(key)]) - toZeroK].index(cypherText[i].upper()))
			#append with respect to original case
			plainText += [c,c.lower()][l]
			keyPos += 1
	return plainText


#Build lookup table in terms of char 'A'
A = ord('A')
a = ord('a')
chart = [[chr(A + (i+j)%26) for j in range(26)] for i in range(26)]

debug = False

#Start of the Code
#check for correct number of arguments
if (len(sys.argv) == 3):
	op = sys.argv[1]
	key = sys.argv[2]
	#remove spaces in key for easier index incrementation 
	key = [key, key.replace(" ","")][key.find(" ") != -1]
else:
	sys.exit("invalid arguments. Try -e or -d followed by a \"key\".")

#check for valid option
if (op == "-e"):
	while(1):
		plainText = str(input())
		print(enCode(key, plainText))
elif (op == "-d"):
	while(1):
		cypherText = str(input())
		print(deCode(key, cypherText))
else:
	sys.exit("Invalid option. -e for encryption, -d for decryption.")
	