import sys
input = sys.stdin.readline

n = int(input())
cnt = [0] * 2000001

for _ in range(n):
    cnt[int(input()) + 1000000] = 1

for i in range(2000001):
    if cnt[i] == 1:
        print(i - 1000000)