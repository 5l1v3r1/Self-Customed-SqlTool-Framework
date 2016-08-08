# -*- coding:utf-8 -*-
import os
def main():
    name=raw_input(">请输入文件名，不带后缀:")
    if os.path.exists(name+'.xml')==True:
        print "文件已存在"
        return 0
    else:
        f=open(name+'.xml','w')
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<root>\n')
        x=''
        while x!='x':
            title=raw_input(">输入标题:")
            vector=raw_input(">输入攻击向量"+"(提示攻击向量中支持MS字符,见xml/说明.txt):")
            
            f.write("    <test>\n")
            f.write("        <title>"+title+"</title>\n")
            f.write("        <stype></stype>\n")
            f.write("        <level></level>\n")
            f.write("        <risk></risk>\n")
            f.write("        <clause></clause>\n")
            f.write("        <where></where>\n")
            f.write("        <vector>"+vector+"</vector>\n")
            f.write("        <request>\n")
            f.write("            <payload></payload>\n")
            f.write("        </request>\n")
            f.write("        <response>\n")
            f.write("            <comparison></comparison>\n")

            f.write("        </response>\n")
            f.write("        <details>\n")
            f.write("            <dbms></dbms>\n")
            f.write("            <dbms_version></dbms_version>\n")
            f.write("            <os></os>\n")
            f.write("        </details>\n")
            f.write("    </test>\n")
                    
            x=raw_input(">x|X退出，其余键继续:").lower()
        f.write("</root>")
        f.close()
        return 1
        
main()










            
            
