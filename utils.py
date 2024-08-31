import math
import matplotlib.colors as mcolors
# all possibilities
allPossibilities = [[0, 0, 0, 0],
                    [1, 0, 0, 0],
                    [1, 1, 0, 0],
                    [0, 0, 1, 0],
                    [1, 0, 1, 0],
                    [1, 1, 1, 0],
                    [0, 0, 1, 1],
                    [1, 0, 1, 1],
                    [1, 1, 1, 1]]
# values to colors
def valueToColor(value):
    if value == 1:
        return mcolors.to_rgba('red')
    else:
        return mcolors.to_rgba('white')

def checkMonotonicFunction(function):
    for i in range(9):
        for j in range(9):
            a = allPossibilities[i]
            b = allPossibilities[j]
            #not(x>=y ->fx>=fy) = x>=y and fx<fy
            # same inhibitors but activators are greater or equal in number and the value
            c1_inh = a[2] + a[3]
            c2_inh = b[2] + b[3]
            c1_act = a[0] + a[1]
            c2_act = b[0] + b[1]
            if c1_inh == c2_inh and c1_act<c2_act and function[i] > function[j]:
                return False
            # same activators but inhibitors are greater or equal in number and the value   
            if c1_act == c2_act and c1_inh>c2_inh and function[i] > function[j]:
                return False
    # if all inhibitors or activators are on:
    if function[2] != 1 or function[6] != 0:
        return False
    return True
# helper methods for getPossibleCombinations
def BinArrayToNum(arr):
    res = 0
    for idx, num in enumerate(arr[::-1]):
        res += num * math.pow(2, idx)
    return int(res)

def NumToBinArray(num, totallen):
    arr = []
    while num:
        res = num % 2
        arr.append(res)
        num = num // 2
    while totallen > len(arr):
        arr.append(0)
    return arr[::-1]
# returns all 2^9 possible functions
def getPossibleCombinations(length):
    res = []
    for i in range(2 ** length):
        res.append(NumToBinArray(i, length))
    return res
