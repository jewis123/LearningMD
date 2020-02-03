# coding:utf-8
eg:
import Interface.scan as scan
scan.ScanApi(sPath, sOutputPath="")
"""
import scan
sPath = "test.py"
# 覆盖原有文件
# scan.ScanApi(sPath)
# 如不想覆盖，传入sOutputPath
scan.ScanApi(sPath, "new/" + sPath)
