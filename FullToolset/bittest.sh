#!/bin/bash

# Delete old folder if it exists and create new one
rm -rf stegtest
mkdir stegtest

# $i represents the interval
for i in {1..4}
do
	# $j represents the offset
	for j in {0..16}
	do
		Interval=$i
		# Set up the file name
		FileName="./stegtest/Bit$Interval"
		Temp="_o$j"
		FileName="$FileName$Temp"
		# echo so that we know the status
		echo $FileName
		# Run the program
		python steg.py -b -r -o$j -i$Interval -w$1 > $FileName
	done
done
