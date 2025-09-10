def solution(number, n, m):
    func = lambda number, n ,m : 1 if number % n == 0 and number % m == 0 else 0
    return func(number, n ,m)