from collections import Counter

def solution(points, routes):
    # points : 각 포인트의 위치 (1번 포인트 -> points[0])
    # routes : 로봇들의 경로 (e.g. routes[i] = [4,2] -> i+1번 로봇이 4번에서 2번으로)
    
    def bfs(route):
        # 시간 역할
        idx = 0
        # 로봇이 지나간 (x, y, 시간)을 기록하는 리스트
        path = []
        
        for i in range(len(route) - 1):
            # route[i], route[i+1] : 현재 포인트 -> 다음 포인트 번호
            # spots[번호-1] : 실제 좌표 (포인트 번호는 1부터 시작하니까 -1)
            # 출발 좌표 (sx, sy)에서 다음 포인트 좌표 (ex, ey)로 이동 시뮬레이션
            sx, sy = spots[route[i]-1]
            dx, dy = spots[route[i+1]-1]
            
            # x좌표 (r) 먼저 맞추기
            while sx != dx:
                # x 좌표가 다르면 한 칸씩 움직임
                # path에 (현재x, 현재y, 현재시간)을 넣고
                # x를 이동시키고 idx(시간) 증가
                path.append((sx, sy, idx))  # 현재 좌표 + 시간 기록
                if sx < dx:
                    sx += 1
                else:
                    sx -= 1
                idx += 1
            # y좌표 (c) 맞추기
            while sy != dy:
                # x 좌표가 다 맞춘 뒤 y좌표
                # 규칙대로 r->c 순서
                path.append((sx, sy, idx))  # 현재 좌표 + 시간 기록
                if sy < dy:
                    sy += 1
                else:
                    sy -= 1
                idx += 1
        # 목적지 좌표에 도착했을 때 시간 기록
        path.append((sx, sy, idx))
        return path
            
    #모든 로봇 경로 합치기
    spots = [i for i in points]
    total = []
            
    for route in routes:
        total.extend(bfs(route))
        
    danger = 0
    temp = Counter(total)
    for i in temp.values():
        if i >= 2:
            danger += 1
    return danger