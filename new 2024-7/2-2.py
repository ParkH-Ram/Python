number = 5

a = "I eat %.03f apples." % number

print(a)

# 최신 포맷팅

name = '드라이'

age = '비밀'

a = f'나의 이름은 {name} 입니다. 나이는 {age} 입니다.'

print(a)

age = 30

a = f'나는 내년이면 {age+ 5  }살이 된다.'
print(a)

a = f'{"hi":>10}'

print(a)


# 예시 사용
number = 1234567890
formatted_number = f"{number:,}"
print(formatted_number)  # 출력: 1,234,567,890