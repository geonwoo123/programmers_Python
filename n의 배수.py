def solution(num, n):
    func = lambda num,n : 1 if num % n == 0 else 0
    return func(num, n)