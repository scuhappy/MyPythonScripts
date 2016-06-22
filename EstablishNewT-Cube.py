import os
import os.path
import shutil
import time,datetime
import string
import chardet

SourceDeviceName = "TPA"
TargetDeviceName = "TNA"
SrcFile = "E:\git-svn\chn-std-166\TPA"	
DesFile = "E:\MyPythonScripts\Test"		

def copyFiles(sourceDir,  targetDir): 
    if sourceDir.find(".git") > 0: 
        return 
    for file in os.listdir(sourceDir): 
        sourceFile = os.path.join(sourceDir,  file) 
        targetFile = os.path.join(targetDir,  file.replace("TPA","TNA")) 
        if os.path.isfile(sourceFile): 
            if not os.path.exists(targetDir):  
                os.makedirs(targetDir)  
            if not os.path.exists(targetFile) or(os.path.exists(targetFile) and (os.path.getsize(targetFile) != os.path.getsize(sourceFile))):
                if  ".h" in sourceFile or ".cpp" in sourceFile or ".pro" in sourceFile or ".ui" in sourceFile :
                    open(targetFile,"w").write(open(sourceFile, "r").read().replace(SourceDeviceName,TargetDeviceName)) 
                else:
                    open(targetFile,"wb").write(open(sourceFile, "rb").read())
        if os.path.isdir(sourceFile): 
            First_Directory = False 
            copyFiles(sourceFile, targetFile)		

copyFiles(SrcFile,DesFile)