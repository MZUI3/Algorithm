def solution(number, n, m):
    answer = 1
    if  (number % n):
        answer = 0
    if  (number % m):
        answer = 0
    return answer