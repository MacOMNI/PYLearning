import ssl
import urllib.request

#抓取知乎首页
header = {
 "user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Mobile Safari/537.36",
 "Referer":"http://www.zhihu.com/",
 "Host":"www.zhihu.com"

}

context = ssl._create_unverified_context()

homepageResponse = urllib.request.urlopen("https://www.zhihu.com/",context=context)

data = homepageResponse.read().decode("utf-8")

print(data)
# 登录知乎




