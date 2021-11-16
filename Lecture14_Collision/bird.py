import game_framework
from pico2d import *
import game_world
from random import *



PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14



class Bird:
    image = None

    def __init__(self):
        if Bird.image == None:
            Bird.image = load_image('bird100x100x14.png')
        self.x, self.y = randint(0, 800),randint(400, 600)
        self.frame = 0
        self.velocity = 50
    def get_bb(self):
        # fill here
        return 0,0,0,0

    def draw(self):
        self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)
        # fill here for draw

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.x += self.velocity * game_framework.frame_time
        self.x = clamp(25, self.x, 1600 - 25)







