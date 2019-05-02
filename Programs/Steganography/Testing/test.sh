#!/bin/bash

# Remove old folder if it exists and create a new one
rm -rf stegtest
mkdir stegtest

##BYTES##

# $i represents the power of 2 interval
for i in {0..7}
do
	# $j represents the offset
	for j in {0..7}
	do
		# Power of 2 interval
		Interval=$((2**$i))
		# Get the filename
		FileName="./stegtest/Byte$Interval"
		Temp="_o$j"
		FileName="$FileName$Temp"
		# echo so that we know the status
		echo $FileName
		# Run the program
		python steg_Optimized.py -B -r -o$j -i$Interval -w$1 > $FileName
	done
done

##BITS##

# $i represents the power of 2 interval
for i in {0..3}
do
	# $j represents the offset
	for j in {0..16}
	do
		# Power of 2 interval
		Interval=$((2**$i))
		# Get the filename
		FileName="./stegtest/Bit$Interval"
		Temp="_o$j"
		FileName="$FileName$Temp"
		# echo so that we know the status
		echo $FileName
		# Run the program
		python steg_Optimized.py -b -r -o$j -i$Interval -w$1 > $FileName
	done
done
