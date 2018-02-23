# -*- coding: utf-8 -*-
#!/usr/bin/python

import os

from watchdog.events import FileSystemEventHandler
from webshellcheck import webshellScan
from configurate import readyaml
from config import logger


class FileHandler(FileSystemEventHandler):
    """
    继承事件处理类FileSystemEventHandler
    """
    def __init__(self):
        super(FileHandler, self).__init__()
        self.config = readyaml.yamloperation('guards.yaml')
        self.configFile = self.config.readConfig()
    def on_created(self, event):
        """
        重写FileSystemEventHandler类的on_created方法
        :param event: 事件消息
        :return:
        """
        if self.configFile.get('webshell') is not None and self.configFile.get('webshell').get('check') is True:
            if os.path.isfile(event.src_path):
                webshellscanner = webshellScan.WebshellScanner()
                message = webshellscanner.file2shellCompare(event.src_path, self.configFile.get('webshell').get('delpermissions'))
                if message != "True" and self.configFile.get('webshell').get('delpermissions') is True:
                    logger.info(u"检测到webshell，已删除,所属类型:{}".format(message))
                    # print(u"检测到webshell，已删除,所属类型:{}".format(message))
                elif message != "True" and self.configFile.get('webshell').get('delpermissions') is True:
                    logger.info(u"检测到webshell，未有删除权限,所属类型:{}".format(message))
                    # print(u"检测到webshell，未有删除权限,所属类型:{}".format(message))
                elif message == "True":
                    pass
        else:
            if event.is_directory:
                logger.info(u"{} 文件夹被创建".format(event.src_path))
                # print(u"{} 文件夹被创建".format(event.src_path))
            else :
                logger.info(u"{} 文件被创建".format(event.src_path))
                # print(u"{} 文件被创建".format(event.src_path))

    def on_deleted(self, event):
        if event.is_directory:
            logger.info(u"{} 文件夹被删除".format(event.src_path))
            # print(u"{} 文件夹被删除".format(event.src_path))
        else :
            logger.info(u"{} 文件被删除".format(event.src_path))
            # print(u"{} 文件被删除".format(event.src_path))
        pass

    def on_modified(self, event):
        if os.path.isfile(event.src_path):
            webshellscanner = webshellScan.WebshellScanner()
            message = webshellscanner.file2shellCompare(event.src_path,
                                                        self.configFile.get('webshell').get('delpermissions'))
            if message != "True" and self.configFile.get('webshell').get('delpermissions') is True:
                logger.info(u"检测到webshell，已删除,所属类型:{}".format(message))
                # print(u"检测到webshell，已删除,所属类型:{}".format(message))
            elif message != "True" and self.configFile.get('webshell').get('delpermissions') is True:
                logger.info(u"检测到webshell，未有删除权限,所属类型:{}".format(message))
                # print(u"检测到webshell，未有删除权限,所属类型:{}".format(message))
            elif message == "True":
                pass
        else:
            if event.is_directory:
                logger.info(u"{} 文件夹被修改".format(event.src_path))
                # print(u"{} 文件夹被修改".format(event.src_path))
            else :
                logger.info(u"{} 文件被修改".format(event.src_path))
                # print(u"{} 文件被修改".format(event.src_path))
        pass

    def on_moved(self, event):
        if event.is_directory:
            logger.info(u"{} 文件夹被移动到{}".format(event.src_path,event.dest_path))
            # print(u"{} 文件夹被移动到{}".format(event.src_path,event.dest_path))
        else :
            logger.info(u"{} 文件被移动到{}".format(event.src_path, event.dest_path))
            # print(u"{} 文件被移动到{}".format(event.src_path, event.dest_path))
        pass