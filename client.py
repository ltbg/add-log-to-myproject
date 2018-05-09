# --*-- coding=utf-8 --*--
# import urllib2
import urllib
import json
import sys
sys.stdout=open('client.log','a')
print "info..."
weatherHtml = urllib.urlopen('http://127.0.0.1:5000/todos/ip6')
#通过urllib模块中的urlopen的方法打开url
weatherHtml1 = weatherHtml.read()
#通过read方法获取返回数据
print (weatherHtml1)
#打印返回信息
weatherJSON = json.loads(weatherHtml1)
# #将返回的json格式的数据转化为python对象，json数据转化成了python中的字典，按照字典方法读取数据

print "python的字典数据：",weatherJSON
print "字典中的task数据",weatherJSON["task"]
x=weatherJSON["task"]
print(x)
