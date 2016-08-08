# -*- coding:utf-8 -*-
#SQLlib.py的辅助文件
import xml.dom.minidom
import random
#####
#本文件规定，使用本页函数，后面的不能早于前面的
#####


def SpecialXmlGet(filenameext='test.xml',i=0,tag='vector',coding='utf-8'):#专门解析xml文件夹里的xml文件的函数，得到第i+1个test下的tag
    #test的起始和结束标签之间的内容,返回coding编码字符串，不做encode处理会返回unicode
    dom=xml.dom.minidom.parse('xml/'+filenameext)#windows路径习惯
    root=dom.documentElement
    test=root.getElementsByTagName('test')[i]
    #tag不存在会导致IndexError,标签之间没有内容会导致AttributeError
    try:
        return test.getElementsByTagName(tag)[0].firstChild.data.encode(coding)
    except AttributeError:
        return ''

def SpecialXmlGetAll(filenameext='test.xml',tag='vector',coding='utf-8'):
    #得到xml下某个文件的全部vector标签内容，返回列表
    #不做encode处理会返回utf-8
    dom=xml.dom.minidom.parse('xml/'+filenameext)
    root=dom.documentElement
    goal=root.getElementsByTagName(tag)
    r=[]
    for i in xrange(0,len(goal)):
        try:
            r.append(goal[i].firstChild.data.encode(coding))
        except AttributeError:
            pass
    return r

def prefix(s=''，do=''):#对传递的字符串前缀做匹配do的if下的处理
    #这个函数不建议自行添加，需要才添加
    do=do.lower()
    if do=='':
        return s
    if do=='intfalse':#整形False逻辑
        s=' and [RANDNUM]=[RANDNUM1] '+s
        return s
    if do=='charfalse':#字符型False逻辑
        s="' and '[RANDNUM]'='[RANDNUM1]' "+s
        return s

def suffix(s='',do=''):#后缀处理
    if do=='':
        return s
    if do=='comment1':#mysql注释处理方法  #
        s+=' #'
        return s

def MSHandle(s=''):
    ##处理XML文件里支持的在payload里加上特殊含义的[]MS
    #返回的可能是列表也可能是字符串
    flag=0#标志是否处理过任何一个s的拓展，这是返回值会是一个列表了
    i=random.randint(100,500)#含上下限
    s.replace('[RANDNUM]',str(i))
    i=random.randint(600,800)
    s.replace('[RANDNUM1]',str(i))
    #[INFERENCE]
    if s.find([SEQINT])!=-1 and flag=0:
        sl=[]
        seq=''
        for i in xrange(0,10):
            seq+=str(i)
            sl.append(s.replace('[SEQINT]',seq))
            seq+=','

    if flag==0:
        return s
    else:
        return sl
    
        
    





if __name__=='__main__':
    print SpecialXmlGetAll()
    
