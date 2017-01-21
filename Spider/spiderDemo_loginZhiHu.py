# -*- coding: utf-8 -*-

import ssl
import re
import time
import urllib.request
import http.cookiejar as cookielib
from PIL import  Image
from urllib.parse import urlencode
#抓取知乎首页
header = {
 "user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Mobile Safari/537.36",
 # "Referer":"http://www.zhihu.com/",
 # "Host":"www.zhihu.com"

}
context = ssl._create_unverified_context()

# 登录知乎
## 登录cookie信息

cookies = cookielib.CookieJar()
handler =  urllib.request.HTTPCookieProcessor(cookiejar=cookies)
opener  = urllib.request.build_opener(handler)
opener.addheaders = header
try:
 cookies.load(ignore_discard=True)
except:
 print('cookie 加载失败')
## 获取XSRF (CSRF Cross-site request forgery)跨站请求伪造
def get_xsrf():

 homepageResponse = urllib.request.urlopen("https://www.zhihu.com/", context=context)
 data = homepageResponse.read().decode("utf-8")
 pattern = r'name="_xsrf" value="(.*?)"'
 # arrayList
 _xsrf = re.findall(pattern,data)
 return _xsrf[0]
## 获取验证码
def get_captcha():
 t = str(int(time.time()*1000))
 captcha_url = 'http://www.zhihu.com/captcha.gif?r='+ t + '&type=login'
 homepageResponse = urllib.request.urlopen(captcha_url, context=context)

 with open('captcha.jpg','wb') as f:
  f.write(homepageResponse.read())
  f.close()

 #弹出验证码
 im = Image.open('captcha.jpg')
 im.show()
 im.close()

 captcha = input("please input the captcha\n>")

 return captcha

## 登录
def login(username,password):
 #username = '414294494@qq.com'
 #password = 'azheng51714'
 post_url = 'https://www.zhihu.com/login/email'
 post_data = {
  '_xsrf' : get_xsrf(),
  'password' : password,
  'remeber_me' : 'true',
  'email' : username,
  'captcha' : get_captcha()
 }
 try:
  req = urllib.request.urlopen(post_url,urlencode(post_data).encode(),context=context)
  print(req.read().decode('utf-8'))
 except:
  print("登录失败")

 return

if __name__ == '__main__':
   login('414294494@qq.com','azheng51714')
