def solution(a, b):
    func = lambda a,b : int(str(a) + str(b)) if int(str(a) + str(b)) >= 2 * a * b else 2 * a * b
    return func(a,b)

    #if int(str(a) + str(b)) >= 2 * a * b:
    #    return int(str(a) + str(b))
    #else:
    #    return 2 * a * b