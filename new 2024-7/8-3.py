# a = [1,2,'hello', ['a','b','c','d']]


# print(a[3])


# print(a[3][2])

# print(a[2][4])

# print(a[0:4])

# print(a[0::2])

# print(a[::2])

# print(a[2:3])

# a = [1, 2, 3]
# b = [5, 6, 7]

# print(a+b)

# print(len(a))

a = ['a', 'b', 'd', 'f','s','g']
print(a)
a.sort()
print(a)
a.reverse()
print(a) 

a.insert(1, '5') # 인덱스 번호에 삽입 하겠다.

print(a)

a.remove('5')

print(a)

a.pop() # 인덱스 번호를 안적으면 마지막걸 내 뱉는다

print(a)

print(a.pop(4))  # 인덱스 번호를 적으면 해당 인덱스 번호의 값을 뱉어 낸다.


print(a)


# extend (인덱스로 추가 ( 펼쳐져서 추가 됨 ))
# append (그대로 추가)

a.extend([4,5])

print(a)

a.append([4,5])

print(a)