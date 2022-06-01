# 입력을 두 변수에 나누어 담는다. 이 때 변수 타입은 str이다.
a, b = input().split()

# 문자열 slice를 이용해 뒤부터 출력한 값을 다른 변수에 저장한다.
sangsu_a = a[::-1]
sangsu_b = b[::-1]

# 두 값을 비교해 큰 값을 출력한다.
if sangsu_a > sangsu_b:
    print(sangsu_a)
else:
    print(sangsu_b)
