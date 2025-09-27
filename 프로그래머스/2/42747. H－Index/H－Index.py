def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def solution(citations):
    # h번 이상 인용된 논문이 h편 이상
    # 나머지 논문이 h번 이하 인용되었다면 h의 최댓값
    # 3편의 논문은 3회 이상 인용
    # citations.sort(reverse=True)
    citations = bubble_sort(citations)
    print(citations)
    # i=0 시작, i+1편이 (i+1)회 이상 인용되었는지 확인
    h = 0
    for i, c in enumerate(citations):
        if c >= i+1:
            h = i+1
        else:
            break
    return h