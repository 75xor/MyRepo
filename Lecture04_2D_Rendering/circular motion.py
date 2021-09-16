
import math

from pico2d import*
open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x=400
y=90
a=0
while a<360:
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    a+=5
    x+=20*math.cos(a/360*2* math.pi)
    y+=20*math.sin(a/360*2* math.pi)
    delay(0.01)



close_canvas()   
