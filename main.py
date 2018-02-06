#!/usr/bin/python

import datetime

from filecheck.fileScan import ReadFile
from filecheck.fileCalculate import CalculateFile

def main():
    start = datetime.datetime.now()
    file = ReadFile(root='/home/asura/Documents/Code')
    file.getFile()
    calculateFile = CalculateFile(file.file)
    calculateFile.calculate()
    end = datetime.datetime.now()
    print((end-start).seconds)


if __name__ == '__main__':
    main()
