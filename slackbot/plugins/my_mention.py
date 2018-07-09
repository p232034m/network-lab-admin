from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
import subprocess
import datetime
import time

def check(message):
	all_ping_file = "./shell/all_ping.sh"
	result_txt ="./shellscript_result/result_ping_all.txt"
	subprocess.run(["bash",all_ping_file])
	
	result = open(result_txt,"r")
	contents = result.read()
	message.send(contents)
	result.close()	

@respond_to("cmd")	#cmd
def cmd_func(message):
	message.reply("check\t(全サーバーの動作確認)\nhost\t(指定したIPアドレスorホスト名ひも付け)\njpcert\t(jpcert注意喚起記事最新版入手)\nping\t(指定した計算機の動作確認)")

@respond_to("check")	#check
def all_ping_func(message):
	check(message)

@respond_to("check_start")	#check_start
def check_start(message):
	message.send("SEVER CHECK START")
	flag=0

	while True:
		dt = datetime.datetime.now()
		
		if str(dt.hour) == "10" and flag == 0:
			check(message)
			flag=1
			time.sleep(1)
		
		if str(dt.hour) == "11" and flag == 1:
			flag=0
			time.sleep(1)

		if str(dt.hour) == "12" and flag ==0:
			check(message)			
			flag=1
			time.sleep(1)

		time.sleep(0.1)
	
@respond_to(r'^ping.+') #ping
def ping_func(message):
	text = message.body["text"]
	temp, word = text.split(None,1)
	ping_file = "./shell/ping.sh"
	result_txt = "./shellscript_result/result_ping.txt"
	subprocess.run(["bash",ping_file,word])
	
	result = open(result_txt,"r")
	contents = result.read()
	message.reply(contents)
	result.close()	

@respond_to(r'^host.+')	#host
def dig_func(message):
	text= message.body["text"]
	temp, word = text.split(None,1)

	host_file = "./shell/host.sh"
	result_txt = "./shellscript_result/result_host.txt"
	subprocess.run(["bash",host_file,word])

	result = open(result_txt,"r")
	contents = result.read()
	temp = contents.split()
	message.reply(temp[-1])
	temp.clear()
	result.close()	

