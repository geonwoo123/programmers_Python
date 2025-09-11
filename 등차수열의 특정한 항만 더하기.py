def solution(a, d, included):
    stack = []
    for i in range(len(included)):
        stack.append(a)
        a += d
    answer = 0
    for i in range(len(included)):
        if included[i] == True:
            answer += stack[i]
    return answer        
            