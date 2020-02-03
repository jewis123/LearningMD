# coding=utf-8
import xlrd
import argparse
import os

def scanAllExcel(inDest, outDest):
	for sFileName in os.listdir(inDest):
		if not parseExcel(inDest, sFileName, outDest):
			print('在解析%s时发生错误!'%sFileName)
			return False
	return True



def parseExcel(inDest, inFile, outPath):
	filePath = '{}/{}'.format(inDest,inFile)
	workbook = xlrd.open_workbook(filePath)
	sheet = workbook.sheet_by_index(0)
	nrows = sheet.nrows
	ncols = sheet.ncols
	dData = parseSheet(sheet, nrows, ncols)
	sFileName = '%s.py' % inFile.split('.')[0]
	if write2File(outPath, sFileName, dData):
		return True
	return False


def parseSheet(sheet, nrows, ncols):
	dData = {}
	for cellRow in range(1, nrows):
		dRowData = {}
		id = int(sheet.cell_value(cellRow, 0))
		for cellCol in range(1, ncols-1, 2):
			dRowData[sheet.cell_value(0, cellCol+1)] = sheet.cell_value(cellRow, cellCol)
		dData[id] = dRowData
	return dData


def write2File(sOutPath, sFileName, dData):
	try:
		msg = ''
		for key, value in dData.items():
			msg += '{}:{},\n'.format(str(key), str(value))
		msg = """DATA = {
%s
}""" % msg
		with open('{}/{}'.format(sOutPath,sFileName), 'w', encoding='utf-8') as f:
			f.write(msg)
	except IOError:
		print('[IO ERROR]')
		return False

	return True


def parseArg():
	'''
	解析命令行参数
	:return: 参数列表
	'''
	parser = argparse.ArgumentParser()
	parser.add_argument('inDest', type = str, help= u'excel目录')
	parser.add_argument('outDest', type = str, help= u'输出目录')
	args = parser.parse_args()
	return args


def getInput():
	inDest = input('请输入要解析的目录（支持拖拽）:')
	while not inDest:
		print('[ERROR]:空路径!')
		inDest = input('请输入要解析的目录（支持拖拽）:')

	outDest = input('请输入要输出的目录（支持拖拽）:')
	while not outDest:
		print('[ERROR]:空路径!')
		outDest = input('请输入要输出的目录（支持拖拽）:')
	return inDest,outDest


def exeFunc():
	inDest, outDest = getInput()
	while not scanAllExcel(inDest, outDest):
		print('失败,检查输入路径是否正确')
		inDest, outDest = getInput()
	result = input('完成，输入任意键退出..')

def cmdFunc():
	args = parseArg()
	inDest = args.inDest
	if not inDest:
		print ('[ERROR]:EMPTY IN FILE PATH!')
	outDest = args.outDest
	if not outDest:
		print('[ERROR]:EMPTY OUT FILE PATH!')
	if scanAllExcel(inDest, outDest):
		print ('输出成功！')


if __name__ == '__main__':
	cmdFunc()
	# exeFunc()

