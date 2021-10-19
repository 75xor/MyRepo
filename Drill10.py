from pico2d import *
import random
# Game object class here
class Grass:
    def __init__(self):
        self.image =load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)
    pass
class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100,700),90
        self.frame =random.randint(0,7)
        self.image=load_image('run_animation.png')
    def update(self):
        self.frame = (self.frame+1)%8
        self.x+=5
    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)

class Ball_small:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599
        self.speed = random.randint(0, 10)
        self.image = load_image('ball21x21.png')

    def update(self):
        if self.y <= 30: speed =0
        self.y -= self.speed

    def draw(self):
        self.image.draw(self.x, self.y)

class Ball_big:
    def __init__(self):
        self.x, self.y = random.randint(0, 800), 599
        self.speed = random.randint(0, 10)
        self.image = load_image('ball41x41.png')
    def update(self):
        if self.y <= 35: speed =0
        self.y -= self.speed

    def draw(self):
        self.image.draw(self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False



open_canvas()
boy=Boy()
grass=Grass()
small_ball=Ball_small()
big_ball=Ball_big()
team =[Boy() for i in range(11)]
i =(random.randint(10, 15))
small_ballbox = [Ball_small() for a in range(i)]
big_ballbox = [Ball_big() for u in range(20-i)]
bc = []
running=True

while running:
    handle_events()
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.update()
        boy.draw()
    for small_ball in small_ballbox:
        small_ball.update()
        small_ball.draw()
    for big_ball in big_ballbox:
        big_ball.update()
        big_ball.draw()

    update_canvas()
    delay(0.05)

close_canvas()