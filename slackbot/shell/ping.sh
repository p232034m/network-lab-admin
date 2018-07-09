#!/bin/bash

str=$1

save_file=./shellscript_result/result_ping.txt
ping -q -c3 $str > /dev/null
 
if [ $? -eq 0 ]
then
    date > $save_file
    echo "working" >> $save_file
else
    date > $save_file
    echo "emergency! Not Working"  >> $save_file    
fi



#$?:直前に終了した命令が正常終了したかどうか評価
#正常終了時は０を返す
#-eq : equal
