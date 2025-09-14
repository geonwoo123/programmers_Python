def solution(numLog):
    answer = ''
    for i in range(0,len(numLog)-1):
        dif = numLog[i+1] - numLog[i]
        if dif == 1:
            answer += 'w'
        elif dif == -1:
            answer += 's'
        elif dif == 10:
            answer += 'd'
        else:
            answer += 'a'
    return answer