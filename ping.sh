#!/usr/bin/env bash
var=1
#localtion=$HOME
#filename='ping2'
#echo $var
#echo $localtion
#echo $filename
#if [ -e $localtion/$filename ]
#then
#    echo "exit file"
#else
#    touch ping2
#fi


while [ $var -eq 1 ]
do

    date >> $1
    ping -c 4 $2 >> $1
    sleep 4s

done