#!/usr/bin/python

from ssdeep import hash_from_file
from ssdeep import compare
from os import remove

class WebshellScanner(object):
    def __init__(self):
        pass

    def file2shellCompare(self, filepath):
        hashFile = self.file2ssdeep(filepath)

        with open(filepath, 'r') as f:
            if 'php' in f.read().lower():
                with open('wsl/php.wsl','r') as k:
                    for i in k.readlines():
                        if compare(hashFile, i.split('\t')[0]) > 60:
                            remove(filepath)
                            return i.split('\t')[1]
                        else:
                            return "True"

            elif 'asp' in f.read().lower() or 'aspx' in f.read().lower():
                with open('wsl/asp.wsl','r') as k:
                    for i in k.readlines():
                        if compare(hashFile, i.split('\t')[0]) > 60:
                            remove(filepath)
                            return i.split('\t')[1]
                        else:
                            return "True"

            elif 'jsp' in f.read().lower() or 'jspx' in f.read().lower():
                with open('wsl/jsp.wsl','r') as k:
                    for i in k.readlines():
                        if compare(hashFile, i.split('\t')[0]) > 60:
                            remove(filepath)
                            return i.split('\t')[1]
                        else:
                            return "True"

            else:
                with open('wsl/other.wsl','r') as k:
                    for i in k.readlines():
                        if compare(hashFile, i.split('\t')[0]) > 60:
                            remove(filepath)
                            return i.split('\t')[1]
                        else:
                            return "True"

    def file2ssdeep(self, filepath):
        return hash_from_file(filepath)