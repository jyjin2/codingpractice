import sys
input = sys.stdin.readline

n = int(input())
serial = [ input().strip() for _ in range(n) ]

# 버블 정렬
for i in range(n):
    for j in range(i+1, n):
        # 1. 길이가 다르면 짧은 거 먼저
        if len(serial[i]) > len(serial[j]):
            serial[i], serial[j] = serial[j], serial[i]
            
        # 2. 길이 같다면 숫자의 합이 더 작은 것이 먼저
        elif len(serial[i]) == len(serial[j]):
            sumA = 0
            sumB = 0
            for x, y in zip(serial[i], serial[j]):
                if x.isdigit():
                    sumA += int(x)
                if y.isdigit():
                    sumB += int(y)
            if sumA > sumB:
                serial[i], serial[j] = serial[j], serial[i]
            elif sumA == sumB:
                if serial[i] > serial[j]:
                    serial[i], serial[j] = serial[j], serial[i]

for s in serial:
    print(s)
            
        

