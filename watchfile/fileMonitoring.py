# -*- coding: utf-8 -*-
#!/usr/bin/python

from watchdog.events import FileSystemEventHandler
from webshellcheck import webshellScan
import os


class FileHandler(FileSystemEventHandler):
    """
    继承事件处理类FileSystemEventHandler
    """
    def on_created(self, event):
        """
        重写FileSystemEventHandler类的on_created方法
        :param event: 事件消息
        :return:
        """
        if event.is_directory:
            print(u"{} 文件夹被创建".format(event.src_path))
        else :
            print(u"{} 文件被创建".format(event.src_path))
        if os.path.isfile(event.src_path):
            webshellscanner = webshellScan.WebshellScanner()
            message = webshellscanner.file2shellCompare(event.src_path)
            if message is not "True":
                print(u"检测到webshell，已删除,所属类型:{}".format(message))
        pass

    def on_deleted(self, event):
        if event.is_directory:
            print(u"{} 文件夹被删除".format(event.src_path))
        else :
            print(u"{} 文件被删除".format(event.src_path))
        pass

    def on_modified(self, event):
        if event.is_directory:
            print(u"{} 文件夹被修改".format(event.src_path))
        else :
            print(u"{} 文件被修改".format(event.src_path))
        if os.path.isfile(event.src_path):
            webshellscanner = webshellScan.WebshellScanner()
            message = webshellscanner.file2shellCompare(event.src_path)
            if message is not "True":
                print(u"检测到webshell，已删除,所属类型:{}".format(message))
        pass

    def on_moved(self, event):
        if event.is_directory:
            print(u"{} 文件夹被移动到{}".format(event.src_path,event.dest_path))
        else :
            print(u"{} 文件被移动到{}".format(event.src_path, event.dest_path))
        pass