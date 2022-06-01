# 입력을 받음
words = input()
# 시간을 계산할 변수 생성
seconds = 0

# 문자열의 길이 만큼 반복
for i in words:
    # 각 문자가 해당하는 경우에 추가되는 시간을 작성함
    if i == 'A' or i == 'B' or i == 'C':
        seconds += 3
    elif i == 'D' or i == 'E' or i == 'F':
        seconds += 4
    elif i == 'G' or i == 'H' or i == 'I':
        seconds += 5
    elif i == 'J' or i == 'K' or i == 'L':
        seconds += 6
    elif i == 'M' or i == 'N' or i == 'O':
        seconds += 7
    elif i == 'P' or i == 'Q' or i == 'R' or i == 'S':
        seconds += 8
    elif i == 'T' or i == 'U' or i == 'V':
        seconds += 9
    else:
        seconds += 10

print(seconds)
