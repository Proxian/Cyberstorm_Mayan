#!/bin/bash


# Remove old folder and create new folder for output files
rm -rf stegtest
mkdir stegtest

# Use $i for interval
for i in {1..8}
do
	# Use $j for offset
	for j in {0..8}
	do
		# interval
		Interval=$i
		# Filename
		FileName="./stegtest/Byte$Interval"
		Temp="_o$j"
		FileName="$FileName$Temp"
		# echo so we know status
		echo $FileName
		# Run the Steg Program
		python steg_Optimized.py -B -r -o$j -i$Interval -w$1 > $FileName
	done
done
