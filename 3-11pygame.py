# 파이선 지렁이 게임
# 깃 연동 성공적
#연동 #삽질 #주석은나중에 #;;;

import pygame
import sys
import time
import random

from pygame.locals import *

WINDOW_WIDTH = 800                       #넓이 지정
WINDOW_HEIGHT = 600                      #높이 지정
GRID_SIZE =20                            #한칸을 20으로 큼직하게 나눈다? 
GRID_WIDTH = WINDOW_WIDTH / GRID_SIZE    #그리드로 나눴을 때 크기도 계산? 
GRID_HEIGHT = WINDOW_HEIGHT / GRID_SIZE 


WHITE = (255, 255, 255)  # RGB (16진수) 최대 밝은 색
GREEN = (0, 50, 0)
ORANGE = (55, 33, 22)

# x y 좌표 ... 왜 반대 인지 확인 모르겠음~~ 
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

FPS = 10

# Python 클래스 생성 
class Python(object):
    # 초기화? 
    def __init__(self):
        # 생성 
        self.create()
        # 초기화 색상 = 초록색
        self.color = GREEN

     #  create 메서드 정하기 초기화 된 뱀 생성   
    def create(self):
        self.length = 2
        # 위치들의 집합이니 positions로   전체 크기의 /2 하면 중앙
        self.positions = [((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2))]
        # 뱀이 랜덤으로 생성 
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

     # 움직임 
    def control(self, xy):
        # 왼쪽으로 가는 도중에 오른쪽으로 못가게...
        # 반대 방향으로 조작하는 것 방지
        # 변화를 주지 않겠
        if (xy[0] * -1, xy[1] * -1) == self.direction:
            return
        
        # self.direction이 제대로 가고 있다~ 그냥 이동~~ 
        else:
            self.direction = xy

    # 이동 설정 
    def move(self):
        # 뱀의 길이는 포지션 으로 이루어져 있고 포지션의 0인덱스는 뱀의 머리 
        cur = self.positions[0]
        x, y = self.direction

        #현재위치의 0번째, x축에다 GRID_SIZE를 곱하고
        # cur의 첫번째에 y를 곱하고...
        # 움직이는 순간에 화면이 넘어 갈 때 사라지거나 끝나지 않고 반대쪽으로 나올 수 있게 해주는 
        new = ((cur[0] + (x * GRID_SIZE)) % WINDOW_WIDTH , (cur[1] + (y * GRID_SIZE)) % WINDOW_HEIGHT)

        # 새로 생긴 뱀이 꼬리에 닿으면 디진다  , // create로 새로 시
        if new in self.positions[2:]:
            self.create()
        else:

            # 아니면 새로 만들었던 
            self.positions.insert(0, new)
            # 포지션즈보다 길이가 커진다 
            if len(self.positions) > self.length:
                # 포지션즈 에서 하나를 꺼낸다 ?
                self.positions.pop()

    # 먹이를 먹으면 뱀의 길이가 1 증가
    def eat(self):
        self.length += 1

    # 뱀이 화면에 표시될 수 있게 그리기 
    def draw(self, surface):
        for p in self.positions:
            draw_object(surface, self.color, p)

class Feed(object):
    def __init__(self):
        self.position = (0, 0)
        self.color = ORANGE
        self.create()

    def create(self):
        self.position = (random.randint(0, GRID_WIDTH -1) * GRID_SIZE, random.randint(0, GRID_HEIGHT -1) * GRID_SIZE)

    def draw(self, surface):
        draw_object(surface, self.color, self.position)

        
# 그리드로 창을 표시 해놨는데...             
def draw_object(surface, color, pos):
    
    r = pygame.Rect((pos[0], pos[1]),(GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(surface, color, r)
        
def check_eat(python, feed):
    if python.positions[0] == feed.position:
        python.eat()
        feed.create()


# 메인.. 생성?
if __name__ == '__main__':
    python = Python()   # 파이썬에서 객체 생성 하는 방법
    feed = Feed()       # python 객체를 = Python() 클래스에서 받아서 만든
    
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
    pygame.display.set_caption('Python Game')           # 캡션 이름 지정 
    surface = pygame.Surface(window.get_size())         # 창위에다 게임적인 요소를 하기 위해  아 표면 공간? 그걸 화면 크기 지정한 걸 가져오는 
    surface = surface.convert()                         # surface를 컨버터 해줌, 변화??  적용 시킨다? 
    surface.fill(WHITE)                                 # 실제 표면 색상? white로 지정 
    clock = pygame.time.Clock()                         # 게임이니까 시간을 이용 한다 ? 
    pygame.key.set_repeat(1, 40)                        # 키의 repeat 정도?
    window.blit(surface, (0, 0))                        # 비트연산으로 화면 구성? 


    #뱀을 조작
    while True:

        #계속 반
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    python.control(UP)
                elif event.key == K_DOWN:
                    python.control(DOWN)
                elif event.key == K_LEFT:
                    python.control(LEFT)
                elif event.key == K_RIGHT:
                    python.control(RIGHT)

        #화면을 하얀색으로 칠해주
        surface.fill(WHITE)
        python.move()
        check_eat(python, feed)
        # python 의 길이  / 2 만큼 속도가 빨라지게 하기 위해
        speed = (FPS + python.length) / 2
        python.draw(surface)
        feed.draw(surface)
        window.blit(surface, (0, 0))
        pygame.display.flip()
        pygame.display.update()
        clock.tick(speed)
