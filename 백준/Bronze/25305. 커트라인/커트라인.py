import sys
input = sys.stdin.readline

n, k = map(int, input().split())
grades = list(map(int, input().split()))

desc_grades = sorted(grades, reverse=True)

print(desc_grades[k-1])