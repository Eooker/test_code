import re
import json
import urllib
import urllib.request
#import urllib2
# 
# kk='{"corpus_no":"6917789402638143506","err_msg":"success.","err_no":0,"result":["我和我的祖国一刻也不能分割。"],"sn":"422374002361610673359"}'
# print(type(kk))
# aa=json.loads(kk)
# print(type(aa))
# print(aa)
# print(aa['err_msg'])
# if aa['err_msg'] == 'success.':
#     print('y')
#     print(aa['result'][0])
#     print(type(aa['result']))
# else:
#     print('n')

# ff=open('./ak.txt','r')
# print(ff.read())
# bb=ff.read()
# print(bb)
# print(type(bb))

#url="http://api.qingyunke.com/api.php?key=free&appid=0&msg=你好"
#kok=urllib.request.urlopen(url)
#kok=urllib.request.urlopen("http://www.baidu.com")
#text="你叫什么"
text=open('./result.txt','r')
text=text.read()
text=urllib.parse.quote(text)
url="http://api.qingyunke.com/api.php?key=free&appid=0&msg=%s"%(text)
kok=urllib.request.urlopen(url)
#kok=urllib.request.urlopen("http://api.qingyunke.com/api.php?key=free&appid=0&msg=你好")
#print(str(kok.read(),'utf-8'))
nn=kok.read()
print(nn)
bb=str(nn,'utf-8')
print(type(bb))
print(bb)
aa=json.loads(bb)
print("aa--------------------------------")
print(aa)
print(type(aa))
print(aa['content'])