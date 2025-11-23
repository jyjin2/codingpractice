import sys
input = sys.stdin.readline

k, n = map(int, input().split())
arr = [ input().strip() for _ in range(k) ]
arr.sort(key=lambda x:x*10, reverse=True)
maxi = max(arr, key=int)

for i in range(n-k):
    arr.append(maxi)

arr.sort(key=lambda x:x*10, reverse=True)

print("".join(arr))