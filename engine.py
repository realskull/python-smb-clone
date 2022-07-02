__author__='Utkrist Karki,realskull'
__version__='v1'
__builddate__='2020/5/8'

# Python 3.7.7 , Pygame 1.9.6
# HELP v1 ENGINE, WRITTEN BY UTKRIST KARKI
#2D PLATFORMER SIDE SCROLLING ENGINE

'''
ENGINE FEATURES (AS OF BUILD DATE AND VERSION):
2D PERSPECTIVE
PLATFORMER SIDE SCROLLING ( BOTH X & Y )
OBJECT SYSTEM ( COINS MUSHROOM ETC )
ENEMIES SYSTEM
SIMPLE TILE MAP ( refer to map/readme.txt for info)
MULTIPLE LEVELS
'''

'''
MSG FROM DEV

This is my first take on a super mario bros clone and a working 2d platformer
engine for my future games. I will keep improving the engine and keep adding
new features and optimizations. The code can be a bit messy and I tried to
go a little bit towards object oriented route. This can be confusing for
beginners so,I tried to comment each and every line of the code how it works
and what it does. For Expeirenced verteran ones, You will find a lot
of bad programming practises and really stupid way of doing things.

Currently the game manages a 60fps lock and 200fps on a i5 2.9ghz cpu
pygame doesn't use any rendering backend (openGL,directX,vulcan etc) so,
gpu isn't used here. All the calculations are done by the cpu itself.

Game doesn't use too much memory. Currently only uses 37MB (which is still
a lot originL MARIO USED 2KB )
'''

import pygame,sys # pygame library and system library
from pygame.locals import * # Import all the modules of pygame.
import dumbmenu as dm # simple module to make a menu, cudn't make a menu so used a opensource module for that

a0xe3d = 0 # jpt variable

# Initialization phase.
######## WINDOW INITIALIZATION ##############################
pygame.init() # Initialization.

WINDOW_SIZE = (640,480) # Window size (X,Y) in pixels

screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # Make the window.

display = pygame.Surface((300,200)) # used as the surface for rendering, which is scaled

pygame.mixer.pre_init(44100, -16,2,512) # Initialize the sound controller with 44100hz freq, 16bit stero 512k buffer.

myfont = pygame.font.SysFont("retro", 15)


pygame.display.set_caption('[HELPx v1] [SuperMario]') # Set the window title.
###### PYGAME INITIALIZATION ################################
clock = pygame.time.Clock() # Set the clock timer.


########## Memory & Variable Initialization #################

#Image initialization.(many are just placeholder images)
# .convert() is used for greencast. ( white is removed)


player_img = pygame.image.load('player.png').convert()
player_img.set_colorkey((255,255,255))

big_flag_img = pygame.image.load('player.png').convert()
big_flag_img.set_colorkey((255,255,255))

small_flag_img = pygame.image.load('player_animations/small/flag/flag_0.png').convert()
small_flag_img.set_colorkey((255,255,255))

playerDead_img = pygame.image.load('player_animations/small/die/die_0.png').convert()
playerDead_img.set_colorkey((255,255,255))

mushroom_img = pygame.image.load('tiles/objects/mushroom/pop/pop_0.png').convert()
mushroom_img.set_colorkey((255,255,255))

flower_img = pygame.image.load('tiles/objects/flower/fpop/fpop_0.png').convert()
flower_img.set_colorkey((255,255,255))

bomber_img = pygame.image.load('tiles/objects/bomber/bomber_pop/bomber_pop_0.png').convert()
bomber_img.set_colorkey((255,255,255))

bomb_img = pygame.image.load('tiles/objects/bomb/bomb_0.png').convert()
bomb_img.set_colorkey((255,255,255))

explosion_img = pygame.image.load('tiles/objects/explosion/explosion_0.png').convert()
explosion_img.set_colorkey((255,255,255))

fireball_img = pygame.image.load('tiles/objects/fireball/fireball_0.png').convert()
fireball_img.set_colorkey((255,255,255))

coin_img = pygame.image.load('tiles/objects/coin/coin_0.png').convert()
coin_img.set_colorkey((255,255,255))

coin_bounce_img = pygame.image.load('tiles/objects/coin_bounce/coin_bounce_0.png').convert()
coin_bounce_img.set_colorkey((255,255,255))

flag_img = pygame.image.load('tiles/objects/flag.png').convert()
flag_img.set_colorkey((255,255,255))

brick_img = pygame.image.load('tiles/blocks/brick/brick/brick_0.png') 
broken_brick_img = pygame.image.load('tiles/blocks/broken.png')
block_img = pygame.image.load('tiles/blocks/block.png')

pipe0_img = pygame.image.load('tiles/pipes/pipe_0.png').convert()
pipe0_img.set_colorkey((255,255,255))
pipe1_img = pygame.image.load('tiles/pipes/pipe_1.png').convert()
pipe1_img.set_colorkey((255,255,255))
pipe2_img = pygame.image.load('tiles/pipes/pipe_2.png').convert()
pipe2_img.set_colorkey((255,255,255))

cloud0_img = pygame.image.load('tiles/background/cloud_0.png').convert()
cloud0_img.set_colorkey((255,255,255))
grass0_img = pygame.image.load('tiles/background/grass_0.png').convert()
grass0_img.set_colorkey((255,255,255))
hill0_img = pygame.image.load('tiles/background/hill_0.png').convert()
hill0_img.set_colorkey((255,255,255))
hill1_img = pygame.image.load('tiles/background/hill_1.png').convert()
hill1_img.set_colorkey((255,255,255))
castle0_img = pygame.image.load('tiles/background/castle_0.png').convert()
castle0_img.set_colorkey((255,255,255))

what_block_img = pygame.image.load('tiles/blocks/what/what_0.png').convert()
what_block_img.set_colorkey((255,255,255))

empty_what_block_img = pygame.image.load('tiles/blocks/empty.png')

goomba_img = pygame.image.load('tiles/enemy/goomba/goomba_run/goomba_run_0.png').convert()
goomba_img.set_colorkey((255,255,255))
koopa_img = pygame.image.load('tiles/enemy/koopa/koopa_run/koopa_run_0.png').convert()
koopa_img.set_colorkey((255,255,255))
#####################################################################################

#load game sounds

small_jump_sound = pygame.mixer.Sound('sounds/Jump_small.wav')
big_jump_sound = pygame.mixer.Sound('sounds/Jump_big.wav')
coin_sound = pygame.mixer.Sound('sounds/coin.ogg')
stomp_sound = pygame.mixer.Sound('sounds/stomp.wav')
bump_sound = pygame.mixer.Sound('sounds/bump.wav')
brick_break_sound = pygame.mixer.Sound('sounds/brick_break.wav')
die_sound = pygame.mixer.Sound('sounds/die.wav')
powerup_appear = pygame.mixer.Sound('sounds/powerup_appear.wav')
powerup = pygame.mixer.Sound('sounds/powerup.wav')
powerdown = pygame.mixer.Sound('sounds/powerdown.wav')
fireball_sound = pygame.mixer.Sound('sounds/fireball.ogg')
kick_sound = pygame.mixer.Sound('sounds/kick.ogg')
######################################################################################

pygame.mixer.music.load('music/main.ogg')  #load music from files
pygame.mixer.music.play() #play the loaded music


#RGB Tuples values.

blue = (146,244,255)
transparent = (255,255,255)
skyblue = (107,140,255)
red   = 255,  0,  0
green =   0,255,  0
blue  =   0,  0,255


#Game Variables.Almost all variables need to be reset for
#so a nextlevel boolean will be used to check for re-initialization


IsGameOver = False
blockinput = False

player_x = 96
player_y = 128
freeze_y = 0
speedMultiplier = 1
player_size = 'small'

coin_frame = 0
coin_action = 'coin'

score = 0
coins = 0

player_flash = False
beingsmall = False
beingbig = False
beingbomber = False
beingfire = False
moving_left = False
moving_right = False
isFreeFalling = False
isinvincible = False

NextLevel = False

scrollx = 0
scrolly = 0

true_scrollx = 0
true_scrolly = 0

level = 0

#level,scroll and game objects lists

