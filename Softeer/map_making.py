import sys


N, = map(int, input().split())



# 정사각형이니까 한변만 보면 됨. 
# 한변기준 / 0단계에 점 2개 (변이 1개라 점이 1개 추가되면), 1단계에서 점이 3개 (변이 2개라 점이 2개 추가되면), 2단계에서 점이 5개 

# 전체 점의 개수는 한 변에 있는 점의 개수^2


NofP = 2 # 0단계

for i in range(1, N+1):
    
    NofL = NofP - 1
    NofP += NofL

print(NofP*NofP)
