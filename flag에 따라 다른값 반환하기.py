def solution(a, b, flag):
    func = lambda a,b,flag : a+b if flag == True else a-b
    answer = func(a,b,flag)
    return answer