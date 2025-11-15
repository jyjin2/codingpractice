N = int(input())
top = list(map(int, input().split()))
ans = [0] * N
stack = []      # (index, height)

for i in range(N):
    while stack and top[i] >= stack[-1][1]:  # height
        stack.pop()     # no need
    if stack:
        ans[i] = stack[-1][0] + 1
    else:
        ans[i] = 0
    stack.append((i, top[i]))

print(*ans)
