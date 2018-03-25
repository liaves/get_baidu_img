#_*_ coding:utf-8*_
from selenium import webdriver
import urllib,re
import time
import urllib2
import sys
import os
import socket
import threading
socket.setdefaulttimeout(15.0)#全局等待是为15秒时间
def mkdir(name):#创建文件夹
    if not os.path.exists(name):
        os.mkdir(name)
def get_html(name,papg):#访问目标网址获取html
        try:
            name = urllib.quote(name)
            driver=webdriver.PhantomJS()
            driver.get('https://image.baidu.com/search/index?tn=baiduimage&word={}&pn={}'.format(name,papg))
            data=driver.page_source
            driver.quit()
            return data
        except Exception:
            return None
def req(html):#获取图片的utl链接
    try:
        s=r'data-objurl="(http://.*?)"'
        req=re.findall(s,html)
        return req
    except Exception:
        return None
def Loadown(req):#下载图片
    for i in req:
        try:
            #heard={'User-Agent':"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"}
            #urllib2.Request.add_header('User-Agent',"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0")
            if urllib2.urlopen(i).getcode()==200:
                print i
                urllib.urlretrieve(i,name+'/%s'% len(os.listdir(name)))
            else:
                pass
        except Exception :
            pass
def three(req):#多线程
    threading.Thread(target=Loadown, args=(req,)).start()
    while (threading.activeCount() > 5):
        if (threading.activeCount() < 5):
            break;

def ForImg(papg):#循环控制
    time.sleep(1)
    html = get_html(name, papg)
    res = req(html)
    if res != None:
        three(res)

#data-thumburl="https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=2766886107,1571085905&fm=23&gp=0.jpg"
if __name__ == '__main__':#程序入口函数
    print '本爬虫是基于百度图片'
    print '----------------------------------------------------------------------------'
    name = raw_input('请输入搜索的目标:').decode(sys.stdin.encoding)
    name = name.encode('utf-8')
    mkdir(name)
    s=raw_input('请输入需要几页数据')
    if s.isdigit():
        s=int(s)
    else:
        print '请输入数字'
    papg=0
    for i in range(0,s):
        ForImg(papg)
        papg+=20
