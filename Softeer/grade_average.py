import sys

import math


def banolim(num):
    num = int(num * 1000 //1)
    num_str = str(num)
    
    olim = False


    if int(num_str[-1]) >= 5:
        olim = True
    num_str = num_str[:-1]

    num = int(num_str) / 100
    if olim:
        num += 0.01
    

    return num


N, K = map(int, input().split())

score_li = list(map(int, input().split())) # 학번순

for i in range(K):
    a, b = map(int, input().split())
    sum = 0
    for j in range(a-1, b):
        sum += score_li[j]
    
    print(format(banolim(sum/(b-a+1)),".2f"))
