#!/bin/sh
date='date +%Y%m%d %H:%M'
ftp -v -n  <<EOF  #FTP地址

#用户名 密码
user oaapp oaapp
binary


prompt off

cd /$new_dir

lcd   #本地目录

mget *.ipa

cd /    #FTP目录
delete *.ipa

lcd / #切换至本地目录
mput *.ipa


close

quit
EOF
