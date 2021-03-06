# -*- coding:utf-8 -*-
import random
import pprint
from defines import *

RANDOM_MAP = [["" for i in range(I_MAP_WIDTH)] for j in range(I_MAP_HEIGHT)]
lWalkableSpot = []

TEST_MAP = [
    ['▢', '▢', '▢', '▢', '▢', '▢', '▢', '▢', '▢', '▢'],
    ['▢', '▢', '▢', '▢', '■', '▢', '▢', '▢', '▢', '▢'],
    ['▢', '▢', '▢', '▢', '■', '▢', '▢', '▢', '▢', 'EN'],
    ['▢', '▢', '▢', '▢', '■', '▢', '▢', '■', '▢', '▢'],
    ['▢', '▢', '■', '▢', '■', '▢', '▢', '■', '▢', '▢'],
    ['▢', '▢', '■', '▢', '■', '▢', '▢', '■', '▢', '▢'],
    ['ST', '▢', '■', '▢', '■', '▢', '▢', '■', '▢', '▢'],
    ['▢', '▢', '■', '▢', '▢', '▢', '▢', '■', '▢', '▢'],
    ['▢', '▢', '▢', '▢', '▢', '▢', '▢', '■', '▢', '▢'],
    ['▢', '▢', '▢', '▢', '▢', '▢', '▢', '▢', '▢', '▢']
]


def GetTestMap():
    return TEST_MAP


def GetTestStartEnd():
    return (0, 6), (2, 9)


def GetRandomMap():
    if not RANDOM_MAP:
        CreateRandomMap()
    return RANDOM_MAP


def CreateRandomMap():
    for i in range(I_MAP_WIDTH):
        for j in range(I_MAP_HEIGHT):
            iRandInt = random.randint(0, I_MAP_HEIGHT * I_MAP_WIDTH)
            if iRandInt < 30:
                RANDOM_MAP[i][j] = S_BLOCK
            else:
                RANDOM_MAP[i][j] = S_EMPTY
                lWalkableSpot.append((i, j))


def GetStartEnd():
    tStart = lWalkableSpot[0]
    tEnd = lWalkableSpot[len(lWalkableSpot) - 1]
    return tStart, tEnd
