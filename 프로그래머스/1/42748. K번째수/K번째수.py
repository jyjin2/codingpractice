def solution(array, commands):
    answer = []
    for i, j, k in commands:
        # i-1부터 j까지 (j 포함 x)
        arr = sorted(array[i-1:j])
        # k번째 수 구하기
        answer.append(arr[k-1])
    return answer