levels = []
scroll = []
flags = []
game_map = []
coin_objects = []
what_blocks = []
empty_what_blocks = []
mushroom_blocks = []
mushrooms = []
flowers = []
fireballs = []
bombers = []
bombs = []
bricks = []
goombas = []
goombas_kill = []
koopas = []
koopas_kill = []
tile_rects_indexes = []
broken_bricks = []
Labels = []
labels_kill = []
coin_bounces = []
explosions = []
path = 'map'


air_timer = 0
vertical_momentum = 0


player_rect = pygame.rect.Rect(player_x,player_y,16,16) # player collision rectangle



#Game functions

def loadlevels(path): # create the list of playable levels
    level = 0
    while True:
        try:
            f = open(path + str(level) + '.txt','r')
            f.close()
            levels.append(path + str(level) + '.txt')
            level += 1
        except:
            break

def load_map(path): # load the game map according to level aray
    f = open(path)
    data = f.read()
    f.close()
    data = data.split('\n')
    gamemap = []
    for row in data:
        game_map.append(list(row))
    return game_map

global animation_frames
animation_frames = {} # anim dict

def load_animation(path,frame_durations): # Load animation and create a
    global animation_frames               # dictionary of images for each
    animation_name = path.split('/')[-1]  # animation types
    animation_frame_data = []
    n = 0 # counter
    for frame in frame_durations: # add same frame multiple given times
        animation_frame_id = animation_name + '_' + str(n) # load the name
        img_loc = path + '/' + animation_frame_id + '.png' # get location
        animation_image = pygame.image.load(img_loc).convert() # load file
        animation_image.set_colorkey((255,255,255))# make transparent
        animation_frames[animation_frame_id] = animation_image.copy() # copy array
        for i in range(frame):
            animation_frame_data.append(animation_frame_id)
        n += 1
    return animation_frame_data

def change_action(action_var,frame,new_value): #change animation
    if action_var != new_value:
        action_var = new_value
        frame = 0
    return action_var,frame


def collision_test(rect,tiles): # test collision between obj & tiles
    
    hit_list = []
    
    for tile in tiles:
        
        if rect.colliderect(tile):
            hit_list.append(tile)
            
    return hit_list

