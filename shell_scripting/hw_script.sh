#!/bin/bash
#author: abuzar
#This script is about arrays in shell scripting
#1. Create an array of different data types
#2. Change existing the value at 2nd index to something else
#3. Print all the values of an array together in a single usimg speciail variable
#
myarray=("khan" "mohammed" 200 15000 7.14 "none")


myarray[2]="abuzar"

echo "my modified array is ${myarray[2]}"


echo "${myarray[@]}"











