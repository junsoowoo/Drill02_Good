from pico2d import*
import math
import os

os.chdir('D:\\2DGP\\Drill02')
grass= lode_image('grass.png')
character= lode_image('character.png')

open_canvas()

def run_circle():
    print('circle')
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(400,90)
    pass


def run_rectangle():
    print('rectangle')
    
    pass



while true:
    run_circle()
    run_rectangle()
    break



close_canvas


