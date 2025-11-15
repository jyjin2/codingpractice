from collections import deque

n = int(input())
# [1, 2, 3, 4, 5, 6]
# cards = [ i+1 for i in range(n) ]
q = deque( i+1 for i in range(n) )

# for i in range(n):
#     q.append(cards[i])
while len(q) > 1:
    q.popleft()     # 맨 위 버리기
    q.append(q.popleft())   # 맨 뒤로 옮기기

print(q[0])