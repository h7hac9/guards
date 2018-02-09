#!/usr/bin/python

import psutil

class ProcessScaner(object):
    def __init__(self):
        pass

    def getPids(self):
        pid_informations = dict()
        pid_list = psutil.pids()
        for i in pid_list:
            pid_informations.__setitem__(i,self.getInformation(i))
        return pid_informations

    def getInformation(self, pid):
        process_name = psutil.Process(pid).name()
        process_user = psutil.Process(pid).username()
        return [process_name,process_user]


    def pidContrast(self, oldPidList, newPidList, oldPidInformation, newPidInformation):
        oldStopPidList = set(oldPidList) - set(newPidList)
        newStartPidList = set(newPidList) - set(oldPidList)
        if oldStopPidList.__len__() != 0:
            print(u"某些进程被关闭:\n")
            for i in oldStopPidList:
                print(str(oldPidInformation[i][0]) + "\t" + str(oldPidInformation[1]) + "\t" + "\n")
        if newStartPidList.__len__() != 0:
            print(u"某些新进程被创建:\n")
            for i in newStartPidList:
                print(str(newPidInformation[i][0]) + "\t" + str(newPidInformation[1]) + "\t" + "\n")