from collections import deque

T = int(input())
for _ in range(T):
    # N = 문서 개수, M = 찾고자 하는 문서의 queue 순서
    N, M = map(int, input().split())
    pri = list(map(int, input().split()))
    cnt = 0
    dq = deque()

    for i, j in enumerate(pri):
        dq.append((i, j))

    # pri = [1 1 1 1 1 9]
    pri.sort()

    while dq:
        i, j = dq.popleft()
        if j == pri[-1]:    # 중요도가 가장 높을 때
            cnt += 1
            pri.pop()
            if i == M:
                print(cnt)
                break
        else:
            dq.append((i, j))

