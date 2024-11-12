#!/bin/bash
##author : abuzar
#This script explains about local vars
#global variables are accesed everywhere but where as locsl variable are accssedinside the function or after the calling the function 
#

getname(){
NAME="ABUZAR"   #LOCAL VARIABLE
echo "$NAME - from inside the function"
}

echo "$NAME - outside the function"
getname
echo "$NAME - outside the function after calling the function"

AGE=100   #GLOBAL VARIABLE

getage(){
echo "My age is :$AGE - Inside the function"
}

echo "my age is :$AGE - Outside the function"
getage
