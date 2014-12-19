#!/usr/bin/env python	

import xml.dom.minidom as md

rx_tag_list = ['ToUserName', 'FromUserName', 'CreateTime', 'MsgType', 'Content', 'MsgId']
tx_tag_list = ['ToUserName', 'FromUserName', 'CreateTime', 'MsgType', 'Content', 'FuncFlag']

def proc_file(fn):
	fd = md.parse(fn)
	root = fd.documentElement

	for tag in rx_tag_list:
		node = root.getElementsByTagName(tag)
		print(tag +':'+ node[0].childNodes[0].nodeValue)

if __name__ == "__main__":
	file = "para.xml"
	proc_file(file)
