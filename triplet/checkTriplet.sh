#!/bin/bash

arg1=`echo "$1" |cut -d , -f 1`
arg2=`echo "$1" |cut -d , -f 2`
arg3=`echo "$1" |cut -d , -f 3`
#echo "arg1 = " $arg1
#echo "arg2 = " $arg2
#echo "arg3 = " $arg3
python main_math.py "$arg1" "$arg2" "$arg3"