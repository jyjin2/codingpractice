def solution(answers):
    answer=[]

    first = [1, 2, 3, 4, 5]
    second = [2,1,2,3,2,4,2,5]
    third = [3,3,1,1,2,2,4,4,5,5]
    
    result = [0,0,0]
    # see if they got right
    for i in range(len(answers)):
        if first[i % len(first)] == answers[i]:
            result[0] += 1
        if second[i % len(second)] == answers[i]:
            result[1] += 1
        if third[i % len(third)] == answers[i]:
            result[2] += 1
    
    for i in range(3):
        if result[i] == max(result):
            answer.append(i+1)
            
    return answer