t1 = ()
t2 = (1,)
t3 = (1,2,3)
t4 = 1,2,3

## 튜플 값은 변경 불가


print(t4[1:])

# 튜플 = 값 변경 불가
# 리스트 = 값 변경 가능 ( 배열 이라 생각 )

t5 = t4 * 20

print(len(t5))