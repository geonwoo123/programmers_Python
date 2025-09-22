def solution(a, b, c, d):
    dice = [a, b, c, d]
    
    if len(set(dice)) == 1:
        return 1111 * a
    
    elif a==b and b==c and c!=d: return (10 * a + d)**2
    elif a==b and b==d and d!=c: return (10 * a + c)**2
    elif a==c and c==d and d!=b: return (10 * a + b)**2
    elif b==c and c==d and d!=a: return (10 * b + a)**2

    elif a==b and b!=c and c==d: return (a + d) * abs(a - d)
    elif a==c and c!=b and b==d: return (a + d) * abs(a - d)
    elif a==d and d!=b and b==c: return (a + c) * abs(a - c)

    elif a==b and a!=c and a!=d and c!=d: return c * d
    elif a==c and a!=b and a!=d and b!=d: return b * d
    elif a==d and a!=b and a!=c and b!=c: return b * c
    elif b==c and b!=a and b!=d and a!=d: return a * d
    elif b==d and b!=a and b!=c and a!=d: return a * c
    elif c==d and c!=a and c!=b and a!=b: return a * b


    if len(set(dice)) == 4:
        return min(dice)