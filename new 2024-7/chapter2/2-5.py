dic = {'name' : 'ram', 'tall' : '187'}


## 새로운 값 추가
     # key             #vlaue
dic['라이징 스타'] =  '이름이 뭐지?'


dic[4] = (1,2,3)


## 삭제 
del(dic[4])  ## key를 선택해 삭제

print(dic)

## 여러값 삭제
#del dic['name'], dic['tall']

print(dic)


print(dic['name'])
print(dic['tall'])

## dic.keys() ->> 키들만 dict 형태로 만들어 주는 함수
print(dic.keys())

for k in dic.keys() : 
  print(k)