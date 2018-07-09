from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply

import requests
from bs4 import BeautifulSoup
import time

@respond_to("jpcert")
def jp_cert_func(message):
	URL = "https://www.jpcert.or.jp"	
	flag1=0
	flag2=0

	while True:	

		#html_get
		res = requests.get(URL)
		#error message
		res.raise_for_status()
		#create BeautifulSoup Object
		soup = BeautifulSoup(res.content, "html.parser")
		#class:contents_list_box_security_alerts以下の<a>タグをget
		elems1=soup.select(".contents_list_box_security_alerts a")
		
		if flag1 == 0:#初回
			old1 = elems1[0].get("href")
			flag = 1
		
		for tmp in elems1:
			if tmp.get("href") == old1:
				break
	
			elif tmp.get("href") != old1:
				message.send(URL + tmp.get("href"))

		old1 = elems1[0].get("href") 

		#class:contents_list_box_jvn以下の<a>タグをget
		elems2=soup.select(".contents_list_box_jvn a")
	
		if flag2 == 0:#初回
			old2 = elems2[1].get("href")
			flag2 = 1

		for tmp in elems2[1::]:
			if tmp.get("href") == old2:
				break
	
			elif tmp.get("href") != old2:
				message.send(tmp.get("href"))

		
		old2 = elems2[1].get("href")		
		
		time.sleep(86400)

