
import urllib.request

#请求
request = urllib.request.Request("http://www.baidu.com")
#爬取
response = urllib.request.urlopen(request)
#结果以及编码
data = response.read()

data = data.decode("utf-8")

#打印爬取数据
print(data)
#print(type(response))
#print(type(response.info()))
