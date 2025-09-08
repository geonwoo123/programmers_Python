str = input()
answer = ""
for i in str:
    if i.isupper():
        answer += i.lower()
    else:
        answer += i.upper()
print(answer)        
        
#대문자인지 판별: 변수.isupper()
#소문자인지 판별: 변수.islower()
#소문자 -> 대문자 변환: 변수.upper()
#대문자 -> 소문자 변환: 변수.lower()         