#!/usr/bin/python

import os
import queue



class ReadFile(object):

    def __init__(self, **kwargs):
        self.root = kwargs['root']

    def getFile(self, ):
        self.file = queue.Queue()
        for root, dirs, files in os.walk(self.root):
            for i in files:
                # print(os.path.join(root, i))
                self.file.put(os.path.join(root, i))
        return self.file

    def getFileNumber(self):
        return self.file.__sizeof__()

    def readFile(self, filename):
        try:
            with open(filename,'r') as fileHandle:
                text = fileHandle.read().splitlines()
            return text
        except IOError as e:
            print("Read File Error:"+str(e))