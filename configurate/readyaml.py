#!/usr/bin/python

import yaml

class yamloperation(object):
    """
    yaml配置文件类
    """
    def __init__(self, configureFile):
        self.configureFile = configureFile

    def readConfig(self):
        """
        读取配置文件
        :return: 配置文件内容，类型：字典类型
        """
        with open('etc/'+self.configureFile) as f:
            configResult = yaml.load(f)
        return configResult