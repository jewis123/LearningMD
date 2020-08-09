# -*- coding:utf-8 -*-
"""

"""

def proxyGen():
    lDirStright = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    lDirDiagnal = [(-1, -1), (1, 1), (-1, 1), (1, -1)]
    for t in lDirDiagnal:
        if t[0] > 0:
            yield t
    for t in lDirStright:
        yield t


def Gen():
    yield from proxyGen()

for i in Gen():
    print(i)