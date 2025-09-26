def solution(N, number):
    ans = -1	# 정답 (최솟값), 기본값 -1
    
    # 예외 처리: 둘이 같으면 한 번만 써도 끝
    if N == number:
        return 1
    
    # li[i] = N을 (i+1)번 써서 만들 수 있는 모든 수들의 집합
    # e.g. li[0] -> N 1개 쓴 경우, li[1] N 2개 쓴
    li = [set() for _ in range(8)]
    
    # 1  2   3   4    5     6     7   8 
    # 5  55  555 5555 55555 555555, ...
    
    # i starts from 0
    # 이어붙인 수 먼저 넣어줌
    # N=5 -> 5, 55, 555, ...
    for i in range(len(li)):
    	li[i].add(int(str(N)*(i+1)))
        
    # dp 진행. op로 새로운 수. ㅏㄴ들기
    for i in range(1, 8):	# li[0]은 N 하나만 쓴 경우라 연산 불필요
        for j in range(i):	# j + (i-j-1) = i-1 -> 전체 i개로 쪼개기
            for op1 in li[j]:	# 왼쪽 집합에서 하나 뽑고
                for op2 in li[i-j-1]:	# 오른쪽 집합에서 하나 뽑아서
                    # 사칙연산 적용
                    li[i].add(op1+op2)
                    li[i].add(op1-op2)
                    li[i].add(op1*op2)
                    if op2 != 0:	# 나눗셈. 분모가 0이 아니어야 함.
                        li[i].add(op1//op2)	# 정수 나눗셈이라 나머지 무지
        
        # 목표 number가 나오면 바로 정답
        if number in li[i]:
            ans = i+1	# li[i]는 N을 (i+1)번 사용했을 때
            break
                  
    return ans