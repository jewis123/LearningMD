# coding:utf-8
"""
针对基础模块库，进行接口扫描并生成对应的接口文档
eg:
import Interface.scan as scan
scan.ScanApi(sPath, sOutputPath="") 覆盖原有文件，如不想覆盖，传入sOutputPath
"""
import re
import os

S_FUNC_EXTEND = "\n    pass\n\n\n"
S_CLAFUNC_EXTEND = "\n        pass\n\n"

sFuncPattern = re.compile(r"def[^:]*:")
sClsFuncPattern = re.compile(r" +def[^:]*:")
sClsPattern = re.compile(r"class[^:]*:")
sIsFunc = re.compile(r"^def")
sIsCls = re.compile(r"^class")


def ScanApi(sPath, sOutputPath=""):
    obj = CScanApi(sPath)
    obj.run(sOutputPath)


class CScanApi(object):
    def __init__(self, sPath):
        self.m_sPath = sPath

    def run(self, sOutputPath=""):
        bClass = False
        sPath = self.m_sPath
        if not os.path.exists(sPath):
            print 'file not exist!'
            return
        sOutPutCode = ""
        with open(sPath) as f:
            lCode = f.readlines()
            for sCode in lCode:
                if self.isFunc(sCode):
                    bClass = False
                if self.isClass(sCode):
                    bClass = True
                    sApi = self.getClass(sCode)
                elif bClass:
                    sApi = self.getClsFunc(sCode)
                else:
                    sApi = self.getFunc(sCode)
                if sApi:
                    sOutPutCode += sApi
        if not sOutputPath:
            sOutputPath = sPath
        with open(sOutputPath, "w") as f:
            f.write(sOutPutCode)

    def getFunc(self, sCode):
        sApi = ""
        oFuncMatch = re.match(sFuncPattern, sCode)
        if oFuncMatch:
            sApi = oFuncMatch.group(0)
            sApi += S_FUNC_EXTEND
        return sApi

    def getClass(self, sCode):
        sApi = ""
        oClsMatch = re.match(sClsPattern, sCode)
        if oClsMatch:
            sApi = oClsMatch.group(0)
            sApi += "\n"
        return sApi

    def getClsFunc(self, sCode):
        sApi = ""
        oClsFunc = re.match(sClsFuncPattern, sCode)
        if oClsFunc:
            sApi = oClsFunc.group(0)
            sApi += S_CLAFUNC_EXTEND
        return sApi

    def isFunc(self, sCode):
        if re.match(sIsFunc, sCode):
            return True
        return False

    def isClass(self, sCode):
        if re.match(sIsCls, sCode):
            return True
        return False


if __name__ == '__main__':
    sPath = "test.py"
    obj = CScanApi(sPath)
    obj.run("api/"+sPath)


