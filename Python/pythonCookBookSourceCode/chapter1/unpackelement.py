# -*-coding: utf-8 -*-
elems = [1,2,3,4,5,6,7,8,9]
first, *rest = elems
print(first,rest)

def sum(items):
    first, *rest = items
    return first + sum(rest) if rest else first

print(sum(elems))