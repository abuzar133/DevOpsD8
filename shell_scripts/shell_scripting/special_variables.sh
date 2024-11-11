#!/bin/bash
#Author : abuzar
#This script explains about special variables in shell 
#
echo "current file name is: $0"
echo "First argument passed to the script is: $1"
echo "Second argument passed to the script is: $2"
echo "All the argument combuined together: $*"
echo "All tghe arguments combined together: $@"
echo "Total number of arguments passed $#"
echo "exit status of the script: $?"

