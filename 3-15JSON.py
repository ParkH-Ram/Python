import requests
import json

domain_name = input('domain_name: ')
url = 'http://ip-api.com/json/' + domain_name

response = requests.get(url)
dict1 = json.loads(response.text)  # 딕셔너리 형태로 넣음
                                   # response는 .text로 데이터를 받아야 활용 가능

for i in sorted(dict1.keys()) :    # sorted로 임름 순으로 정렬
    print (i, ':', dict1[i])

#
