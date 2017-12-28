#coding:utf-8

import requests
import random
import time
import datetime
import sys

compname=sys.argv[1]
employnum=sys.argv[2]
mobile=sys.argv[3]
fullname=sys.argv[4]

#公司到期日期为当前日期的一年后

expiretime =(datetime.datetime.now()+datetime.timedelta(days=365))
expiretimestamp = int(time.mktime(expiretime.timetuple()))*1000
#print expiretime,expiretimestamp

#公司员工数量Max
#employnum = random.randint(20,200)
#print employnum

#超管手机号随机获取
#mobile = random.choice(['9000000','8000000','7000000','6000000','5000000','4000000'])+"".join(random.choice("0123456789") for i in range(4))

#print mobile

#公司名称随机数
#compname = random.randint(1,100)
#print compname

def create_company():

    url=''  #创建公司的接口URL
    headers={
        'Content-type' : 'application/json',
        'Authorization' : ''
    }
    #post data数据
    data={
	    
	    "employeenum": employnum,
	    "mobile": mobile,
	    "fullname": fullname,
	    "Fullname": compname,
	    
	    "param":{
		    "expireTime":expiretimestamp

	    }
    }
    resp=requests.post(url,headers=headers,json=data)
    return resp

if create_company().status_code==200:
    print "创建公司成功！success"
else:
    print "error!"


if __name__ == '__main__':
    create_company()
