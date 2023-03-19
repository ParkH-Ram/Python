import requests
import json

domain_name = input('domain_name: ')
url = 'http://ip-api.com/json/' + domain_name
#
'''
웹에서 많이 사용하는 구조화 된 데이터
딕셔너리랑 완전히 같은 형태
'''

response = requests.get(url)
dict1 = json.loads(response.text)  # 딕셔너리 형태로 넣음
                                   # response는 .text로 데이터를 받아야 활용 가능
#lodas json을 딕셔너리 타입으로 바꿔줌

for i in sorted(dict1.keys()) :    # sorted로 임름 순으로 정렬
    print (i, ':', dict1[i])

#
