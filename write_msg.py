import re

src_file = "E:\\test_MSG.txt"
des_file = "E:\outputMSG.txt"
file_handle_src = open(src_file,'r+')
file_handle_des = open(des_file,'w+')
src_content = file_handle_src.read()


#OLD REG: Generic::(.*?)\([^}]+?b\[0\][ ]*?=[ ]*?(?:\(char\))*?0x(.+?);b\[1\]=0x(.+?);
str_reg_msg = r'(MGMSG_.*?GET.*?) (.*?) '
re_msg = re.compile(str_reg_msg)
MSG_ARY =re.findall(re_msg,src_content)
add_content = ""
for name in MSG_ARY:
	add_content+="\n	APT_"+name[0]+" = "+name[1]+","
print(add_content)
file_handle_des.write(add_content)