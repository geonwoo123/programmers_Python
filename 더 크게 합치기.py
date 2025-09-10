def solution(a, b):
    a_b_sum = str(a) + str(b)
    b_a_sum = str(b) + str(a)
    if int(a_b_sum) > int(b_a_sum):
        return int(a_b_sum)
    else:
        return int(b_a_sum)