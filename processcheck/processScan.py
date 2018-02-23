#!/usr/bin/python

import psutil

from config import logger

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
        parent_pid = psutil.Process(pid).parent()
        return [process_name,process_user]


    def pidContrast(self, oldPidList, newPidList, oldPidInformation, newPidInformation):
        """
        进程状态检查
        :param oldPidList:之前进程
        :param newPidList:新状态进程
        :param oldPidInformation:旧状态进程信息
        :param newPidInformation:新进程状态信息
        :return:新创建进程列表
        """
        oldStopPidList = set(oldPidList) - set(newPidList)
        newStartPidList = set(newPidList) - set(oldPidList)
        if oldStopPidList.__len__() != 0:
            logger.info(u"某些进程被关闭:\n")
            # print(u"某些进程被关闭:\n")
            for i in oldStopPidList:
                logger.info(str(oldPidInformation[i][0]) + "\t" + str(oldPidInformation[1]) + "\t" + "\n")
                # print(str(oldPidInformation[i][0]) + "\t" + str(oldPidInformation[1]) + "\t" + "\n")
            return None
        if newStartPidList.__len__() != 0:
            logger.info(u"某些新进程被创建:\n")
            # print(u"某些新进程被创建:\n")
            for i in newStartPidList:
                logger.info(str(newPidInformation[i][0]) + "\t" + str(newPidInformation[1]) + "\t" + "\n")
                # print(str(newPidInformation[i][0]) + "\t" + str(newPidInformation[1]) + "\t" + "\n")
            return newStartPidList

    def privilgeEscalation(self, pidList):
        """
        提权检查
        :param pidList:新创建的进程
        :return:
        """
        if pidList is not None:
            for i in pidList:
                if (int(i) < int(psutil.Process(i).parent().pid)):
                    logger.info(u"提权进程被创建")
                else:
                    pass