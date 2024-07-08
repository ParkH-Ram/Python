x = 2
y = 1



for x in range (2,10) :
    if ( x % 2 == 0) :
        for y in range (1,11,3) :
            print(x, 'x', y, '=', x * y)
            if (y==9) :
                print("---------------")
