# client.py  
# coding=utf-8
import socket
def chin(word):
	s = str(word).replace('u\'','\'')
	return s.decode("unicode-escape")

def client(message):
	host = "159.203.251.224"                          

	port = 31504
	# create a socket object
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

	# get local machine name
	# while True:

	# 	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# try:
	# 	s.connect((ip, port))
	# # do something:send, recv
	# except socket.error, e:
	# 	print "get connect error as", e
		#continue

	try:
	# connection to hostname on the port.
		s.connect((host, port)) 
	except socket.error, e:
		print e
		return "无法连接"
	s.send(message)

	# Receive no more than 1024 bytes
	while 1:
		info  = s.recv(1024)
		if len(info) > 0:
			break                                     
	#print info
	s.close()
	return str(info)

def run(source,data):

        res = "由于台集团限制，暂时无法提供服务"
        if "cfb" in data:

                data = data.replace("cfb","")
                data = data.replace(" ","")
                sdata = str(data)
                print sdata
                res = client(sdata)
        return res





