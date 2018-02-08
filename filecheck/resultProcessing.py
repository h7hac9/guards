# -*- coding: utf-8 -*-
#!/usr/bin/python

class ResultProcess(object):
    def __init__(self, result):
        self.result = result

    def startProcess(self):
        i = 0
        while i < len(self.result):
            if self.result[i].split(' ')[0] == '-' and self.result[i+1].split(' ')[0] == "?" and self.result[i+2].split(' ')[0] == "+" and self.result[i+3].split(' ')[0] == "?":
                print(u"{0}文件被修改".format(self.result[i].split(' ')[1]))
                i += 4
            elif self.result[i].split(' ')[0] == '+':
                print(u"增加了一个新文件：{0}".format(self.result[i].split(' ')[1]))
                i += 1
            elif self.result[i].split(' ')[0] == '-':
                print(u"{0}文件被删除".format(self.result[i].split(' ')[1]))
                i += 1
            else:
                i += 1