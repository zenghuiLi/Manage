#!/bin/sh
dir="/AndroidUpdate/差分包制作工具/bsdiff-4.3/" #bsdiff目录

cd $dir
echo $pwd

rm -rf ${dir}/*.apk
rm -rf ${dir}/*.txt


wget *.apk #获取旧目录下的apk路径
mv *.apk $old_dir.apk


wget *.apk  #获取新目录下的apk路径
mv *.apk oa.apk


./bsdiff $old_dir.apk oa.apk patch.apk
./bspatch $old_dir.apk new$new_dir.apk patch.apk

md5 oa.apk > 1md5.txt

md5 new$new_dir.apk > 2md5.txt

diff 1md5.txt  2md5.txt  -y  -W  500

sh ftp_mput.sh

ls
