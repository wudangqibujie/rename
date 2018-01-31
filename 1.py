import os
import os.path
curDir = r'C:\Users\liujie2\Desktop\龙腾\1A'
new = r'C:\Users\liujie2\Desktop\2A'
file_list = os.listdir(curDir)
for file_obj in file_list:
    print(file_obj)
    a = file_obj.split("-")
    
    os.rename(os.path.join(curDir,file_obj),os.path.join(new,'GC'+'-'+a[2]+'-'+a[3]+"("+a[4][:-4]+")"+'.dwg'))
    
