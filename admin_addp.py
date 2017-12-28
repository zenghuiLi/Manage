# -*- coding: UTF-8 -*-
import requests
import sys
import json
import time

mobile=sys.argv[1]
fullname=sys.argv[2]
title=sys.argv[3]
access_token=sys.argv[4]

jobat = time.strftime("%Y-%m-%d",time.localtime())
nowtime = int(time.time())*1000
#print jobat
#print nowtime

'''

str = []
mob_name = open("mob_name.txt", 'r')
lines=mob_name.readlines()
list1 = []

for line in lines:
	temp = line.replace('', '').split(',')
	list1.append(temp)


for data in range(len(list1)):
	v = data % 3
	if v == 0:
		a = list1[data][0]
	elif v == 1:
		b = list1[data][0]
	elif v == 2:
		c = list1[data][0]
print list1
print a,b,c
'''

def admin_add_peo():
	url = '' #接口url

	headers = {
    	'Accept-Encoding': 'gzip, deflate',
   		'Accept' :	'application/json, text/plain, */*',
    	'Content-Type':	'application/json;charset=UTF-8',
    	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
    	'Authorization': 'Bearer '+access_token
	}
	#post data数据
	data = {
		
		"contractVos": [{
			"startDate": nowtime,
			"attachments": []
		}],
		"loginAccount": mobile,
		"mobile": mobile,
		"fullname": fullname,
		"jobTitle": title,
		"joinedAt": jobat
	}

	#print data
	return requests.request("POST", url, headers=headers, json=data).json()


if __name__ == '__main__':
	admin_add_peo()

