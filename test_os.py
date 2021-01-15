import os
import time
#os.system("omxplayer /home/pi/Videos/result.wav")
#os.system("pwd")
#print(os.system("ls"))
file_data=os.stat("/home/pi/Videos/result.wav")
print(file_data) #st_ino索引号 st_dev设备号 st_nlink st_uid所有者的用户id st_gid所有者的组id st_size文件大小（单位：字节） st_atime最后一次访问时间 st_mtime最后一次修改时间 st_ctime最后一次状态变化时间
print(file_data.st_mtime)
print(time.localtime())#获取当前时间
print(time.localtime(file_data.st_mtime))#文件最后一次修改时间
filetime_format=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(file_data.st_mtime))#时间格式化
print(filetime_format)