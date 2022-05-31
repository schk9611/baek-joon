# 처음 불러올 때 대문자로 만들어주고 리스트에 저장
users_list = list(input().upper())
# 중복되는 문자 제거를 위해 set 타입으로 저장
users_set = set(users_list)
# 문자와 반복 횟수를 저장할 dictionary 타입 생성
users_dict = {}

# 반복으로 dictionary에 문자와 반복횟수를 key와 value로 저장
for i in users_set:
    users_dict[i] = users_list.count(i)

# 리스트 컴프리헨션으로 중복횟수가 가장 큰 값을 리스트로 만들어 저장
result = [x for x, y in users_dict.items() if max(users_dict.values()) == y]

# 그렇게 리스트로 만들어진 값이 하나이면 그 값을 가진 문자를 출력 두개 이상이면 ?물음표 출력
if len(result) < 2:
    print(result[0])
else:
    print('?')
