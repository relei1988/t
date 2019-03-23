# -*- coding:utf-8 -*-
import json
import requests
#from werobot import client
file_path = 'data.json'
with open(file_path) as f:
    js = json.load(f)

ls = len(js)

#def get_group_by_id(source):

 #       res =  requests.post(
 #           url="https://api.weixin.qq.com/cgi-bin/groups/getid",
 #           data={"openid": source}
 #       )

  #      return res.text


def chin(word):
	s = str(word).replace('u\'','\'')
	return s.decode("unicode-escape")




def get_info(data):
	i = 0
	a = ""
	b = "查无此人/号"
	while i<ls:
		if data in js[i]["name"]  or js[i]["num"] == data:
			#b = ""
			a = a + chin(js[i])
			i = i+1
		else:
			i=i+1
	if len(a) < len(b):
		a = b
	return a

def run(source,data):
#	print source
#	print get_group_by_id(source)
	res = "由于台集团限制，暂时无法提供服务"
	if "cfb" in data:

		data = data.replace("cfb","")
		data = data.replace(" ","")
		res = get_info(data)
	f.close()
	return res
