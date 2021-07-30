import os 
import shutil
#os.system("date")
#os.mkdir("test")
os.getcwd()
#Specifying path
path = 'abc.txt'
#check wether the specified path exists or not
isExist = os.path.exists(path)
print(isExist)
#split the path in root and ext pair
root_ext = os.path.splitext(path)
#print root & ext of the specified path
print("Root part ", root_ext[0])
print("Ext part ", root_ext[1], "\n")
print(os.listdir())
path1 = "C:/Yerneni/Dheeru/whitehat/C99-PY"
#list file and directories. 
print("Before copying files ")
print(os.listdir(path1))
#source path
source = "abc.txt"
#destination path
destination = "test/abc.txt"
#copying the content of source to destination
dest = shutil.copy(source,destination)
#list files and directories
print("After copying files: ")
print(os.listdir(path1))
path2 = "C:/Yerneni/Dheeru/whitehat/C99-PY/videos"
#before moving files
print("Before moving file: ")
print(os.listdir(path2))
source1 = "C:/Yerneni/Dheeru/whitehat/C99-PY/videos/mp4"
destination1 = "C:/Yerneni/Dheeru/whitehat/C99-PY/videos/png"
dest1 = shutil.move(source1, destination1)
#after moving file
print("After moving file: ")
print(os.listdir(path2))
