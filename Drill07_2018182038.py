from pico2d import *
from random import *
KPU_WIDTH, KPU_HEIGHT = 1280, 700

def randomPos():
    global mx, my
    mx, my = randrange(0, KPU_WIDTH), randrange(0, KPU_HEIGHT)
    pass

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
             running = False
    pass

open_canvas(KPU_WIDTH,KPU_HEIGHT)


kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
mouse = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
mx, my = randrange(0, KPU_WIDTH), randrange(0, KPU_HEIGHT)
frame = 0
hide_cursor()
d = 1 #0 l 1 r

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT//2)
    mouse.draw(mx, my)
    character.clip_draw(frame * 100, 100*d, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
   
    # a = (my - y) / (mx - x)
    # b = y - x * a
    if mx > x:
        x += 2
        d = 1
        # y = a * +b
    else:
        x -= 2
        # y = a * +b
        d = 0
    if my > y:
        y += 2

    else:
        y -= 2


    if(x >= mx-5 and x <= mx+5 and y >= my-5 and y <= my+5):
        randomPos()
    handle_events()

close_canvas()




