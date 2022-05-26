# 내 풀이
# 두 개의 값을 받지만 첫 번째 값은 제 풀이에 사용하지 않아 받기만 하고 두 번째 값은 for문을 통해 풀어낼 생각이라 str 형변환하였습니다.
a = int(input())
b = str(input())
# sums 변수를 미리 정의
sums = 0

# 반복을 통해 첫 인덱스부터 하나하나 i에 받고 int로 형변환하여 더해줌
for i in b:
    sums = sums + int(i)

print(sums)
