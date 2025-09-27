def solution(n, computers):
    cnt = 0
    visited = [False] * n
    
    def dfs(idx):
        visited[idx] = True
        for j in range(n):
            if not visited[j] and computers[idx][j] == 1:
                dfs(j)
    for i in range(n):
        if not visited[i]:
            dfs(i)
            cnt += 1
    return cnt