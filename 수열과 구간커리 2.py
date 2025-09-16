def solution(arr, queries):
    answer = []
    for i in range(len(queries)):
        min_check = []
        for j in range(queries[i][0],queries[i][1]+1):
            if arr[j] > queries[i][2]:
                min_check.append(arr[j])
        if not min_check:
            answer.append(-1)
        else:
            answer.append(min(min_check))        
    return answer