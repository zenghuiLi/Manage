#coding:utf-8
import MySQLdb
from sshtunnel import SSHTunnelForwarder

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#import sys
#import qtgui tkinter
#使用前先替换mobile为新手机号
def getuserid():
    name=sys.argv[1]
    global fzrid
    server = SSHTunnelForwarder(
            ('jumpserver', port),  # jumpserver机器的配置
            ssh_password='pwd',
            ssh_username='username',
            remote_bind_address=('ip', mysql_port), #mysql配置
            local_bind_address=('local_ip', local_port),  # 本地绑定的端口
        )
    server.start()

    conn = MySQLdb.connect(host='127.0.0.1',  # 此处必须是是127.0.0.1
                       port=local_ip,
                       user='user', #mysqluser
                       passwd='pwd', #mysqlpwd
                       db='dbname',  #mysqldbname
                       charset='utf8')


    cursor=conn.cursor()

    sql = "select * from table  where name= %s " % ( name )
    cursor.execute(sql)
    res=cursor.fetchall()
    #for r in res:

    #    print r
    #print server.local_bind_address
    print res
    userid=list(res)
    t=res.__str__()
    print t
    print userid
    
def getmobile():
    global fzrid
    #m=sys.argv[0]
    server = SSHTunnelForwarder(
            ('jumpserver', ),  # jumpserver机器的配置
            ssh_password='',
            ssh_username='',
            remote_bind_address=('', ),
            local_bind_address=('127.0.0.1', ),  # 本地绑定的端口
        )
    server.start()

    conn = MySQLdb.connect(host='127.0.0.1',  # 此处必须是是127.0.0.1
                       port=,
                       user='',
                       passwd='',
                       db='')


    cursor=conn.cursor()

    sql2=""
    cursor.execute(sql2)
    people=cursor.fetchall()
    print people
    return people

    server.stop()



if __name__ == '__main__':
    getuserid()
    getmobile()




