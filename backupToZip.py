#! python3
# backupToZip.py - 备份文件为ZIP格式
# 备份指定文件夹内容为文件名递增的zip文件

import zipfile,os

def backupToZip(folder):
    #将“文件夹”的全部内容备份到zip文件中

    folder = os.path.abspath('C:\\pythonS') #确保文件夹是绝对路径的
    #找出这段代码应该基于的文件名
    #哪些文件已经存在

    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    #创建zip文件
    print('创建 %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename,'w')
    #遍历整个文件夹树并压缩每个文件夹中的文件
    for foldername,subfolders,filenames in os.walk(folder):
        print('添加文件 %s...' % (foldername))
        #将当前文件夹添加到zip文件中
        backupZip.write(foldername)
    
        #将该文件夹中的所有文件添加到zip文件中
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue #不要备份备份的ZIP文件
            backupZip.write(os.path.join(foldername,filename))
    
    backupZip.close()

    print('Done')

backupToZip('C:\\pythonS')
