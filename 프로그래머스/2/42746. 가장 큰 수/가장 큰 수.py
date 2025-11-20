def solution(numbers):  
    # 숫자를 문자열로 변환
    strr = list(map(str, numbers))
    # 문자열을 3번 반복해서 비교
    # 원소는 최대 1000이므로 문자열 길이 최대 4자리
    # reverse =True 내림차순으로 정렬
    strr.sort(key=lambda x: x*3, reverse=True)
    # 모든 원소가 '0'일 경우 '000...'이 아닌 '0' 반환
    return '0' if strr[0] == '0' else ''.join(strr)