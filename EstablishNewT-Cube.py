import os
import os.path
import shutil
import time,datetime
import string
import chardet

SourceDeviceName = "TNA"
TargetDeviceName = "TDC001"
SrcFile = "E:\git-svn\chn-std-166\TNA\Thorlabs.WPF.TNA"	
DesFile = "E:\MyPythonScripts\Thorlabs.WPF.TDC001"		
filetypes = [".h",".cpp",".pro",".ui",".vcproj",".cs",".sln"]
def copyFiles(sourceDir,  targetDir): 
    if sourceDir.find(".git") > 0: 
        return 
    for file in os.listdir(sourceDir): 
        sourceFile = os.path.join(sourceDir,  file) 
        targetFile = os.path.join(targetDir,  file.replace(SourceDeviceName,TargetDeviceName)) 
        if os.path.isfile(sourceFile): 
            if not os.path.exists(targetDir):  
                os.makedirs(targetDir)  
            if not os.path.exists(targetFile) or(os.path.exists(targetFile) and (os.path.getsize(targetFile) != os.path.getsize(sourceFile))):
                flag = 0
                for type  in filetypes:
                    if type in sourceFile:
                        result = chardet.detect(open(sourceFile, "rb").readline())
                        print("file name :"+sourceFile)
                        print(result)
                        data = open(sourceFile, "r",encoding=result["encoding"]).read().replace(SourceDeviceName,TargetDeviceName)
                        open(targetFile,"w",encoding=result["encoding"]).write(data) 
                        flag = 1
                if 0 ==flag:
                    open(targetFile,"wb").write(open(sourceFile, "rb").read())
        if os.path.isdir(sourceFile): 
            First_Directory = False 
            copyFiles(sourceFile, targetFile)		

copyFiles(SrcFile,DesFile)