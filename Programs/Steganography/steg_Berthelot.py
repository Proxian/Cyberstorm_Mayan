 ############################################################################
#                                                                           #
#  Team:  Mayans                                                            #
#  Names: Dawson Markham, Justin Bethelot, Emily Rumfola                    #
#  Date:  5/3/2019                                                          #
#                                                                           #
#  Description: Program takes user input and can hide a file or extract a   #
# 		 file using either bit or byte steganography.               #
############################################################################

###LIBRARIES###
import sys

###VARIABLES###
SENTINEL = [0x0, 0xff, 0x0, 0x0, 0xff, 0x0]
DEBUG = False
BIT_METHOD = False
BYTE_METHOD = False
EXTRACT = False

offset = 0
interval = 1
WRAPPER = []
HIDDEN = []

###FUNCTIONS###

# Bit Method
def bitMethod():
    global EXTRACT, offset, WRAPPER, HIDDEN, interval
    # Check extraction mode
    if EXTRACT:

        # Set counters and buffer
        i = offset
        j = k = m = 0
        out_buffer = [0,0,0,0,0,0]

        # Extract the last bit from every byte as specified by variables
        while (i < len(WRAPPER)):
            tmp = 0x0		# Set counter and tmp variable
            k = 0
            for k in range(0,8):
                if (i >= len(WRAPPER)):
                    break
                tmp |= ((ord(WRAPPER[i]) & 0b00000001) << (7-k)) # Add bit to correct location
                i += interval
            
            # Check if enough cycles have been completed to fill the buffer
            if (i > offset + 6*(8*interval)):
                sys.stdout.write(chr(out_buffer[m]))

            # Store in buffer
            out_buffer[m] = tmp

            # DETECT SENTINEL
            if (out_buffer[m] == SENTINEL[j]): # Check if correct sentinel byte has been detected
                j+=1
                if DEBUG:
                    print "here"
                if (j == 6):		   # Break if sentinel has been found
                    break
            else:				   # Else, reset search	
                if DEBUG:
                    if (j>0):
                       print "reset"
                j=0
            
            # Update buffer variables
            m += 1
            m %= 6

    # Hide file
    else:

        # Add sentinel to end of hidden file list
        i = 0
        for i in range(0, len(SENTINEL)):
            HIDDEN.append(SENTINEL[i])
        
        # Set counters
        i = offset
        j = 0
        for j in range(0, len(HIDDEN)):
            # Get each bit of hidden byte and store in the ends of bytes in the wrapper
            k = 0
            for k in range(0, 8):
                tmp = ord(WRAPPER[i]) & 11111110			
                WRAPPER[i] = chr(tmp | ((HIDDEN[j] & 10000000) >> 7))
                HIDDEN[j] <<= 1
                i += interval
        
        # Output edited file
        i = 0
        for i in range(0, len(WRAPPER)):
            sys.stdout.write(WRAPPER[i])

# Byte Method
def byteMethod():
    global EXTRACT, offset, WRAPPER, HIDDEN, interval
    # Check extraction mode
    if EXTRACT:

        # Set counters and buffer
        i = j = m = 0
        out_buffer = [0,0,0,0,0,0]

        # Find and output the hidden bytes as specified by variables
        for i in range(offset,len(WRAPPER), i + interval):
            if (i >= offset + 6*interval):		# Check if buffer has been filled
                sys.stdout.write(out_buffer[m])
            
            out_buffer[m] = WRAPPER[i] 	# Buffer to prevent sending sentinel bytes

            # SENTINEL DETECTION
            if (ord(out_buffer[m]) == SENTINEL[j]): # Check if next sentinel byte has been sent
                j+=1
                if DEBUG:
                    print "here"
                if (j == 6):		# Break if entire sentinel has been sent
                    break
            else:				# Else, reseet search
                if DEBUG:
                    if (j>0):
                        print "reset"
                j=0

            # Update buffer variables
            m += 1
            m %=6

    # Else, hide file
    else:

        # Store the bytes of hidden file within wrapper
        i = 0
        o = offset
        for i in range(0, len(HIDDEN)):
            WRAPPER[o] = HIDDEN[i]
            o += interval

        # Store sentinel after hidden file
        i = 0
        for i in range(0, len(SENTINEL)):
            WRAPPER[o] = chr(SENTINEL[i])
            o += interval
        
        # Output new file
        i = 0
        for i in range(0, len(WRAPPER)):
            sys.stdout.write(WRAPPER[i])

def ShowHelpScreen():
    print "Usage: 'python steg.py -(bB) -(sr) -o<val> [-i<val>] -w<val> [-h<val>]'"
    print ""
    print " "*3 + "-b\tUse the bit method"
    print " "*3 + "-B\tUse the byte method"
    print " "*3 + "-s\tStore (and hide) data"
    print " "*3 + "-r\tRetrieve hidden data"
    print " "*3 + "-o<val>\tSet offset to <val>"
    print " "*3 + "-i<val>\tSet interval to <val>"
    print " "*3 + "-w<val>\tSet wrapper file to <val>"
    print " "*3 + "-h<val>\tSet hidden file to <val>"

# Get the arguments that are 
def GetUserInput():
    global BYTE_METHOD, BIT_METHOD, EXTRACT, offset, WRAPPER, HIDDEN, interval
    if (len(sys.argv) >= 5):
        for arg in sys.argv:
            if "-b" in arg[0:2]:
                if not BYTE_METHOD:
                    BIT_METHOD = True
            elif "-B" in arg[0:2]:
                if not BIT_METHOD:
                    BYTE_METHOD = True
            elif "-s" in arg[0:2]:
                    EXTRACT = False
            elif "-r" in arg[0:2]:
                    EXTRACT = True
            elif "-o" in arg[0:2]:
                if arg[2:].isdigit():
                    offset = int(arg[2:])
            elif "-i" in arg[0:2]:
                if arg[2:].isdigit():
                    interval = int(arg[2:])
            elif "-w" in arg[0:2]:
                try:
                    wrap_file = open(arg[2:], 'r')
                    while True:
                        tmp = wrap_file.read(1)
                        if not tmp:
                            break
                        WRAPPER.append(tmp)
                except:
                    print "Wrapper file does not exist!"
                    exit(1)
            elif "-h" in arg[0:2]:
                if BYTE_METHOD:
                    try:
                        hidden_file = open(arg[2:], 'r')
                        while True:
                            tmp = hidden_file.read(1)
                            if not tmp:
                                break
                            HIDDEN.append(tmp)
                    except:
                        print "Hidden file does not exist!"
                        exit(1)
                else:
                    try:
                        hidden_file = open(arg[2:], 'r')
                        while True:
                            tmp = hidden_file.read(1)
                            if not tmp:
                                break
                            HIDDEN.append(ord(tmp))
                    except:
                        print "Hidden file does not exist!"
                        exit(1)
        if BYTE_METHOD:
            byteMethod()
        elif BIT_METHOD:
            bitMethod()
        else:
            pass
    else:
        ShowHelpScreen()



###MAIN###
GetUserInput()
