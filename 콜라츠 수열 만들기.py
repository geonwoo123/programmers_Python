def solution(n):
    answer = []
    while True:
        if n % 2 == 0:
            answer.append(n)
            n /= 2
        elif n == 1:
            answer.append(1)
            break
        else:
            answer.append(n)
            n = 3 * n + 1
            
    return answer