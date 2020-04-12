### 算法背景

用于在长字符串中返回匹配到短字符串的第一个索引。

### 暴力解法

```python
# 暴力匹配
def search(sShort, sLong):
    iLenShort = len(sShort)
    iLenLong = len(sLong)
    for i in range(iLenLong - iLenShort):
        for j in range(iLenShort):
            if sShort[j] != sLong[i+j]:
                break;
        # shortStr 全都匹配了
        if j == iLenShort:
        	return i
    # txt 中不存在 shortStr 字串
    return -1

```

时间复杂度 O(MN)，空间复杂度 O(1)

### 优化思路

上述采用双指针解题，那么很自然的想到找办法去减少指针遍历次数。要是能有办法让长串指针跳过检查过的字符就好了