def move(rect,movement,tiles): # return dict for possible movement directions
    collision_types = {'top':False,'bottom':False,'right':False,'left':False}
    rect.x += movement[0]
    hit_list = collision_test(rect,tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True
    rect.y += movement[1]
    hit_list = collision_test(rect,tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect, collision_types

animation_database = {} # animation database dict

#Load player's animations
animation_database['bomberidle'] = load_animation('player_animations/bomber/bomberidle',[7])
animation_database['bomberrun'] = load_animation('player_animations/bomber/bomberrun',[7,7,7])
animation_database['bomberjump'] = load_animation('player_animations/bomber/bomberjump',[7])
animation_database['bomberdie'] = load_animation('player_animations/bomber/bomberdie',[7])

animation_database['firetobomber'] = load_animation('player_animations/bomber/firetobomber',[22,22])
animation_database['bombertofire'] = load_animation('player_animations/bomber/bombertofire',[22,22])

animation_database['fireidle'] = load_animation('player_animations/fire/fireidle',[7])
animation_database['firerun'] = load_animation('player_animations/fire/firerun',[7,7,7])
animation_database['firejump'] = load_animation('player_animations/fire/firejump',[7])
animation_database['firedie'] = load_animation('player_animations/fire/firedie',[7])

animation_database['bigtofire'] = load_animation('player_animations/fire/bigtofire',[22,22])
animation_database['firetobig'] = load_animation('player_animations/fire/firetobig',[22,22])

animation_database['bigrun'] = load_animation('player_animations/big/bigrun',[7,7,7])
animation_database['bigjump'] = load_animation('player_animations/big/bigjump',[7])
animation_database['bigdie'] = load_animation('player_animations/big/bigdie',[7])
animation_database['bigidle'] = load_animation('player_animations/big/bigidle',[7])
animation_database['big_to_small'] = load_animation('player_animations/big/big_to_small',[22,22])
animation_database['small_to_big'] = load_animation('player_animations/small/small_to_big',[22,22])
animation_database['smallrun'] = load_animation('player_animations/small/run',[7,7,7])
animation_database['smalljump'] = load_animation('player_animations/small/jump',[7])
animation_database['smalldie'] = load_animation('player_animations/small/die',[7])
animation_database['smallidle'] = load_animation('player_animations/small/idle',[7])
animation_database['smallflag'] = load_animation('player_animations/small/flag',[7])

#Load enemy's animations
animation_database['goomba_run'] = load_animation('tiles/enemy/goomba/goomba_run',[7,7])
animation_database['goomba_die'] = load_animation('tiles/enemy/goomba/goomba_die',[7])
animation_database['koopa_run'] = load_animation('tiles/enemy/koopa/koopa_run',[7,7])
animation_database['koopa_die'] = load_animation('tiles/enemy/koopa/koopa_die',[7])

#Load object animations
animation_database['what'] = load_animation('tiles/blocks/what',[14,14,14,14])
animation_database['brick'] = load_animation('tiles/blocks/brick/brick',[4,4,4,4,4,4,4])
animation_database['brick_idle'] = load_animation('tiles/blocks/brick/brick_idle',[7])
animation_database['fireball'] = load_animation('tiles/objects/fireball',[7,7,7,7])
#Load consumables animations
animation_database['coin'] = load_animation('tiles/objects/coin',[7,7,7,7,7])
animation_database['coin_bounce'] = load_animation('tiles/objects/coin_bounce',[2,2,2,2,2,2,2,2])
animation_database['pop'] = load_animation('tiles/objects/mushroom/pop',[7,7,7,7])
animation_database['mushroom'] = load_animation('tiles/objects/mushroom',[7])
animation_database['flower'] = load_animation('tiles/objects/flower/flower',[7,7,7,7])
animation_database['fpop'] = load_animation('tiles/objects/flower/fpop',[7,7,7,7,7])
animation_database['bomber_pop'] = load_animation('tiles/objects/bomber/bomber_pop',[7,7,7,7])
animation_database['bomber'] = load_animation('tiles/objects/bomber/bomber',[7,7,7,7])
animation_database['bomb'] = load_animation('tiles/objects/bomb',[7,7,7,7])
animation_database['explosion'] = load_animation('tiles/objects/explosion',[2,2,3,3,4,4,4,4])

global player_action
global player_frame
player_action = 'idle' # Player current action
player_frame = 0 # Player frame
player_flip = False # Flip player?


def gameOver(): # Play dying animation
    global player_action
    global player_frame
    player_action,player_frame = change_action(player_action,player_frame,'smalldie')




############################################################
    
#Classes of objects,consumables and enemies.
#I might improve this by including sub-classes.
    
class Flag():
    def __init__(self, loc):
        self.loc = loc

    def render(self, surf):
        surf.blit(flag_img, (self.loc[0] - scroll[0], self.loc[1] - scroll[1]))

    def get_rect(self):
        return pygame.Rect(self.loc[0], self.loc[1], 16, 168)

    def collision_test(self, rect):
        flag_rect = self.get_rect()
        return flag_rect.colliderect(rect)
    
class Coin_obj():
    def __init__(self, loc):
        self.loc = loc

    def render(self, surf):
        surf.blit(coin_img, (self.loc[0] - scroll[0], self.loc[1] - scroll[1]))

    def get_rect(self):
        return pygame.Rect(self.loc[0], self.loc[1], 16, 16)

    def collision_test(self, rect):
        coin_rect = self.get_rect()
        return coin_rect.colliderect(rect)

class Coin_bounce():
    def __init__(self, loc):
        self.loc = [loc[0],loc[1]-16]
        self.frame = 0
        self.img = coin_bounce_img
        self.img_id = 0
        self.action = 'coin_bounce'
        self.justcreated = True
        self.frameloops = 0

    def render(self, surf):
        surf.blit(self.img, (self.loc[0] - scroll[0], self.loc[1] - scroll[1]))

    def get_rect(self):
        return pygame.Rect(self.loc[0], self.loc[1], 16, 16)

    def collision_test(self, rect):
        coin_rect = self.get_rect()
        return coin_rect.colliderect(rect)
    
    def animate(self, coin_action):
        print(self.frameloops)
        if self.frame >= len(animation_database[coin_action]):
            self.frame = 0
            self.justcreated = False
            self.frameloops += 1
        self.img_id = animation_database[coin_action][self.frame]
        self.img = animation_frames[self.img_id]
        self.frame += 1

class Mushroom():
    def __init__(self, loc):
        self.loc = [loc[0],loc[1]-16]
        self.img_id = 0
        self.img = mushroom_img
        self.frame = 0
        self.justcreated = True
        self.movement =  [0,0]
        self.direction = 'right'
        self.isAlive = True
        self.vertical_momentum = 3
        self.movementSpeed = 0.5        
        self.collision_types = {'top':False,'bottom':False,'right':False,'left':False}
        self.rect = self.get_rect()

    def render(self, surf):
        self.loc[0] = self.rect.x
        self.loc[1] = self.rect.y
        surf.blit(self.img, (self.loc[0] - scroll[0], self.loc[1] - scroll[1]))

    def get_rect(self):
        return pygame.Rect(self.loc[0], self.loc[1], 16, 16)
    
    def collision_test(self, rect):
        mushroom_rect = self.get_rect()
        return mushroom_rect.colliderect(rect)
    
    def animate(self, mushroom_action):
        if self.frame >= len(animation_database[mushroom_action]):
            self.frame = 0
            self.justcreated = False
        self.img_id = animation_database[mushroom_action][self.frame]
        self.img = animation_frames[self.img_id]
        self.frame += 1
    
    def move(self):
        self.movement = [0,0]
        if self.direction == 'left' and self.isAlive:
            self.movement[0] -= 1
        if self.direction == 'right' and self.isAlive:
            self.movement[0] += 1
            
        mushroom.movement[1] += mushroom.vertical_momentum
        mushroom.vertical_momentum += 0.2
        if mushroom.vertical_momentum > 3:
            mushroom.vertical_momentum = 3

class Flower():
    def __init__(self, loc):
        self.loc = [loc[0],loc[1]-16]
        self.img_id = 0
        self.img = flower_img
        self.frame = 0
        self.justcreated = True
        self.isAlive = True     
        self.rect = self.get_rect()

    def render(self, surf):
        surf.blit(self.img, (self.loc[0] - scroll[0], self.loc[1] - scroll[1]))

    def get_rect(self):
        return pygame.Rect(self.loc[0], self.loc[1], 16, 16)
    
    def collision_test(self, rect):
        flower_rect = self.get_rect()
        return flower_rect.colliderect(rect)
    
    def animate(self, flower_action):        
        if self.frame >= len(animation_database[flower_action]):
            self.frame = 0
            self.justcreated = False
        self.img_id = animation_database[flower_action][self.frame]
        self.img = animation_frames[self.img_id]
        self.frame += 1

class Bomber():
    def __init__(self, loc):
        self.loc = [loc[0],loc[1]-16]
        self.img_id = 0
        self.img = bomber_img
        self.frame = 0
        self.justcreated = True
        self.isAlive = True     
        self.rect = self.get_rect()

    def render(self, surf):
        surf.blit(self.img, (self.loc[0] - scroll[0], self.loc[1] - scroll[1]))

    def get_rect(self):
        return pygame.Rect(self.loc[0], self.loc[1], 16, 16)
    
    def collision_test(self, rect):
        bomber_rect = self.get_rect()
        return bomber_rect.colliderect(rect)
    
    def animate(self, bomber_action):        
        if self.frame >= len(animation_database[bomber_action]):
            self.frame = 0
            self.justcreated = False
        self.img_id = animation_database[bomber_action][self.frame]
        self.img = animation_frames[self.img_id]
        self.frame += 1
        
class Explosion():
    def __init__(self, loc):
        self.loc = loc
        self.img_id = 0
        self.img = explosion_img
        self.frame = 0
        self.justcreated = True
        self.isAlive = True     
        self.rect = self.get_rect()

    def render(self, surf):
        surf.blit(self.img, (self.loc[0] - scroll[0], self.loc[1] - scroll[1]))

    def get_rect(self):
        return pygame.Rect(self.loc[0], self.loc[1], 16, 16)
    
    def collision_test(self, rect):
        Explosion_rect = self.get_rect()
        return Explosion_rect.colliderect(rect)
    
    def animate(self, Explosion_action):        
        if self.frame >= len(animation_database[Explosion_action]):
            self.frame = 0
            self.justcreated = False
        self.img_id = animation_database[Explosion_action][self.frame]
        self.img = animation_frames[self.img_id]
        self.frame += 1
        

class Mushroom_block():
    def __init__(self, loc):
        self.loc = loc
        self.img = what_block_img
        self.img_id = 0
        self.frame = 0
        self.vertical_momentum = 0.01
        self.rest_height = self.loc[1]
        self.rect = self.get_rect()
        self.y_vel = 0
        self.isbumping = False
        self.bumpingfinish = False

    def render(self, surf):
        
        surf.blit(self.img, (self.loc[0] - scroll[0], self.loc[1] - scroll[1]))

    def get_rect(self):
        return pygame.Rect(self.loc[0], self.loc[1], 16, 16)

    def collision_test(self, rect):
        mushroom_block_rect = self.get_rect()
        return mushroom_block_rect.colliderect(rect)
    
    def bump(self):
        if self.isbumping: # After mario bumps
            self.rect.y -= self.y_vel 
            self.y_vel += self.vertical_momentum
        
        if self.rect.y <= (self.rest_height - 5):
            self.isbumping = False
            self.bumpingfinish = True
            self.rect.y = self.rest_height

  
class What_block():
    def __init__(self, loc):
        self.loc = loc
        self.img = what_block_img
        self.img_id = 0
        self.frame = 0
        self.vertical_momentum = 0.01
        self.rest_height = self.loc[1]
        self.rect = self.get_rect()
        self.y_vel = 0
        self.isbumping = False
        self.bumpingfinish = False

    def render(self, surf):
        self.loc[0] = self.rect.x
        self.loc[1] = self.rect.y
        surf.blit(self.img, (self.loc[0] - scroll[0], self.loc[1] - scroll[1]))

    def get_rect(self):
        return pygame.Rect(self.loc[0], self.loc[1], 16, 16)

    def collision_test(self, rect):
        what_block_rect = self.get_rect()
        return what_block_rect.colliderect(rect)
    
    def bump(self):
        if self.isbumping: # After mario bumps
            self.rect.y -= self.y_vel 
            self.y_vel += self.vertical_momentum
        
        if self.rect.y <= (self.rest_height - 5):
            self.isbumping = False
            self.bumpingfinish = True
            self.rect.y = self.rest_height

class Empty_what_block():
    
    def __init__(self, loc):
        self.loc = loc
        
    def render(self, surf):
        surf.blit(empty_what_block_img, (self.loc[0] - scroll[0], self.loc[1] - scroll[1]))

    def get_rect(self):
        return pygame.Rect(self.loc[0], self.loc[1], 16, 16)

    def collision_test(self, rect):
        empty_block_rect = self.get_rect()
        return empty_block_rect.colliderect(rect)
    
class Brick():
    def __init__(self, loc, indexx):
        self.loc = loc
        self.img = brick_img
        self.img_id = 0
        self.frame = 0
        self.action = 'brick_idle'
        self.vertical_momentum = 0.01
        self.y_vel = 0
        self.rect = self.get_rect()
        self.destroyed = False
        self.indexx = indexx
        self.rest_height = self.loc[1]
        self.isbumping = False

    def render(self, surf):
        self.loc[0] = self.rect.x
        self.loc[1] = self.rect.y
        surf.blit(self.img, (self.loc[0] - scroll[0], self.loc[1] - scroll[1]))

    def get_rect(self):
        return pygame.Rect(self.loc[0], self.loc[1], 16, 16)
    
    def get_small_rect(self):
        return pygame.Rect(self.loc[0], self.loc[1], 16, 14)

    def collision_test(self, rect):
        brick_rect = self.get_rect()
        return brick_rect.colliderect(rect)
    
    def bump(self):
        
        if self.isbumping: # After mario bumps
            self.rect.y -= self.y_vel 
            self.y_vel += self.vertical_momentum
        
        if self.rect.y < (self.rest_height - 8):
            self.isbumping = False
            self.rect.y = self.rest_height





class Goomba():
    def __init__(self, loc):
        self.loc = loc
        self.direction = 'left'
        self.vertical_momentum = 3
        self.movement = [0,0]
        self.img_id = 0
        self.img = goomba_img
        self.frame = 0
        self.isAlive = True
        self.movementSpeed = 0.5
        self.collision_types = {'top':False,'bottom':False,'right':False,'left':False}
        self.rect = self.get_rect()
        self.flip = False


    def render(self, surf):
        self.loc[0] = self.rect.x
        self.loc[1] = self.rect.y
        surf.blit(pygame.transform.flip(self.img, False, self.flip), (self.loc[0] - scroll[0], self.loc[1] - scroll[1]))

    def get_rect(self):
        return pygame.Rect(self.loc[0], self.loc[1], 16, 16)

    def collision_test(self, rect):
        goomba_rect = self.get_rect()
        return goomba_rect.colliderect(rect)
    
    def move(self):
        self.movement = [0,0]
        if self.direction == 'left' and self.isAlive:
            goomba.movement[0] -= 1
        if self.direction == 'right' and self.isAlive:
            goomba.movement[0] += 1
        goomba.movement[1] += goomba.vertical_momentum
        goomba.vertical_momentum += 0.2
        if goomba.vertical_momentum > 3:
            goomba.vertical_momentum = 3
            
    def animate(self, goomba_action):
        self.frame += 1
        if self.frame >= len(animation_database[goomba_action]):
            self.frame = 0
        self.img_id = animation_database[goomba_action][self.frame]
        self.img = animation_frames[self.img_id]
        
class Koopa():
    def __init__(self, loc):
        self.loc = loc
        self.direction = 'left'
        self.vertical_momentum = 3
        self.movement = [0,0]
        self.img_id = 0
        self.img = koopa_img
        self.frame = 0
        self.isAlive = True
        self.isstomped = False
        self.movementSpeed = 0.5
        self.collision_types = {'top':False,'bottom':False,'right':False,'left':False}
        self.rect = self.get_rect()
        self.flip = False
        self.action = 'koopa_run'
        self.xflip = True
        


    def render(self, surf):
        self.loc[0] = self.rect.x
        self.loc[1] = self.rect.y
        surf.blit(pygame.transform.flip(self.img, self.xflip, self.flip), (self.loc[0] - scroll[0], self.loc[1] - scroll[1]))

    def get_rect(self):
        if self.isAlive and not self.isstomped:
            return pygame.Rect(self.loc[0], self.loc[1], 16, 22)
        else:
            return pygame.Rect(self.loc[0], self.loc[1], 16, 16)

    def collision_test(self, rect):
        koopa_rect = self.get_rect()
        return koopa_rect.colliderect(rect)
    
    def move(self):
        self.movement = [0,0]
        if self.direction == 'left' and self.isAlive and not self.isstomped:
            self.movement[0] -= 1
            self.xflip = False
        if self.direction == 'right' and self.isAlive and not self.isstomped:
            self.movement[0] += 1
            self.xflip = True
        self.movement[1] += self.vertical_momentum
        self.vertical_momentum += 0.2
        if self.vertical_momentum > 3:
            self.vertical_momentum = 3
            
    def animate(self, koopa_action):
        self.frame += 1
        if self.frame >= len(animation_database[koopa_action]):
            self.frame = 0
        self.img_id = animation_database[koopa_action][self.frame]
        self.img = animation_frames[self.img_id]


class Fireball():
    def __init__(self, loc , direction):
        self.loc = loc
        self.direction = direction
        self.vertical_momentum = -2
        self.movement = [0,0]
        self.img_id = 0
        self.img = fireball_img
        self.frame = 0
        self.isAlive = True
        self.bounces = 0
        self.movementSpeed = 3
        self.collision_types = {'top':False,'bottom':False,'right':False,'left':False}
        self.rect = self.get_rect()


    def render(self, surf):
        self.loc[0] = self.rect.x
        self.loc[1] = self.rect.y
        surf.blit(self.img, (self.loc[0] - scroll[0], self.loc[1] - scroll[1]))

    def get_rect(self):
        return pygame.Rect(self.loc[0], self.loc[1], 8, 8)

    def collision_test(self, rect):
        fireball_rect = self.get_rect()
        return fireball_rect.colliderect(rect)
    
    def move(self):
        self.movement = [0,0]
        if self.direction == 'left' and self.isAlive:
            self.movement[0] -= self.movementSpeed
        if self.direction == 'right' and self.isAlive:
            self.movement[0] += self.movementSpeed
        self.movement[1] += self.vertical_momentum
        
        self.vertical_momentum += 0.2
        if self.vertical_momentum > 3:
            self.vertical_momentum = 3
            
    def animate(self, fireball_action):
        self.frame += 1
        if self.frame >= len(animation_database[fireball_action]):
            self.frame = 0
        self.img_id = animation_database[fireball_action][self.frame]
        self.img = animation_frames[self.img_id]

class Bomb():
    def __init__(self, loc , direction):
        self.loc = loc
        self.direction = direction
        self.vertical_momentum = -2
        self.movement = [0,0]
        self.img_id = 0
        self.img = bomb_img
        self.frame = 0
        self.isAlive = True
        self.bounces = 0
        self.movementSpeed = 3
        self.collision_types = {'top':False,'bottom':False,'right':False,'left':False}
        self.rect = self.get_rect()


    def render(self, surf):
        self.loc[0] = self.rect.x
        self.loc[1] = self.rect.y
        surf.blit(self.img, (self.loc[0] - scroll[0], self.loc[1] - scroll[1]))

    def get_rect(self):
        return pygame.Rect(self.loc[0], self.loc[1], 8, 8)

    def collision_test(self, rect):
        bomb_rect = self.get_rect()
        return bomb_rect.colliderect(rect)
    
    def move(self):
        self.movement = [0,0]
        if self.direction == 'left' and self.isAlive:
            self.movement[0] -= self.movementSpeed
        if self.direction == 'right' and self.isAlive:
            self.movement[0] += self.movementSpeed
        self.movement[1] += self.vertical_momentum
        
        self.vertical_momentum += 0.2
        if self.vertical_momentum > 3:
            self.vertical_momentum = 3
            
    def animate(self, bomb_action):
        self.frame += 1
        if self.frame >= len(animation_database[bomb_action]):
            self.frame = 0
        self.img_id = animation_database[bomb_action][self.frame]
        self.img = animation_frames[self.img_id]
    


########## Game Main Functions ##############################

loadlevels('levels/map')
load_map(levels[0]) # load the map as tilemap

#Create object\instances from classes according to loaded tilemap

def loadtiles():
    idex = []
    global tile_rects
    tile_rects = []
    indexx = 0
    y = 0
    for layer in game_map:
        x = 0
        for tile in layer:
            if tile == '@':
                player_rect.x = x*16
                player_rect.y = y*16
            elif tile == 'c':
                coin_objects.append(Coin_obj((x*16,y*16)))
                indexx +=1
            elif tile == 'x':
                goombas.append(Goomba([x*16,y*16]))
            elif tile == 'k':
                koopas.append(Koopa([x*16,y*16]))
                indexx +=1
            elif tile == '?':
                what_blocks.append(What_block([x*16,y*16]))
                indexx +=1
            elif tile == 'm':
                mushroom_blocks.append(Mushroom_block([x*16,y*16]))
                

                indexx +=1
            elif tile == 'b':
                bricks.append(Brick([x*16,y*16],indexx))

                indexx +=1
            elif tile == 'F':
                flags.append(Flag([x*16,y*16-152]))
            x += 1
        y += 1


def render_map(): #Render the current map (Repeat every frame)
    #Rendering map from tilemap
    tile_rects.clear()
    y = 0
    for layer in game_map:
        x = 0
        for tile in layer:
            
            if tile == 'b':#If the current brick is broken dont add colliders
                brickrect = pygame.Rect(x*16,(y*16),16,14)
                if brickrect not in broken_bricks:
                    tile_rects.append(brickrect)
                else:
                    tile_rects.append(pygame.Rect(x*16,(y*16)+300,1,1))
            
            if tile == 'a':
                display.blit(broken_brick_img,(x*16-scrollx,y*16-scrolly))
            if tile == 'l':
                display.blit(block_img,(x*16-scrollx,y*16-scrolly))
            
            if tile == 'q':
                display.blit(pipe0_img,(x*16-scrollx,(y*16)-16-scrolly))
                tile_rects.append(pygame.Rect(x*16,(y*16)-16,32,32))
            if tile == 'w':
                display.blit(pipe1_img,(x*16-scrollx,(y*16)-32-scrolly))
                tile_rects.append(pygame.Rect(x*16,(y*16)-32,32,48))
            if tile == 'e':
                display.blit(pipe2_img,(x*16-scrollx,(y*16)-48-scrolly))
                tile_rects.append(pygame.Rect(x*16,(y*16)-48,32,64))
                
            if tile == 'Q':
                display.blit(cloud0_img,(x*16-scrollx,(y*16)-scrolly))
            if tile == 'W':
                display.blit(grass0_img,(x*16-scrollx,(y*16)-scrolly))
            if tile == 'E':
                display.blit(hill0_img,(x*16-scrollx,(y*16)-16-scrolly))
            if tile == 'R':
                display.blit(hill1_img,(x*16-scrollx,(y*16)-scrolly))
            if tile == 'O':
                display.blit(castle0_img,(x*16-scrollx,(y*16)-scrolly))
                       
            if tile not in ['@',' ','0','c','x','?','b','m','q',
                            'w','e','Q','W','E','R','O','F','k']: #Add tile colliders if jpt is given
                tile_rects.append(pygame.Rect(x*16,y*16,16,16))           
            if tile == '?':
                tile_rects.append(pygame.Rect(x*16,(y*16),16,14))
            if tile == 'm':
                tile_rects.append(pygame.Rect(x*16,(y*16),16,14))
            if tile == 'F':
                tile_rects.append(pygame.Rect(x*16,(y*16),16,16))
                
            
            x += 1
        y += 1
    

screen.fill(blue)
pygame.display.update()
pygame.key.set_repeat(500,30)

    
choose = dm.dumbmenu(screen, [
                        'Start Game',
                        'Quit Game'], 250,200,None,32,1.4,green,red)
if choose == 1:
    pygame.quit()
    exit()

loadtiles()

while not IsGameOver or True: # Main game loop
    
    if player_rect.y > 216:
        IsGameOver = True
        pygame.mixer.music.stop()
        die_sound.play()
        pygame.time.delay(3000)
        level -= 1
        NextLevel = True
    
    if NextLevel:
                
        pygame.time.delay(5000)


        print('nextlevel') 
        IsGameOver = False
        blockinput = False

        freeze_y = 0

        coin_frame = 0
        coin_action = 'coin'

        score = 0

        player_flash = False
        beingsmall = False
        beingbig = False
        beinggod = False
        moving_left = False
        moving_right = False
        isFreeFalling = False

        NextLevel = False

        scrollx = 0
        scrolly = 0

        true_scrollx = 0
        true_scrolly = 0

        level = 0
        
        

        #level,scroll and game objects lists
        pygame.mixer.music.load('music/main.ogg')  #load music from files
        pygame.mixer.music.play() #play the loaded music


        levels = []
        scroll = []
        flags = []
        game_map = []
        coin_objects = []
        what_blocks = []
        empty_what_blocks = []
        mushroom_blocks = []
        mushrooms = []
        flowers = []
        fireballs = []
        bricks = []
        goombas = []
        goombas_kill = []
        tile_rects_indexes = []
        broken_bricks = []
        tile_rects = []
        koopas = []
        koopas_kill = []
        
        pygame.mixer.music.load('music/main.ogg')
        pygame.mixer.music.play()
        level += 1
        
        air_timer = 0
        vertical_momentum = 0
        
        if level > len(levels):
                pygame.mixer.music.stop()
                display.fill((0,0,0))
                scorelabel = myfont.render('GAME OVER', 1, (255,255,255))
                display.blit(scorelabel, (100,100)) 
            
        loadlevels('levels/map')
        load_map(levels[level])
        loadtiles()
    
    display.fill(skyblue)# fill the background with sky blue
    
    true_scrollx += ((player_rect.x-true_scrollx) - 152)/15 #scrolling   
    true_scrolly += ((player_rect.y-true_scrolly) - 106)/15 #scrolling 
    
    scrollx = int(true_scrollx)  #scrolling x , camera following player along x axis
    scrolly = 16  #scrolling y, leaving this off for supermario bros original scrolling

    scroll = [scrollx,scrolly]  #scrolling 
    
    render_map()  #draw the whole map on screen
    
    scorelabel = myfont.render('SCORE:' + str(score), 1, (255,255,255))
    display.blit(scorelabel, (240,10))
    fpslabel = myfont.render('FPS:' + str(int(clock.get_fps())), 1, (255,255,255))
    display.blit(fpslabel, (250,20)) 

    # Movement and Gravity
        
    player_movement = [0,0]
    if moving_right == True:
        player_movement[0] += 2 * speedMultiplier
    if moving_left == True:
        player_movement[0] -= 2 * speedMultiplier
    player_movement[1] += vertical_momentum
    vertical_momentum += 0.2

    
    #Handle Player Animation
    if NextLevel:
        player_action,player_frame = change_action(player_action,player_frame,'smallflag')
    
    elif player_size == 'small': 
        if IsGameOver:
            player_action,player_frame = change_action(player_action,player_frame,'smalldie')       
        elif beingsmall:
                player_action,player_frame = change_action(player_action,player_frame,'big_to_small')
                if not player_flash:
                    player_flash = True
                else:
                    player_flash = False
                
        elif isFreeFalling == True:
            player_action,player_frame = change_action(player_action,player_frame,'smalljump')

        elif player_movement[0] == 0:
            player_action,player_frame = change_action(player_action,player_frame,'smallidle')

        elif player_movement[0] > 0:
            player_flip = False
            player_action,player_frame = change_action(player_action,player_frame,'smallrun')

        elif player_movement[0] < 0:
            player_flip = True
            player_action,player_frame = change_action(player_action,player_frame,'smallrun')
    
    elif player_size == 'big':
        
        if IsGameOver:
            player_action,player_frame = change_action(player_action,player_frame,'bigdie')       
        
        elif beingbig:
                vertical_momentum = 0
                player_rect.y = freeze_y
                player_action,player_frame = change_action(player_action,player_frame,'small_to_big')
                if not player_flash:
                    player_flash = True
                else:
                    player_flash = False
                    isinvincible = False
                    
        elif beingsmall:
                vertical_momentum = -2
                player_action,player_frame = change_action(player_action,player_frame,'firetobig')
                if not player_flash:
                    player_flash = True
                else:
                    player_flash = False
                    isinvincible = False
                    
        elif isFreeFalling == True:
            player_action,player_frame = change_action(player_action,player_frame,'bigjump')

        elif player_movement[0] == 0:
            player_action,player_frame = change_action(player_action,player_frame,'bigidle')

        elif player_movement[0] > 0:
            player_flip = False
            player_action,player_frame = change_action(player_action,player_frame,'bigrun')

        elif player_movement[0] < 0:
            player_flip = True
            player_action,player_frame = change_action(player_action,player_frame,'bigrun')
        
    elif player_size == 'fire':
        
        if IsGameOver:
            player_action,player_frame = change_action(player_action,player_frame,'firedie')       
            
        elif beingfire:
            vertical_momentum = 0
            player_rect.y = freeze_y
            player_action,player_frame = change_action(player_action,player_frame,'bigtofire')
            if not player_flash:
                player_flash = True
            else:
                player_flash = False
                isinvincible = False
                        
        elif isFreeFalling == True:
            player_action,player_frame = change_action(player_action,player_frame,'firejump')

        elif player_movement[0] == 0:
            player_action,player_frame = change_action(player_action,player_frame,'fireidle')

        elif player_movement[0] > 0:
            player_flip = False
            player_action,player_frame = change_action(player_action,player_frame,'firerun')

        elif player_movement[0] < 0:
            player_flip = True
            player_action,player_frame = change_action(player_action,player_frame,'firerun')
    
    elif player_size == 'bomber':
        
        if IsGameOver:
            player_action,player_frame = change_action(player_action,player_frame,'bomberdie')       
            
        elif beingbomber:
            vertical_momentum = 0
            player_rect.y = freeze_y
            player_action,player_frame = change_action(player_action,player_frame,'firetobomber')
            if not player_flash:
                player_flash = True
            else:
                player_flash = False
                isinvincible = False
                        
        elif isFreeFalling == True:
            player_action,player_frame = change_action(player_action,player_frame,'bomberjump')

        elif player_movement[0] == 0:
            player_action,player_frame = change_action(player_action,player_frame,'bomberidle')

        elif player_movement[0] > 0:
            player_flip = False
            player_action,player_frame = change_action(player_action,player_frame,'bomberrun')

        elif player_movement[0] < 0:
            player_flip = True
            player_action,player_frame = change_action(player_action,player_frame,'bomberrun')
               
    player_rect,collisions = move(player_rect,player_movement,tile_rects) #Check player collision
    
    if collisions['bottom'] == True and not IsGameOver:
        air_timer = 0
        vertical_momentum = 0
        isFreeFalling = False
    if collisions['top'] == True and not IsGameOver:
        vertical_momentum = 0
        isFreeFalling = False
    if vertical_momentum > 3:
        vertical_momentum = 3
    else:
        air_timer += 1
        
    player_frame += 1
    if player_frame >= len(animation_database[player_action]):
        player_frame = 0
        beingsmall = False
        beingbig = False
        beingfire = False
        beingbomber = False

    player_img_id = animation_database[player_action][player_frame]
    player_img = animation_frames[player_img_id]
    
    if not player_flash:
        display.blit(pygame.transform.flip(player_img,player_flip,False),(player_rect.x - scrollx,player_rect.y - scrolly)) # player render
    
    ###########################################################
    
    #Objects and Enemies processing.
    coin_frame += 1
    if coin_frame >= len(animation_database[coin_action]):
        coin_frame = 0
    coin_img_id = animation_database[coin_action][coin_frame]
    coin_img = animation_frames[coin_img_id]
     
    
    for explosion in explosions:
        if explosion.justcreated:
            explosion.render(display)
            explosion.animate('explosion')
        
        
        
    
    for brick in bricks:
        if brick.isbumping:
            brick.bump()
            

        brick.frame += 1
        if brick.frame  >= len(animation_database['brick']) and brick.action == 'brick' and not brick.destroyed:
            
            brick.frame = 0
            brick.destroyed = True
            bricks.remove(brick)
            
        if brick.frame >= len(animation_database[brick.action]):
            brick.frame = 0
            
        
        if not brick.destroyed:
            brick.img_id = animation_database[brick.action][brick.frame]
            brick.img = animation_frames[brick.img_id]
        
        brick.render(display)
        if brick.collision_test(player_rect) and not IsGameOver:
            if brick.loc[1] > player_rect.y:
                vertical_momentum -= 0.2
                air_timer = 0
            if brick.loc[1] < player_rect.y and not IsGameOver:
                if player_size in ['big','fire','bomber']:
                    broken_bricks.append(brick.get_small_rect())
                    brick.action,brick.frame = change_action(brick.action,brick.frame,'brick')
                    brick_break_sound.set_volume(1)
                    brick_break_sound.play()
                    vertical_momentum = 5
                if player_size == 'small':
                    brick.isbumping = True
                    brick.bump()
                    bump_sound.set_volume(1)
                    bump_sound.play()
                

    for emptyblock in empty_what_blocks:
        emptyblock.render(display)
        if emptyblock.collision_test(player_rect) and not IsGameOver:
            if emptyblock.loc[1] > player_rect.y:
                vertical_momentum -= 0.2
                air_timer = 0
            if emptyblock.loc[1] < player_rect.y and not IsGameOver:
                bump_sound.set_volume(1)
                bump_sound.play()
                vertical_momentum = 5
    

    
    for whatblock in what_blocks:
        if whatblock.isbumping:
            whatblock.bump()
        
        if whatblock.bumpingfinish:
            coins += 1
            score += 50
            coin_bounces.append(Coin_bounce(whatblock.loc))
            empty_what_blocks.append(Empty_what_block(whatblock.loc))
            what_blocks.remove(whatblock)

        whatblock_action = 'what'
        
        whatblock_action,whatblock.frame = change_action(whatblock_action,whatblock.frame,'what')
        
        whatblock.frame += 1        
        if whatblock.frame >= len(animation_database[whatblock_action]):
            whatblock.frame = 0
        whatblock.img_id = animation_database[whatblock_action][whatblock.frame]
        whatblock.img = animation_frames[whatblock.img_id]
        
        
        whatblock.render(display)
        
        if whatblock.collision_test(player_rect) and not IsGameOver:
            if player_rect.y > whatblock.loc[1]:
                whatblock.isbumping = True
                bump_sound.set_volume(0.5)
                bump_sound.play()
                coin_sound.play()
    
    for coin_bounce in coin_bounces:
        coin_bounce.loc[1] -= 0.5
        coin_bounce.render(display)
        coin_bounce.action,coin_bounce.frame = change_action(coin_bounce.action,coin_bounce.frame,'coin_bounce')
        coin_bounce.animate(coin_bounce.action)
        
        if coin_bounce.frameloops > 0:
            coin_bounces.remove(coin_bounce)

        
    for mushroomblock in mushroom_blocks:
        
        if mushroomblock.isbumping:
            mushroomblock.bump()
        
        if mushroomblock.bumpingfinish:
            if player_size == 'small':
                empty_what_blocks.append(Empty_what_block(mushroomblock.loc))           
                mushrooms.append(Mushroom(mushroomblock.loc))
                mushroom_blocks.remove(mushroomblock)
            if player_size in ['big']:
                empty_what_blocks.append(Empty_what_block(mushroomblock.loc))           
                flowers.append(Flower(mushroomblock.loc))
                mushroom_blocks.remove(mushroomblock)
            if player_size in ['fire','bomber']:
                empty_what_blocks.append(Empty_what_block(mushroomblock.loc))           
                bombers.append(Bomber(mushroomblock.loc))
                mushroom_blocks.remove(mushroomblock)
        
        mushroomblock_action = 'what'
        mushroomblock_action,mushroomblock.frame = change_action(mushroomblock_action,mushroomblock.frame,'what')
        
        mushroomblock.frame += 1        
        if mushroomblock.frame >= len(animation_database[mushroomblock_action]):
            mushroomblock.frame = 0
        mushroomblock.img_id = animation_database[mushroomblock_action][mushroomblock.frame]
        mushroomblock.img = animation_frames[mushroomblock.img_id]
        
        mushroomblock.render(display)
        if mushroomblock.collision_test(player_rect) and not IsGameOver:
            if player_rect.y > mushroomblock.loc[1]:
                mushroomblock.isbumping = True               
                powerup_appear.set_volume(1)
                powerup_appear.play()
                vertical_momentum -= 3
                
    for bomber in bombers:
        bomber.render(display) 
        if bomber.justcreated:
            bomber.animate('bomber_pop')
        else:
            bomber.animate('bomber')
            
        if bomber.collision_test(player_rect) and bomber.isAlive and not IsGameOver:
            if player_size == 'small':
                score += 200
                beingbig = True
                player_rect = pygame.rect.Rect(player_rect.x,player_rect.y,16,32)
                powerup.play()
                player_size = 'big'
                freeze_y = player_rect.y - 16
                bombers.remove(bomber)
            elif player_size == 'big':
                beingfire = True
                score += 200
                powerup.play()
                player_size = 'fire'
                freeze_y = player_rect.y - 16
                bombers.remove(bomber)
            elif player_size == 'fire':
                beingbomber = True
                score += 200
                powerup.play()
                player_size = 'bomber'
                freeze_y = player_rect.y - 16
                bombers.remove(bomber)      
            else:
                score += 100
                powerup.play()
                bombers.remove(bomber)
                
    for flower in flowers:
        flower.render(display) 
        if flower.justcreated:
            flower.animate('fpop')
        else:
            flower.animate('flower')
            
        if flower.collision_test(player_rect) and flower.isAlive and not IsGameOver:
            if player_size == 'small':
                score += 200
                beingbig = True
                player_rect = pygame.rect.Rect(player_rect.x,player_rect.y,16,32)
                powerup.play()
                player_size = 'big'
                freeze_y = player_rect.y - 16
                flowers.remove(flower)
            elif player_size == 'big':
                beingfire = True
                score += 200
                powerup.play()
                player_size = 'fire'
                freeze_y = player_rect.y - 16
                flowers.remove(flower)
            else:
                score += 100
                powerup.play()
                flowers.remove(flower)
            
    for mushroom in mushrooms:
        
        mushroom.render(display)
        
        if mushroom.justcreated:
            mushroom.animate('pop')
        else:
            mushroom.animate('mushroom')
    
        
        mushroom.move()
        mushroom.rect,collisions = move(mushroom.rect,mushroom.movement,tile_rects)
        
        if collisions['bottom'] == True:
            mushroom.vertical_momentum = 0
        if collisions['top'] == True:
            mushroom.vertical_momentum = 0
        if mushroom.vertical_momentum > 3:
            mushroom.vertical_momentum = 3
        if collisions['left'] == True:
            mushroom.movement[0] = 1
            mushroom.direction = 'right'
            mushroom.move()
        if collisions['right'] == True:
            mushroom.direction = 'left'
            mushroom.movement[0] = -1
            mushroom.move()
            
        mushroom.loc[1] += mushroom.vertical_momentum
        
        if mushroom.collision_test(player_rect) and mushroom.isAlive and not IsGameOver:
            if player_size == 'small':
                score += 200
                beingbig = True
                player_rect = pygame.rect.Rect(player_rect.x,player_rect.y,16,32)
                powerup.play()
                player_size = 'big'
                freeze_y = player_rect.y - 16
                mushrooms.remove(mushroom)
            else:
                score += 100
                powerup.play()
                mushrooms.remove(mushroom)
                
    for coin in coin_objects:
        coin.render(display)
        if coin.collision_test(player_rect):
            score += 50
            coins += 1
            coin_sound.play()
            coin_objects.remove(coin)
            
    
    
    for goomba in goombas:
        if abs(player_rect.x - goomba.loc[0]) < 160:
            goomba.move()
            
            if goomba.rect.y > 200:
                goombas.remove(goomba)
            if goomba.flip:
                goomba.rect.y += 2
                
            if not goomba.flip:
                goomba.rect,collisions = move(goomba.rect,goomba.movement,tile_rects)
                if collisions['bottom'] == True:
                    goomba.vertical_momentum = 0
                if collisions['top'] == True:
                    goomba.vertical_momentum = 0
                if goomba.vertical_momentum > 3:
                    goomba.vertical_momentum = 3
                if collisions['left'] == True:
                    goomba.direction = 'right'
                    goomba.move()
                if collisions['right'] == True:
                    goomba.direction = 'left'
                    goomba.move()
                
                if goomba.vertical_momentum > 3:
                    goomba.vertical_momentum = 3
                
        
            
            if goomba.isAlive or goomba not in goombas_kill:
                goomba.move()
                goomba.animate('goomba_run')
            else:
                goomba.animate('goomba_die')
                
            goomba.render(display)
            
            for fireball in fireballs:
                if goomba.collision_test(fireball.get_rect()) and goomba.isAlive:
                    fireballs.remove(fireball)
                    kick_sound.play()
                    score += 100
                    goomba.isAlive = True
                    pygame.time.set_timer(pygame.USEREVENT+0, 500)
                    goombas_kill.append(goomba)
                    goomba.flip = True
            
            for explosion in explosions:
                if goomba.collision_test(explosion.get_rect()) and goomba.isAlive:
                    kick_sound.play()
                    score += 100
                    goomba.isAlive = False
                    pygame.time.set_timer(pygame.USEREVENT+0, 500)
                    koopas_kill.append(koopa)
                    goomba.flip = True
        
            if goomba.collision_test(player_rect) and goomba.isAlive and not IsGameOver:
                if player_size == 'small':
                    if (player_rect.y) < goomba.loc[1]:
                        stomp_sound.play()
                        vertical_momentum = -3
                        score += 100
                        goomba.isAlive = False
                        pygame.time.set_timer(pygame.USEREVENT+0, 500)
                        goombas_kill.append(goomba)
                    elif goomba.isAlive:
                        pygame.time.set_timer(pygame.USEREVENT+1, 1)
                        die_sound.play()
                        IsGameOver = True
                    
                if player_size == 'big':
                    if (player_rect.y+16) < goomba.loc[1]:
                        stomp_sound.play()
                        vertical_momentum = -3
                        score += 100
                        goomba.isAlive = False
                        pygame.time.set_timer(pygame.USEREVENT+0, 500)
                        goombas_kill.append(goomba)
                    elif goomba.isAlive and not isinvincible:
                        player_rect = pygame.rect.Rect(player_rect.x,player_rect.y,16,16)
                        powerdown.play()
                        player_size = 'small'
                        beingsmall = True
                        vertical_momentum = -3
                        isinvincible = True
                        
                if player_size in ['fire']:
                    if (player_rect.y+16) < goomba.loc[1]:
                        stomp_sound.play()
                        vertical_momentum = -3
                        score += 100
                        goomba.isAlive = False
                        pygame.time.set_timer(pygame.USEREVENT+0, 500)
                        goombas_kill.append(goomba)
                    elif goomba.isAlive and not isinvincible:
                        powerdown.play()
                        player_size = 'big'
                        beingsmall = True
                        vertical_momentum = -3
                        isinvincible = True
                
                if player_size in ['bomber']:
                    if (player_rect.y+16) < goomba.loc[1]:
                        stomp_sound.play()
                        vertical_momentum = -3
                        score += 100
                        goomba.isAlive = False
                        pygame.time.set_timer(pygame.USEREVENT+0, 500)
                        goombas_kill.append(goomba)
                    elif goomba.isAlive and not isinvincible:
                        powerdown.play()
                        player_size = 'fire'
                        beingfire = True
                        vertical_momentum = -3
                        isinvincible = True
                
    
    for koopa in koopas:
        if abs(player_rect.x - koopa.loc[0]) < 160:
        
            if not koopa.isstomped:
                koopa.move()
            
            if koopa.rect.y > 200:
                koopas.remove(koopa)
            if koopa.flip:
                koopa.rect.y += 2
                
            if not koopa.flip:
                koopa.rect,collisions = move(koopa.rect,koopa.movement,tile_rects)
                if collisions['bottom'] == True:
                    koopa.vertical_momentum = 0
                if collisions['top'] == True:
                    koopa.vertical_momentum = 0
                if koopa.vertical_momentum > 3:
                    koopa.vertical_momentum = 3
                if collisions['left'] == True:
                    koopa.direction = 'right'
                if collisions['right'] == True:
                    koopa.direction = 'left'
                
                if koopa.vertical_momentum > 3:
                    koopa.vertical_momentum = 3
                
        
            
            if koopa.isAlive or koopa not in koopas_kill:
                koopa.animate('koopa_run')
            if koopa.isstomped:
                koopa.animate('koopa_die')
            
            koopa.render(display)
            
            for fireball in fireballs:
                if koopa.collision_test(fireball.get_rect()):
                    fireballs.remove(fireball)
                    kick_sound.play()
                    score += 100
                    koopa.isAlive = False
                    koopa.isstomped = True
                    pygame.time.set_timer(pygame.USEREVENT+0, 500)
                    koopas_kill.append(koopa)
                    koopa.flip = True
            
            for explosion in explosions:
                if koopa.collision_test(explosion.get_rect()):
                    kick_sound.play()
                    score += 100
                    koopa.isAlive = False
                    koopa.isstomped = True
                    pygame.time.set_timer(pygame.USEREVENT+0, 500)
                    koopas_kill.append(koopa)
                    koopa.flip = True
        
            if koopa.collision_test(player_rect) and koopa.isAlive and not IsGameOver:
                if not koopa.isstomped:
                    if player_size == 'small':
                        if (player_rect.y) < koopa.loc[1]:
                            stomp_sound.play()
                            vertical_momentum = -3
                            score += 100
                            koopa.isstomped = True
                            pygame.time.set_timer(pygame.USEREVENT+0, 500)
                            koopas_kill.append(koopa)
                            koopa.rect = pygame.Rect(koopa.loc[0], koopa.loc[1] + 6, 16, 16)
                            koopa.movement[0] = 0
                        elif not koopa.isstomped:
                            die_sound.play()
                            IsGameOver = True
                        
                    if player_size == 'big':
                        if (player_rect.y+16) < koopa.loc[1]:
                            stomp_sound.play()
                            vertical_momentum = -3
                            score += 100
                            koopa.isstomped = True
                            pygame.time.set_timer(pygame.USEREVENT+0, 500)
                            koopas_kill.append(koopa)
                            koopa.rect = pygame.Rect(koopa.loc[0], koopa.loc[1] + 6, 16, 16)
                            koopa.movement[0] = 0
                        elif not koopa.isstomped:
                            player_rect = pygame.rect.Rect(player_rect.x,player_rect.y,16,16)
                            powerdown.play()
                            player_size = 'small'
                            beingsmall = True
                            vertical_momentum = -3
                            
                    if player_size in ['bomber']:
                        if (player_rect.y+16) < koopa.loc[1]:
                            stomp_sound.play()
                            vertical_momentum = -3
                            score += 100
                            koopa.isAlive = True
                            koopa.isstomped = True
                            koopa.rect = pygame.Rect(koopa.loc[0], koopa.loc[1] + 6, 16, 16)
                            pygame.time.set_timer(pygame.USEREVENT+0, 500)
                            koopas_kill.append(koopa)
                            koopa.movement[0] = 0
                        elif koopa.isAlive:
                            powerdown.play()
                            player_size = 'fire'
                            beingfire = True
                            vertical_momentum = -3
                    
                    if player_size in ['fire']:
                        if (player_rect.y+16) < koopa.loc[1]:
                            stomp_sound.play()
                            vertical_momentum = -3
                            score += 100
                            koopa.isAlive = True
                            koopa.isstomped = True
                            koopa.rect = pygame.Rect(koopa.loc[0], koopa.loc[1] + 6, 16, 16)
                            pygame.time.set_timer(pygame.USEREVENT+0, 500)
                            koopas_kill.append(koopa)
                            koopa.movement[0] = 0
                        elif koopa.isAlive:
                            powerdown.play()
                            player_size = 'big'
                            beingvig = True
                            vertical_momentum = -3
                    
    
    
    
    for fireball in fireballs:
        
        fireball.render(display)
        fireball.animate('fireball')
        
        fireball.move()
        fireball.rect,collisions = move(fireball.rect,fireball.movement,tile_rects)
        
        if fireball.bounces > 1:
            fireballs.remove(fireball)
        
        if collisions['bottom'] == True:
            fireball.bounces += 1
            fireball.vertical_momentum = -3
        if collisions['top'] == True:
            fireball.bounces += 1
            fireball.vertical_momentum = -3
        if fireball.vertical_momentum > 3:
            fireball.vertical_momentum = 3
        if collisions['left'] == True:
            fireball.bounces += 1
            if fireball.vertical_momentum > 0:
                fireball.vertical_momentum = -3
                fireball.direction = 'right'
            else:
                fireball.vertical_momentum = 3
                fireball.direction = 'right'
                
        if collisions['right'] == True:
            fireball.bounces += 1
            if fireball.vertical_momentum > 0:
                fireball.vertical_momentum = -3
                fireball.direction = 'right'
            else:
                fireball.vertical_momentum = 3
                fireball.direction = 'left'
        if fireball.loc[1] > 200:
            fireballs.remove(fireball)
    
    for bomb in bombs:
        
        bomb.render(display)
        bomb.animate('bomb')
        
        bomb.move()
        bomb.rect,collisions = move(bomb.rect,bomb.movement,tile_rects)
        
        
        if collisions['bottom'] == True:
            bomb.vertical_momentum = -3
            explosions.append(Explosion(bomb.loc))
            bombs.remove(bomb)
        if collisions['top'] == True:
            bomb.vertical_momentum = -3
            explosions.append(Explosion(bomb.loc))
            bombs.remove(bomb)
        if bomb.vertical_momentum > 3:
            bomb.vertical_momentum = 3
        if collisions['left'] == True:
            explosions.append(Explosion(bomb.loc))
            bombs.remove(bomb)         
                
        if collisions['right'] == True:
            explosions.append(Explosion(bomb.loc))
            bombs.remove(bomb)
            
        if bomb.loc[1] > 200:
            bombs.remove(bomb)
    
    
    
    for flag in flags:
        flag.render(display)
        if flag.collision_test(player_rect) and not IsGameOver:
                blockinput = False
                vertical_momentum = 1.2
                player_flip = False
                print('Level end')
                
                player_img = small_flag_img
                player_rect.x = flag.loc[0] - 12
                pygame.mixer.music.stop()
                pygame.mixer.music.load('music/stage_clear.wav')  #load music from files
                pygame.mixer.music.play() #play the loaded music
                
                NextLevel = True

    
    for label in Labels:
        label.render(display)
                
                
                

    for event in pygame.event.get(): # Loop through every events of the game.
        
        if event.type == pygame.USEREVENT+0:
            for goo in goombas_kill:
                if not goo.flip:
                    try:
                        goombas.remove(goo)
                        goombas_kill.remove(goo)
                    except:
                        break
                    
        if event.type == pygame.USEREVENT+1:

            if a0xe3d == 0:
                player_rect.y -= 9
            a0xe3d = 1
            pygame.time.delay(10)
        
            
        
                
                
        if event.type == QUIT: # Check if the [X] Close window button is clicked.
            pygame.quit() # Exit the window.
            sys.exit() # Exit the console.

        # Input Handling.    
        if event.type == KEYDOWN and not IsGameOver and not blockinput: # Check if any key is pressed
            if event.key == K_LEFT: # Check if the pressed key is left 
                moving_left = True
                if event.key == K_x:
                    movement[0] += 3
            if event.key == K_RIGHT: # Check if the pressed key is right 
                moving_right = True
                if event.key == K_x:
                    movement[0] -= 3
            if event.key == K_UP:
                if air_timer < 7:
                    vertical_momentum = -5
                    isFreeFalling = True
                    if player_size == 'small':
                        small_jump_sound.set_volume(1)
                        small_jump_sound.play()
                    elif player_size in ['big','fire','bomber']:
                        big_jump_sound.set_volume(1)
                        big_jump_sound.play()
                        
            if event.key == K_x:
                if player_size == 'fire':
                    
                    if not isFreeFalling:
                        speedMultiplier = 1.5
                    if len(fireballs) < 2:
                        fireball_sound.play()
                        if player_flip:
                            fireballs.append(Fireball([player_rect.x - 12,player_rect.y], 'left'))
                        else:
                            fireballs.append(Fireball([player_rect.x + 12,player_rect.y], 'right'))
                elif player_size == 'bomber':
                    
                    if not isFreeFalling:
                        speedMultiplier = 1.5
                    if len(bombs) < 2:
                        fireball_sound.play()
                        if player_flip:
                            bombs.append(Bomb([player_rect.x - 12,player_rect.y], 'left'))
                        else:
                            bombs.append(Bomb([player_rect.x + 12,player_rect.y], 'right'))
                else:
                    if not isFreeFalling:
                        speedMultiplier = 1.5
                    
            if event.key == K_1:
                    beingsmall = True
                    player_size ='small'
                    powerdown.play()
                    player_x = player_rect.x
                    player_y = player_rect.y
                    player_rect = pygame.rect.Rect(player_x,player_y,16,16)
                    
            if event.key == K_2:
                    beingbig = True
                    player_size ='big'
                    powerup.play()
                    player_x = player_rect.x
                    player_y = player_rect.y
                    player_rect = pygame.rect.Rect(player_x,player_y,16,32)
             
            if event.key == K_3:
                    beingfire = True
                    player_size ='fire'
                    powerup.play()
                    player_x = player_rect.x
                    player_y = player_rect.y
                    player_rect = pygame.rect.Rect(player_x,player_y,16,32)
                    
            if event.key == K_4:
                    beingbomber = True
                    player_size ='bomber'
                    powerup.play()
                    player_x = player_rect.x
                    player_y = player_rect.y
                    player_rect = pygame.rect.Rect(player_x,player_y,16,32)
           
            if event.key == K_0:
               NextLevel = True
        if event.type == KEYUP and not IsGameOver: # Check if any key is released.
            if event.key == K_LEFT : # Check if the pressed key is left 
                moving_left = False
            if event.key == K_RIGHT: # Check if the pressed key is right 
                moving_right = False
            if event.key == K_x:
                speedMultiplier = 1

    #Debug Console
    #print('\n' * 100)
    #print('Player[x,y,g,airtime,fps] :'+ str([player_rect.x,player_rect.y,vertical_momentum,air_timer,clock]))
    #print('Player[score,scrollx,scrolly]' +str([score,scrollx,scrolly]))
    pygame.display.update() # Update the display.
    screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
    clock.tick(60) # Cap the frame rate of the game to 60fps.

