from pico2d import *
import math

open_canvas()

character=load_image('character.png')
grass=load_image('grass.png')

def render_frame(x, y): # x,y 위치에 캐릭터를 그려줄 수 있는 함수
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    delay(0.01)

def run_circle():
    print('CIRCLE')

    cx, cy, r=400, 300, 200
    for deg in range(0, 360, 5):
        x=cx+r*math.cos(math.radians(deg))
        y=cy+r*math.sin(math.radians(deg))
        render_frame(x, y)

def run_rectangle():
    print('RECTANGLE')

    # bottom
    for x in range(50, 750+1, 5):
        render_frame(x, 90)

    # right
    for y in range(90, 550+1, 5):
        render_frame(750, y)

    # top
    for x in range(750, 50-1, -5):
        render_frame(x, 550)

    # left
    for y in range(550, 90-1, -5):
        render_frame(50, y)     

while True:
    run_circle()
    run_rectangle()

close_canvas()
