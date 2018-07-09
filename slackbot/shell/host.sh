#!/bin/bash

save_file=./shellscript_result/result_host.txt

host $1 > /dev/null

if [ $? -eq 0 ]
then
    host $1 > $save_file
else
    echo "undefined(><)" > $save_file
fi


#$?:直前に終了した命令が正常終了したかどうか評価
#正常終了時は０を返す
#-eq : equal
