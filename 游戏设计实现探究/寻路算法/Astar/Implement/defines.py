# -*- coding:utf-8 -*-
"""

"""

I_MAP_WIDTH = 10
I_MAP_HEIGHT = 10

S_BLOCK = '■'
S_EMPTY = '□'
S_START = '☆'
S_END = '★'
S_PATH = '▲'

# 10*10
MAP1 = [
    ['□', '□', '□', '□', '□', '□', '□', '□', '□', '★'],
    ['□', '□', '□', '□', '□', '□', '□', '□', '□', '□'],
    ['□', '□', '□', '□', '□', '■', '■', '■', '□', '□'],
    ['□', '□', '□', '■', '□', '□', '□', '□', '□', '□'],
    ['□', '□', '□', '■', '□', '□', '□', '□', '■', '□'],
    ['□', '□', '□', '■', '□', '□', '□', '□', '■', '□'],
    ['□', '□', '□', '□', '■', '■', '■', '■', '■', '■'],
    ['■', '■', '■', '□', '□', '□', '□', '□', '□', '□'],
    ['□', '□', '□', '□', '□', '□', '□', '□', '■', '□'],
    ['☆', '□', '□', '□', '□', '□', '□', '■', '■', '□'],
]


def GetStartEndPos():
    tStart = tEnd = (0, 0)
    bStartFind = bEndFind = False
    for row in range(I_MAP_HEIGHT):
        for col in range(I_MAP_WIDTH):
            if MAP1[row][col] == S_START:
                tStart = (row, col)
                bStartFind = True
            elif MAP1[row][col] == S_END:
                tEnd = (row, col)
                bEndFind = True
            if bEndFind and bStartFind:
                break
    return tStart, tEnd

