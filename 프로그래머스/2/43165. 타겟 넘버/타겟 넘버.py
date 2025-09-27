def solution(numbers, target):
    way = 0		# 경우의 수
    n = len(numbers)	
    
    def dfs(i, curr_sum):	# i: 현재 번째 숫자
        nonlocal way
        if i == n:		# 모든 숫자를 다 사용했을때
            if curr_sum == target:
                way += 1
            return
        
        # i번째 숫자를 +로 더하는 경우
        dfs(i+1, curr_sum + numbers[i])
        # i번째 숫자를 -로 빼는 경우
        dfs(i+1, curr_sum - numbers[i])
        
    dfs(0, 0)	# 처음엔 0번째 숫자, 합=0에서 시작
    return way