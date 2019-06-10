from os import listdir
from os.path import isfile, isdir, join
from os import walk
import urllib
import re

#https://www.caribbeancompr.com/moviepages/053119_003/images/l_l.jpg
imgurl1='https://www.caribbeancompr.com/moviepages/'
imgurl2='053119_003'
imgurl3='/images/l_l.jpg'
urllib.request.urlretrieve(imgurl1+imgurl2+imgurl3,'1.jpg')
#print(imgurl1+imgurl2+imgurl3)



'''
mypath = "E:\DOWNLOAD"

# 取得所有檔案與子目錄名稱
files = listdir(mypath)

# 以迴圈處理
for f in files:
  # 產生檔案的絕對路徑
  fullpath = join(mypath, f)
  # 判斷 fullpath 是檔案還是目錄
  if isfile(fullpath):
    print("檔案：", f)
  elif isdir(fullpath):
    print("目錄：", f)

os module中的rename()可以幫助我們修改檔案或是資料夾的檔名，
以下是一個簡單的範例簡介如何使用os.rename來更改檔名。
範例中把path底下的所有檔案從0開始依序編號更改檔名。
此範例使用os.listdir()來列出目錄下的所有檔案名稱，以及使用os.path.join()來產生路徑。

os.rename(sourece, dest) - 更改資料夾或檔案的名稱(從source改成dest)
os.listdir(dir_path) - 回傳一個list包涵dir_path資料夾中的所有檔案名稱
def batch_rename(path):
    count = 0
    for fname in os.listdir(path):
        new_fname = str(count)
        print os.path.join(path, fname)
        os.rename(os.path.join(path, fname), os.path.join(path, new_fname))
        count = count + 1   

for root, dirs, files in walk(mypath):
  print("路徑：", root)
  print("  目錄：", dirs)
  print("  檔案：", files)
'''
