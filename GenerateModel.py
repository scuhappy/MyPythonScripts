import os
import os.path
import shutil
import re

file_path = "Model.txt"
Tar_Path = "model_func.txt"

fp = open(file_path,"r+")
TarFp = open(Tar_Path,"a+")
reg = r'\s(.+)?m_(.+)?;'
newreg = r'MPROPERTY\((.+),[\s*]?(.+)?\)'
NameReg = re.compile(newreg)

FuncList = re.findall(NameReg,fp.read())
for func in FuncList:
	str =  "public void set_"+func[1]+"("+func[0]+" value)\n\
        {\n\
            m_"+func[1]+" = value;\n\
        }\n\
		public "+func[0]+" get_"+func[1]+"()\n\
		{\n\
		return m_"+func[1]+";\n\
		}\n"
	print(str)
	TarFp.write(str)
for func in FuncList:
	members = func[0]+" m_"+func[1]+";\n"
	print(members)
	TarFp.write(members)

       