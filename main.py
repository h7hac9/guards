#!/usr/bin/python

import datetime
import os
import time
from multiprocessing import Pool
from watchdog.observers import Observer

from filecheck.fileScan import ReadFile
from filecheck.fileCalculate import CalculateFile
from filecheck.resultProcessing import ResultProcess
from configurate.readyaml import yamloperation
from watchfile.fileMonitoring import FileHandler
from processcheck.processScan import ProcessScaner

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

def watchdogmethod(path):
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, path=path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

def main():
    # pool = Pool() #进程池
    # config = yamloperation('guards.yaml')
    # configFile = config.readConfig()
    # if configFile.get("directory") is not None and configFile.get("directory").get("watchdog") is not True:
    #     for i in configFile['directory']['target']:
    #         print(i)
    #         pool.apply_async(mainfilecheck, args=(i,))
    #     pool.close()
    #     pool.join()
    #
    # ##watchdog 模块
    # if configFile.get("directory") is not None and configFile.get("directory").get("watchdog") is True:
    #     for i in configFile['directory']['target']:
    #         pool.apply_async(watchdogmethod, args=(i,))
    #     pool.close()
    #     pool.join()
    processScan = ProcessScaner()
    while True:
        processInformation = processScan.getPids()
        time.sleep(10)
        newProcessInformation = processScan.getPids()
        processScan.pidContrast(processInformation.keys(), newProcessInformation.keys(), processInformation,
                                newProcessInformation)




if __name__ == '__main__':
    main()
