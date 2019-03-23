#!/usr/bin/env python
# coding=utf-8
# code by cjj
# last modify time 2018.08.06
import werobot

robot = werobot.WeRoBot(token='nY0XCW4aXQDQkbMVVpI')
robot.config["APP_ID"] = 'wxd3b83c78a33b27f5'
robot.config['ENCODING_AES_KEY'] = 'nY0XCW4aXQDQkbMVVpIX7VS6m5ZsWPNLwF89yiryVQd'


import requests
import re
from bs4 import BeautifulSoup

cookie = dict(cook="username=01005527; password=111111a; rememberMe=1; last_url=%2Findex.php%3Fr%3DsmgwebNews%2Findex%26category_id%3D0; ser_last_url=%2Findex.php%3Fr%3DsmgwebNews%2Findex%26category_id%3D0; PHPSESSID=aoq30h768fqj1100ptusrhuo52; 22d8bff2c7f14696408f80fda66d89a5=615bc15e0a0c5a880cc78809753d7c3d54d27de2a%3A4%3A%7Bi%3A0%3Bs%3A8%3A%2201005527%22%3Bi%3A1%3Bs%3A8%3A%2201005527%22%3Bi%3A2%3Bi%3A2592000%3Bi%3A3%3Ba%3A1%3A%7Bs%3A8%3A%22userinfo%22%3BO%3A11%3A%22SmgUserReal%22%3A11%3A%7Bs%3A19%3A%22%00CActiveRecord%00_new%22%3Bb%3A0%3Bs%3A26%3A%22%00CActiveRecord%00_attributes%22%3Ba%3A21%3A%7Bs%3A9%3A%22loginname%22%3Bs%3A8%3A%2201005527%22%3Bs%3A8%3A%22password%22%3Bs%3A0%3A%22%22%3Bs%3A8%3A%22nickname%22%3Bs%3A9%3A%22%E9%99%88%E4%BF%8A%E6%9D%B0%22%3Bs%3A5%3A%22state%22%3Bs%3A1%3A%223%22%3Bs%3A6%3A%22mobile%22%3Bs%3A11%3A%2213817323253%22%3Bs%3A5%3A%22email%22%3Bs%3A4%3A%22NULL%22%3Bs%3A8%3A%22birthday%22%3Bs%3A10%3A%221988-01-03%22%3Bs%3A6%3A%22org_id%22%3Bs%3A12%3A%22011000000681%22%3Bs%3A6%3A%22gender%22%3Bs%3A3%3A%22%E7%94%B7%22%3Bs%3A10%3A%22createtime%22%3BN%3Bs%3A7%3A%22dept_id%22%3BN%3Bs%3A2%3A%22id%22%3Bs%3A4%3A%226196%22%3Bs%3A14%3A%22birthday_short%22%3Bs%3A5%3A%2201-03%22%3Bs%3A13%3A%22hide_birthday%22%3Bs%3A1%3A%220%22%3Bs%3A9%3A%22tel_phone%22%3Bs%3A8%3A%2222001151%22%3Bs%3A4%3A%22duty%22%3Bs%3A21%3A%22%E6%96%B0%E9%97%BB%E9%87%87%E8%AE%BF%E9%83%A8%E8%AE%B0%E8%80%85%22%3Bs%3A9%3A%22person_id%22%3Bs%3A18%3A%22310108198801030513%22%3Bs%3A11%3A%22first_login%22%3Bs%3A1%3A%221%22%3Bs%3A12%3A%22app_password%22%3Bs%3A32%3A%2249dec5fb8af4eeef7c95e7f5c66c8ae6%22%3Bs%3A10%3A%22app_mobile%22%3Bs%3A11%3A%2218621828022%22%3Bs%3A12%3A%22app_register%22%3Bs%3A1%3A%221%22%3B%7Ds%3A23%3A%22%00CActiveRecord%00_related%22%3Ba%3A0%3A%7B%7Ds%3A17%3A%22%00CActiveRecord%00_c%22%3BN%3Bs%3A18%3A%22%00CActiveRecord%00_pk%22%3Bs%3A4%3A%226196%22%3Bs%3A21%3A%22%00CActiveRecord%00_alias%22%3Bs%3A1%3A%22t%22%3Bs%3A15%3A%22%00CModel%00_errors%22%3Ba%3A0%3A%7B%7Ds%3A19%3A%22%00CModel%00_validators%22%3BN%3Bs%3A17%3A%22%00CModel%00_scenario%22%3Bs%3A6%3A%22update%22%3Bs%3A14%3A%22%00CComponent%00_e%22%3BN%3Bs%3A14%3A%22%00CComponent%00_m%22%3BN%3B%7D%7D%7D")
true = "true"
false = "false"

def judge(name):
	payload = {"page":"0","type":"1","key":name,"back":"1"}
	r = requests.post("http://fqapp.smg.cn:10000/index.php?r=smgUserReal/searchMore",data=payload,cookies=cookie)
	if r.text == true:
		get_data(name)

	return

#中文输出
def chin(word):
	s = str(word).replace('u\'','\'')
	return s.decode("unicode-escape")
		



def get_data(name):
	sname = name
	payload2 = {"search[extension]":'输入姓名',"search[short_phone]":name,"search[type]":"1"}
	r = requests.post("http://fqapp.smg.cn:10000/index.php?r=smgUserReal/search&type=0",data=payload2,cookies=cookie)
	r.encoding='utf-8'
	html_doc = r.text
	soup = BeautifulSoup(html_doc, "lxml")
	##获取姓名
	udata_name = str(soup.find_all("div",{'class':'search_result'}))
	#s = str(udata_name).replace('u\'','\'')
	#print s
	#print s.decode("unicode-escape")
	get_info = re.findall(r"(?<=span>).*?(?=</s)",udata_name)
	return get_info
	#st_name = chin(get_name[1])



@robot.text
def hello_world(message):
    return judge(message.content)

robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80

robot.run()

