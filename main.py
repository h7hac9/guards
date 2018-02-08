#!/usr/bin/python

import datetime
import os
import time
from multiprocessing import Pool

from filecheck.fileScan import ReadFile
from filecheck.fileCalculate import CalculateFile
from filecheck.resultProcessing import ResultProcess

def mainfilecheck(root):
    tmp_file = str(os.getpid()) + '.txt'
    try:
        start = datetime.datetime.now()
        file = ReadFile(root=root)
        file.getFile()
        calculateFile = CalculateFile(file.file)
        calculateFile.calculate(tmp_file)
        end = datetime.datetime.now()
        print((end - start).seconds)

        while True:
            start = datetime.datetime.now()
            file = ReadFile(root=root)
            resultfile = file.getFile()
            calculateFile = CalculateFile(resultfile)
            calculateFile.calculate(tmp_file + '.0')
            fileResult = calculateFile.comparison(tmp_file)
            if not fileResult.empty():
                os.rename('data/' + tmp_file + '.0', 'data/' + tmp_file)
            else:
                os.remove('data/' + tmp_file + '.0')

            result = []
            while not fileResult.empty():
                result.append(fileResult.get().split('\t')[0])

            resultProcess = ResultProcess(result)
            resultProcess.startProcess()
            end = datetime.datetime.now()
            print((end - start).seconds)
            time.sleep(5)
    except Exception as e:
        print(str(e))
    finally:
        os.remove('data/' + tmp_file)
        os.remove('data/' + tmp_file + '.0')

def main():
    pool = Pool()
    for i in range(5):
        pool.apply_async(mainfilecheck, args=('/home/asura/Documents/note',))
    print('Watting .....')
    pool.close()
    pool.join()
    # mainfilecheck('/home/asura/Documents/note')
    pass



if __name__ == '__main__':
    main()
