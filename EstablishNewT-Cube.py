import os
import os.path
import shutil
import time,datetime
def copyFiles(sourceDir,  targetDir): 
    if sourceDir.find(".git") > 0: 
        return 
    for file in os.listdir(sourceDir): 
        sourceFile = os.path.join(sourceDir,  file) 
        targetFile = os.path.join(targetDir,  file) 
        if os.path.isfile(sourceFile): 
            if not os.path.exists(targetDir):  
                os.makedirs(targetDir)  
            if not os.path.exists(targetFile) or(os.path.exists(targetFile) and (os.path.getsize(targetFile) != os.path.getsize(sourceFile))):  
                open(targetFile, "wb").write(open(sourceFile, "rb").read()) 
        if os.path.isdir(sourceFile): 
            First_Directory = False 
            copyFiles(sourceFile, targetFile)

SrcFile = "E:\git-svn\chn-std-166\TPA"	
DesFile = "E:\PythonScripts\Test"		 
copyFiles(SrcFile,DesFile)