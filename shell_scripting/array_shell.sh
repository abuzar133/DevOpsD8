#!/bin/bash
#author: abuzar 
#This script is about arrays in shell scripting 

my_array=("Mohammed" "Abuzar" 100 102345 70.6)

echo "my first name is ${my_array[0]}"
echo "my last name is ${my_array[1]}"

num_1=${my_array[2]}
num_2=${my_array[3]}
num_3=$((num_1+num_2))

echo "Addition of $num_1 and $num_2 is $num_3"

echo "value at 5th index is ${my_array[5]}"

my_array[5]="Dracula"

echo "value at 5th index is ${my_array[5]}"
echo "value at 3rd index is ${my_array[2]}"

echo "${my_array[@]}"

