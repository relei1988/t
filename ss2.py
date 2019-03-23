#!/usr/bin/env python
# coding=utf-8
# code by cjj
# last modify time 2018.08.06
import werobot
import getinfo
import read_json


robot = werobot.WeRoBot(token='nY0XCW4aXQDQkbMVVpI')
robot.config["APP_ID"] = 'wxd3b83c78a33b27f5'
robot.config['ENCODING_AES_KEY'] = 'nY0XCW4aXQDQkbMVVpIX7VS6m5ZsWPNLwF89yiryVQd'


@robot.text
def hello_world(message):
    return client.run(message.source,message.content)
    #return "不让用了"

robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 1080

robot.run()
