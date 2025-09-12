def solution(num_list):
    num_sum = (sum(num_list)) ** 2
    num_mul = 1
    for i in num_list:
        num_mul *= i
    func = lambda num_sum, num_mul : 1 if num_mul < num_sum else 0    
    return func(num_sum, num_mul)