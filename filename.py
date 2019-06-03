from os import listdir
from os.path import isfile, isdir, join
from os import walk

mypath = "E:\DOWNLOAD"

# 取得所有檔案與子目錄名稱
files = listdir(mypath)
'''
# 以迴圈處理
for f in files:
  # 產生檔案的絕對路徑
  fullpath = join(mypath, f)
  # 判斷 fullpath 是檔案還是目錄
  if isfile(fullpath):
    print("檔案：", f)
  elif isdir(fullpath):
    print("目錄：", f)
'''
for root, dirs, files in walk(mypath):
  print("路徑：", root)
  print("  目錄：", dirs)
  print("  檔案：", files)
