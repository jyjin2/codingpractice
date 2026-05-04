def solution(nums):
    answer = 0
    canTake = len(nums)//2
    breed = set(nums)
    
    if canTake <= len(breed):
        answer = canTake
    else:
        answer = len(breed)
    return answer