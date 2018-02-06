# -*- coding: utf-8 -*-
#!/usr/bin/python

import hashlib

class CalculateFile(object):
    def __init__(self, file):
        self.file = file

    def calculate(self):
        m = hashlib.md5()
        sh1 = hashlib.sha1()
        sh256 = hashlib.sha256()
        fopen = open('data/calculate.txt', 'w')
        while not self.file.empty():
            file_name = self.file.get()
            with open(file_name,'r', encoding='utf-8', errors='ignore') as f:
                m.update(f.read(8096).encode("utf8"))
                sh1.update(f.read(8096).encode("utf8"))
                sh256.update(f.read(8096).encode("utf8"))
            fopen.writelines(file_name+"\t"+m.hexdigest()+"\t"+sh1.hexdigest()+"\t"+sh256.hexdigest()+"\n")
        fopen.close()