import shutil

# copy include files
IncludeSrcPath = "E:\git-svn\chn-std-166\APT_COMMAND_LIB\src\\"
IncludeDesPath = "E:/Qt/5.2.1_vs2010_opengl/5.2.1/msvc2010_opengl/include/APT_CMD_Library\\"

shutil.copy(IncludeSrcPath+'apt_cmd_library.h',IncludeDesPath+'apt_cmd_library.h');
shutil.copy(IncludeSrcPath+'apt_type.h',IncludeDesPath+'apt_type.h');
shutil.copy(IncludeSrcPath+'kcube_type.h',IncludeDesPath+'kcube_type.h');
shutil.copy(IncludeSrcPath+'tcube_type.h',IncludeDesPath+'tcube_type.h');


#copy lib files
LibSrcPath = 'E:\git-svn\chn-std-166\APT_COMMAND_LIB\APT_CMD_TEST\\bin\\'
libDesPath = 'E:/Qt/5.2.1_vs2010_opengl/5.2.1/msvc2010_opengl/lib\\'

shutil.copy(LibSrcPath+'APT_CMD.lib',libDesPath+'APT_CMD.lib');
shutil.copy(LibSrcPath+'APT_CMDd.lib',libDesPath+'APT_CMDd.lib');

#copy bin files
BinSrcPath = 'E:\git-svn\chn-std-166\APT_COMMAND_LIB\APT_CMD_TEST\\bin\\'
BinDesPath = 'E:/Qt/5.2.1_vs2010_opengl/5.2.1/msvc2010_opengl/bin\\'
shutil.copy(BinSrcPath+'APT_CMD.dll',BinDesPath+'APT_CMD.dll');
shutil.copy(BinSrcPath+'APT_CMDd.dll',BinDesPath+'APT_CMDd.dll');



