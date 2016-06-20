import os
import os.path
import shutil
import time,datetime
import string
import sys
from imp import reload
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
                content = open(sourceFile, "rb").read().decode('utf-8')
                open(targetFile, "wb").write(content.replace("TPA","TNA")) 
        if os.path.isdir(sourceFile): 
            First_Directory = False 
            copyFiles(sourceFile, targetFile)
imp.reload(sys) 
sys.setdefaultencoding('utf8') 			
SrcFile = "E:\git-svn\chn-std-166\TPA"	
DesFile = "E:\MyPythonScripts\Test"		 
copyFiles(SrcFile,DesFile)