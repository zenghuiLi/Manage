#!/bin/sh
date='date +%Y%m%d %H:%M'
ftp -v -n 1.1.1.1  <<EOF  #ftpIP

user test test #账号密码
binary

prompt off

cd /$new_dir
lcd $dir

put ${date}.log

mput oa.apk
mput patch.apk

close

quit
EOF
