def solution(enroll, referral, seller, amount):
    # 각 판매원의 이익을 저장할 배열 (enroll 순서대로)
    profit = [0 for _ in range(len(enroll))]
    
    # 판매원 이름 -> 인덱스 번호 매핑
    dict = {name: i for i, name in enumerate(enroll)}
    
    # 판매 기록(seller, amount)을 하나씩 처리
    for s, a in zip(seller, amount):
        money = a * 100		# 칫솔 1개당 100원
        
        # 추천 체인을 따라 위로 분배 시작
        while s != '-' and money > 0:
            idx = dict[s]	# 현재 판매원의 인덱스
            # 내가 가져가는 금액 = 전체 - (10% 올릴 몫)
            profit[idx] += money - money//10
            
            # 다음 단계로 넘길 돈 = 전체의 10% (원단위 절사)
            money //= 10
            
            # 추천인으로 이동
            s = referral[idx]
            
    return profit