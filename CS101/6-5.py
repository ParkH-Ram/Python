# 파이썬 함수를 만들기 위해 def 를 만들어 주고 들여쓰기로 실행 부 구분
def print_message():
    print("안녕하세요 만나서 반갑습니다")
    print("초보지만 열심히 해봅시다")


def repeat_message():
    print_message()   # 함수 호출도 가능함
    print_message()  


#   로봇이 움직일 수 있는 윈도우 창
from cs1robots import *
create_world()

# create a robot with one beeper
hubo = Robot(beepers =1)

#move one step  forward
#hubo.move()

# turn left 90 degrees
#hubo.turn_left()


def turn_right():
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

# hubo동작 정의
#climb_up_four_stairs()
#hubo.drop_beeper()
#turn_around()
#climb_down_four_stairs()

def climb_up_one_stairs():
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.move()


def turn_around() :
    hubo.turn_left()
    hubo.turn_left()


def climb_up_four_stairs():
    climb_up_one_stairs()
    climb_up_one_stairs()
    climb_up_one_stairs()
    climb_up_one_stairs()

def start_robot() : 
    climb_up_four_stairs()
    hubo.drop_beeper()
    turn_around()
    climb_up_four_stairs()
    

# --- 6월 5일 추가

def dance() :
    for i in range(4):
        hubo.turn_left()

def move_or_turn() :
    if hubo.front_is_clear(): # 앞이 비어 있으면 전진
         dance()
         hubo.move()
    else :
         hubo.turn_left()        # 앞이 막혀 있으면 turnLeft
         hubo.drop_beeper()

#for i in range(20) :
    #move_or_turn()
        

def check_robot():
    if hubo.on_beeper():
        hubo.pick_beeper()

    elif hubo.front_is_clear():
         hubo.move()
    elif hubo.left_is_clear() :
         hubo.turn_left()
    elif hubo.right_is_clear() :
         turn_right()
    else :
         turn_around()

        







