def solution(diffs, times, limit):
    n = len(diffs)
    def can_solve(level):
        # 현재 숙련도에서 문제를 풀 수 있는가
        
        # 첫 퍼즐은 항상 성공 -> 무조건 times[0] 만큼 걸림.
        total = times[0]
        
        if total > limit:
            return False
        
        # 퍼즐 스캔
        for i in range(1, n):
            diff = diffs[i]
            time_cur = times[i]
            time_prev = times[i-1]
            
            if diff <= level: # 퍼즐 맞힘.
                total += time_cur
            else: # 퍼즐 (diff-level)번 틀림.
                # 실패할 때마다 time_cur + time_prev 걸림.
                # 마지막 성공에 time_cur 더함.
                total += (diff-level) * (time_cur + time_prev) + time_cur
            
            # 제한 시간 초과 -> 조기 종료
            if total > limit:
                return False
            
        return total <= limit
    
    # range. level은 양의 정수. 상한이 max(diffs)면 모든 퍼즐을 한 번에 맞힘
    low = 1
    high = max(diffs)
    
    # 이분 탐색 Binary Search
    while low < high:
        # 중간값 구하기
        mid = (low+high) // 2
        # 풀 수 있는지 
       	level = can_solve(mid)
       	
        # mid level로 가능하다면 더 작은 숙련도로도 되는지 확인해야 함.
        # 탐색 range를 [low, mid]로 변경
        if level:
            high = mid
        # mid level로 불가능하다면 더 높은 숙련도가 필요함.
        # 탐색 range를 [mid+1, high]로 변경.
        else:
            low = mid+1
    return low