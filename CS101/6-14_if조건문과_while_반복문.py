# ----- 6월 14일 if while문

#   로봇이 움직일 수 있는 윈도우 창
from cs1robots import *
load_world("worlds/amazing2.wld")
#edit_world()
#save_world("worlds/new_world.wld")
#create_world()

# create a robot with one beeper
hubo = Robot(beepers =1)

def move_or_turn():
    if hubo.front_is_clear(): # 앞이 깨끗하면
        hubo.move()           # 움직여
    else :
        hubo.turn_left()        # 왼쪽으로 회전



hubo.drop_beeper() # 드랍 비퍼

while not hubo.on_beeper():  # 휴보가 비퍼 위에 있지 않을 때
    if hubo.front_is_clear():    # 앞이 깨끗 하면
        hubo.move()   # 움직여
    else:
        hubo.turn_left()  

    


#hubo = Robot() 코드 아랫줄에

#hubo.set_trace("blue") 코드를 추가해 보십시


        

        

    

        







