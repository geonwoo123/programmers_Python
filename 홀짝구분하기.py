a = int(input())
if a % 2 == 0:
    print(f"{a} is even")
else:
    print(f"{a} is odd")

func = lambda x : f"{a} is even" if x % 2 == 0 else f"{a} is odd"
print(func(100))