import shutil
import re

filePath = "apt_cmd_library.h"
TarPath = "functions.txt"
WrapperPath = "NativeWrapper.cs"
fp = open(filePath,"r")
TarFp = open(TarPath,"a+")
WrapperFp = open(WrapperPath,"w+")
reg = r'int fnAPT_DLL[\s\S]*?\);'
FuncRe = re.compile(reg)
FuncList = re.findall(FuncRe,fp.read())

for func in FuncList:
	print(func)
	#TarFp.write(func+"\n")
	WrapperFp.write("[DllImport(\"APT_CMD.dll\", CallingConvention = CallingConvention.Cdecl)]"+"\n"+"public static extern "+ func+"\n\n")
	

	
