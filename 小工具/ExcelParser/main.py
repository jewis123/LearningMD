import xlrd
import os
import argparse

def ParseExcel(inFile, sheet_index, outFile):
	workbook = xlrd.open_workbook(inFile)
	sheet = workbook.sheet_by_index(sheet_index)
	nrows = sheet.nrows
	ncols = sheet.ncols
	dData = ParseSheet(sheet,nrows,ncols)
	Write2File(outFile, dData)


def ParseSheet(sheet,nrows,ncols):
	dData = {}
	parseDict = {
		1: 'sName',
		2: 'iAge'
	}
	for cellRow in range(1, nrows):
		dRowData = {}
		id = int(sheet.cell_value(cellRow,0))
		for cellCol in range(1, ncols):
			dRowData[parseDict[cellCol]] = sheet.cell_value(cellRow,cellCol)
		dData[id] = dRowData
	return dData


def Write2File(sOutputName, dData):
	msg = "DATA = %s"%str(dData)
	with open(sOutputName,'w',encoding='utf-8') as f:
		f.write(msg)


def parseArg():
	'''
	解析命令行参数
	:return: 参数列表
	'''
	parser = argparse.ArgumentParser()
	parser.add_argument('infile', type = str, help= u'待解析的excel')
	parser.add_argument('-idx',dest = 'idx',type = int, help= u'excel页签索引') #可选属性
	parser.add_argument('outfile', type = str, help= u'输出文件')
	args = parser.parse_args()
	return args


if __name__ == '__main__':
	args = parseArg()
	infile = args.infile
	if not infile:
		print ('[ERROR]:EMPTY IN FILE PATH!')
	index = args.idx if args.idx else 0
	outfile = args.outfile
	if not outfile:
		print('[ERROR]:EMPTY OUT FILE PATH!')
	ParseExcel(infile, index, outfile)
