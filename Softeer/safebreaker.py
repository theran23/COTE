import sys

W, N = map(int, input().split())

li = []
for i in range(N):
    li.append(list(map(int, input().split())))



# 배낭은 W까지 담을 수 잇다. 

answer = 0 # 배낭을 채울 수 있는 가장 비싼 가격은 얼마?


li.sort(key= lambda x: x[1],reverse=True)

weight = 0
price = 0
for stone in li:
    weight += stone[0]
    price += stone[0]*stone[1]
    if weight > W:
        price -= (weight-W)*stone[1]
        break

answer = price

print(answer)
