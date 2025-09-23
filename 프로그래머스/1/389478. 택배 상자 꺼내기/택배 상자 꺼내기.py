def solution(n, w, num):
    # 상자의 위치 찾기
    row = (num-1) // w
    pos = (num-1) % w
    col = pos if row % 2 == 0 else w - 1 - pos
        
    # 위 col에서 해당 row에 상자가 존재하는지 세기 (자기 자신 포함)
    import math
    R = math.ceil(n/w)	# R = (n+w-1) // w
    count = 0
    for r in range(row, R):
        #해당 col의 실제 상자 개수
        if r == R-1:
            len_row = n - r*w
        else:
            len_row = w
        
        if r % 2 == 0:
            exists = (col < len_row)
        else:
            exists = (col >= w - len_row)
            
        if exists:
            count += 1
            
    return count