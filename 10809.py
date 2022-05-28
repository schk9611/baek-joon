# 내 풀이
# input값을 받음
strings = input()

# 비교할 알파벳 리스트를 만듦
alpa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
        'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# 반복문을 통해 알파벳 리스트를 돌고 반복문 안에서 조건문을 통해 일치하는 알파벳이 있으면 index 출력, 없으면 -1 출력
for chars in alpa:
    if chars in strings:
        print(strings.index(chars), end=' ')
    else:
        print('-1', end=' ')


# 다른 사람 풀이1
a = input()
# 리스트가 아닌 문자열 사용
x = 'abcdefghijklmnopqrstuvwxyz'

for i in x:
    # find 내장함수를 사용!
    if i in a:
        index = a.find(i)
        print(index)
    else:
        print('-1')
