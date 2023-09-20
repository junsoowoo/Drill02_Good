from pico2d import*
import math
import os

os.chdir('D:\\2DGP\\Drill02')
open_canvas()
grass=load_image('grass.png')
character=load_image('character.png')



def render_All(x,y):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    delay(0.01)
    
def run_circle():
    print('circle')
    
    delay(1)
    
    cx,cy,r=800/2,600/2,200
    for deg in range(0,360,5):
        x= cx+r*math.cos(deg/360*2*math.pi)
        y= cy+r*math.sin(deg/360*2*math.pi)
        render_All(x,y)


def run_rectangle():
    print('rectangle')

    #bottom line
    for x in range(50,750+1,10):
        render_All(x,90)
    #right line
    for y in range(90,610+1,10):
        render_All(750,y)
    #top line
    for x in range(750,50-1,-10):
        render_All(x,750)
    #left line   
    for y in range(610,90-1,-10):
        render_All(50,y)


while(True):
    run_circle()
    run_rectangle()
    break



close_canvas


