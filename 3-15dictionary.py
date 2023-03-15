# Dictionary   // 사전

# Dictionary 선언 
data = {'김영수': {'영어': 80, '수학': 90},
    	'최희수': {'영어': 70, '국어': 100}}
print(data['김영수'])
data['김영수']
data['김영수']['국어'] = 50    # 점수 추가도 가능
print('국어 추가 후', data['김영수'])

# 각 항에 value update 가능
#  data['김영수']['영어']  =  value  < update

data2 = {1 : 'a', 2: 'b'}   # key 1 'a' index
#data[1]  <<  값으로 서칭 불가
#data["key 입력 "] 하면 value 가 출력 됨

for i in data.keys():
    print(i, ':', data[i])   # 자바 foreach 랑 비슷 
for i in range(1,4):    # 범위 출력
    print(i)


#
"""
딕셔너리 연습 문제
다음 표를 토대로 dict b를 만들고 다음을 구현하라
 - dict b 에서 name 데이터를 찾아라
 - dict b 에서 bith데이터를 101010 으로 바꿔라
 - dict b 에서 key가 city이고 value가 Seoul인 데이터를 추가하라
"""

b = {'name' : {'John'},
     'phone' : {'01012345432'},
     'email' : {'test@test.com'},
     'birth' : {111111}}
for s in b.keys():
    print(s, ':', b[s])  # 출력
print('name 의 value는 : ', b['name'])
b['birth']=101010
print('birth를 101010으로 교체 birth : ', b['birth'])
# 없는걸 새로 만들어서 넣는 법
b['city'] = 'Seoul'     # 변수명 [key] = value  로 추가
print(b)
# 삭제. del 변수명[key]  del은 key로 삭
del b['email']
print(b)

