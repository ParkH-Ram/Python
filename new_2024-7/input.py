x = 2
y = 1



for x in range (2,10) :
    if ( x % 2 == 0) :
        for y in range (1,11,3) :
            print(x, 'x', y, '=', x * y)
            if (y==9) :
                print("---------------")


numbers = input("숫자 4개를 공백으로 구분해서 넣어 주세요.")
a, b, c, d = numbers.split(' ')

e = int(a) + int(b) + int(c) +int(d) 

print("{}, {}, {}, {}의 합은 {}이다" .format(a, b, c, d, e))



#1번 문제
print('''\
    *
   *  *
 *      *
**********\

''')


#2번 문제
a = int(input("a : "))
b = int(input("b : "))
print(" a + b = {}" .format(a + b))
