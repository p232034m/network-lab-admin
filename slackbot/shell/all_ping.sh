#!/bin/bash

#管理したいサーバ名
server_names=(fs franc dollar yuan visa rufiya1 btc rufiya2 monitor)

save_file=./shellscript_result/result_ping_all.txt
flag=0

date > $save_file

#動作確認
for server in ${server_names[@]}
do
	ping $server -q -c2 > /dev/null 
	if [ $? -eq 1 ];
	then
		flag=1
		echo "$server not working" >> $save_file
	fi
done

#正常動作時
if [ $flag -eq 0 ]; 
then
	echo "ALL_SERVER WORKING!!" >> $save_file
fi
