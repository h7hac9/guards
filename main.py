#!/usr/bin/python

import datetime
import os
import time

from filecheck.fileScan import ReadFile
from filecheck.fileCalculate import CalculateFile
from filecheck.resultProcessing import ResultProcess

def main():
    start = datetime.datetime.now()
    file = ReadFile(root='/home/asura/Documents/note')
    file.getFile()
    calculateFile = CalculateFile(file.file)
    calculateFile.calculate('calculate.txt')
    end = datetime.datetime.now()
    print((end-start).seconds)

    while True:
        start = datetime.datetime.now()
        file = ReadFile(root='/home/asura/Documents/note')
        resultfile = file.getFile()
        calculateFile = CalculateFile(resultfile)
        calculateFile.calculate('calculate.txt.0')
        fileResult = calculateFile.comparison()
        if not fileResult.empty():
            os.rename('data/calculate.txt.0', 'data/calculate.txt')
        else:
            os.remove('data/calculate.txt.0')

        result = []
        while not fileResult.empty():
            result.append(fileResult.get().split('\t')[0])

        resultProcess = ResultProcess(result)
        resultProcess.startProcess()
        end = datetime.datetime.now()
        print((end - start).seconds)
        time.sleep(10)


if __name__ == '__main__':
    main()
