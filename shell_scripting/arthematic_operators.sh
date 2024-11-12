#!/bin/bash
#AUthor : abuzar
#Arithmetic operators in linux
#
a=10
b=20

#ADDITION
val=`expr $a + $b`
echo "The sum of $a and $b is :$val"

#subtraction
val=`expr $a - $b`
echo "The differenece of $a and $b is: $val"

#Multiplication
val=`expr $a \* $b`
echo "The multiplication of $a and $b is: $val"

#Division
val=`expr $b / $a`
echo "The division of $b and $a is: $val"

#modulus
val=`expr $b % $a`
echo "The modulus of $b and $a is: $val"

#Equality operator and if..else..fii conditionals 

if [ $a == $b ]; then
	echo "$a is equal to $b"
else
	echo "$a is not equal to $b"
fi
