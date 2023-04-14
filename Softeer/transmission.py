import sys

li = list(map(int, input().split()))


a = 0 # 연속적인(예를 들어 1->2) 증가 변속 횟수
d = 0 # 연속적인(예를 들어 1->2) 감속 변속 횟수


for i in range(len(li)-1):
    tmp = li[i+1] - li[i]
    if tmp == 1:
        a += 1
    elif tmp == -1:
        d += 1

if a == len(li) -1:
    print("ascending")
elif d == len(li) -1:
    print("descending")
else:
    print("mixed")
