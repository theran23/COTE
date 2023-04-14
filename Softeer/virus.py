import sys


K, P, N = map(int, input().split())


R  = K # 주어진 조건에 의해 K의 최대값은 1000000007을 넘을 수 없음
for t in range(1, N+1):

    R = R * P % 1000000007


print(R)
