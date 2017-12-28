# Manage

1、bsdiff+mput android差分包制作；

2、后台添加人员 执行脚本 
python admin_addp.py $mobile "$fullname" "$title" "$access_token"

3、创建公司 

if [ ${type} = "test" ];then
	python create_company_test.py "$compname" $employnum $mobile "$fullname"
elif [ ${type} = "online" ];then
	python create_company.py "$compname" $employnum $mobile "$fullname"
fi

4、上传文件至FTP指定目录


