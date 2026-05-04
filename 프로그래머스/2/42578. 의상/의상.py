def solution(clothes):
    answer = 1
    types = {}

    for c in clothes:
        if c[1] not in types:
            types[c[1]] = 1
        else:
            types[c[1]] += 1

    for t in types.values():
        answer *= (t+1)    # 안 입는 경우 +1
    
    return answer - 1   # 전부 안 입는 경우 -1