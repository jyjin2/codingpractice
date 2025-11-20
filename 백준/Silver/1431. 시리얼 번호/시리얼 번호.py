import sys
input = sys.stdin.readline

n = int(input())

def num_sum(arr):
    ans = 0
    for i in arr:
        if i.isdigit():
            ans += int(i)
    return ans

serial = [input().strip() for _ in range(n)]

for i in range(n):
    for j in range(i+1, n):
        # 1. 길이가 짧은 것이 먼저
        if len(serial[i]) > len(serial[j]):
            serial[i], serial[j] = serial[j], serial[i]
            continue
        # 2. 길이가 같다면 숫자들의 합이 작은 게 먼저
        if len(serial[i]) == len(serial[j]):
            if num_sum(serial[i]) > num_sum(serial[j]):
                serial[i], serial[j] = serial[j], serial[i]
                continue
            # 3. 같으면 사전순으로 비교 (숫자 먼저)
            if num_sum(serial[i]) == num_sum(serial[j]):
                if serial[i] > serial[j]:
                    serial[i], serial[j] = serial[j], serial[i]
            
for s in serial:
    print(s)