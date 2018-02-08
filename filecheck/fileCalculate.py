# -*- coding: utf-8 -*-
#!/usr/bin/python

import hashlib
import difflib
import filecmp
import queue
import os

from .fileScan import ReadFile

class CalculateFile(object):
    def __init__(self, file):
        self.file = file

    def calculate(self, resultname):
        fopen = open('data/'+resultname, 'w')
        while not self.file.empty():
            m = hashlib.md5()
            sh1 = hashlib.sha1()
            sh256 = hashlib.sha256()
            file_name = self.file.get()
            with open(file_name,'r', encoding='utf-8', errors='ignore') as f:
                m.update(f.read(8096).encode("utf8"))
                sh1.update(f.read(8096).encode("utf8"))
                sh256.update(f.read(8096).encode("utf8"))
            fopen.writelines(file_name+"\t"+m.hexdigest()+"\t"+sh1.hexdigest()+"\t"+sh256.hexdigest()+"\n")
        fopen.close()

    def comparison(self, strFile):
        line_result = queue.Queue()
        if not filecmp.cmp(r'data/'+strFile,r'data/'+strFile+'.0'):
            text1 = ReadFile(root='').readFile(filename='data/'+strFile)
            text2 = ReadFile(root='').readFile(filename='data/'+strFile+'.0')
            d = difflib.Differ()  # 创建Differ对象
            diff = d.compare(text1, text2)
            for i in list(diff):
                line_result.put(i)
            return line_result
        else:
            print(u"文件无修改")
            return line_result