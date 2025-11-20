import sys
input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

# 압축된 좌표는 배열의 인덱스 값
# 먼저 input array를 정렬하고
# set으로 중복 제거하고
# dict으로 각자의 키(인덱스) 구하기

sortedLi = sorted(set(li))

dictLi = {val: idx for idx, val in enumerate(sortedLi)}

for i in li:
    print(dictLi[i], end=" ")