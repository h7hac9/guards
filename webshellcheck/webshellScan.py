#!/usr/bin/python

from ssdeep import hash_from_file
from ssdeep import compare
from os import remove

class WebshellScanner(object):
    def __init__(self):
        pass

    def file2shellCompare(self, filepath, delpermissions):
        hashFile = self.file2ssdeep(filepath)

        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            if 'php' in f.read().lower() or 'php' in filepath:
                with open('wsl/php.wsl','r',encoding='utf-8', errors='replace') as k:
                    for i in k.readlines():
                        if compare(hashFile, i.split('\t')[0]) > 60:
                            if delpermissions is True:
                                remove(filepath)
                            return i.split('\t')[1]
                        else:
                            pass
                    return "True"

            elif 'asp' in f.read().lower() or 'aspx' in f.read().lower() or 'asp' in filepath or 'aspx' in filepath:
                with open('wsl/asp.wsl','r',encoding='utf-8', errors='replace') as k:
                    for i in k.readlines():
                        if compare(hashFile, i.split('\t')[0]) > 60:
                            if delpermissions is True:
                                remove(filepath)
                            return i.split('\t')[1]
                        else:
                            pass
                    return "True"

            elif 'jsp' in f.read().lower() or 'jspx' in f.read().lower() or 'jsp' in filepath or 'jspx' in filepath:
                with open('wsl/jsp.wsl','r',encoding='utf-8', errors='replace') as k:
                    for i in k.readlines():
                        if compare(hashFile, i.split('\t')[0]) > 60:
                            if delpermissions is True:
                                remove(filepath)
                            return i.split('\t')[1]
                        else:
                            pass
                    return "True"

            else:
                with open('wsl/other.wsl','r',encoding='utf-8', errors='replace') as k:
                    for i in k.readlines():
                        if compare(hashFile, i.split('\t')[0]) > 60:
                            if delpermissions is True:
                                remove(filepath)
                            return i.split('\t')[1]
                        else:
                            pass
                    return "True"

    def file2ssdeep(self, filepath):
        return hash_from_file(filepath)