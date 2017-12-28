#coding:utf-8

import base64
import time
import hashlib
import types
import requests

class codeBase64(object):
    #global nowtime

    # 获取当前时间格式如201708081800
    now = int(time.time())  #这是时间戳
    # 转换为其他日期格式,如:"%Y%m%d%H%M%S"
    timeArray = time.localtime(now)
    nowtime = time.strftime("%Y%m%d%H%M%S", timeArray)
    print nowtime


    def encode(self,text="Num:%s" %nowtime):   #number

        try:
            #text = "N000000:20170808150000"
            print "----------------------"
            print "origin text:"
            #print text
            #开始编码
            base64_text=base64.encodestring(text)
            print "encoding:"
            print base64_text
            print "-----------编码成功-----------"

            #开始解码，与原始对比
            print "decode:"
            print base64.decodestring(base64_text)
            print "-----------解码成功------------"

        except Exception as e:
            print "encode error"

        return base64_text


    def md5Encode(self, str="%s" % nowtime): #str
        #print str
        if type(str) is types.StringType:
            m = hashlib.md5()  #创建md5对象
            m.update(str)       #生成加密串
            m5=m.hexdigest()   #获取加密串
            #print m5
            return m5
        else:
            return "md5 error!"




    def getcustomer(self):


        url='?sig=%s' %sig #url
        print url
        headers={

            'Content-Type':    'application/json;charset=UTF-8',
            'Authorization': '%s'%auth,
            'Accept':'application/json'
        }
        print headers
        data={
            "version":"201704180000"
        }
        getcustomer=requests.post(url,headers=headers,json=data)
        print (getcustomer)
        return

    def getchat(self):


        url='?sig=%s' %sig #url
        print url
        headers={

            'Content-Type':    'application/json;charset=UTF-8',
            'Authorization': '%s'%auth,
            'Accept':'application/json'
        }
        print headers

        getchat=requests.post(url,headers=headers)
        print (getchat)
        return




if __name__ == '__main__':

    #nowtime=codeBase64.nowtime
    code=codeBase64()
    auth2 = code.encode()
    auth=auth2.strip("\r\n")
    print "auth:"
    print auth
    sig=code.md5Encode().upper()
    print "sig:"
    print sig

    print code.getcustomer()
    print code.getchat()

