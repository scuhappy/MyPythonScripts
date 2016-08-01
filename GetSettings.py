import re
src_file = "E:\MyPythonScripts\\test.txt"
handle = open(src_file,'r+')
src_content = handle.read();
str_reg = r'\s{1}(\S+?)\s{1}(\S+?);'
re_msg = re.compile(str_reg)
MSG_ARY =re.findall(re_msg,src_content)
add_content = ""
load_content = ""
for name in MSG_ARY:
	add_content+="\n	obj.insert(\""+name[1]+"\",m_Model->m_Setting."+name[1]+");"
	load_content+="\n    m_Model->m_Setting."+name[1]+"=obj.value(\""+name[1]+"\").to"+name[0]+"();"
print(load_content)
handle.write(load_content)
