__author__='Utkrist Karki,realskull'
__version__='v1'
__builddate__='2020/5/8'

'''
MAP EDITOR 2D FOR ALL THE GAMES CREATED USING HELPv1 FRAMEWORK.
'''
import pygame,sys
from pygame.locals import * 

a0xe3d = 0 # jpt variable


pygame.init() 

WINDOW_SIZE = (640,480) 

screen = pygame.display.set_mode(WINDOW_SIZE,0,32) 

display = pygame.Surface((300,200)) 

pygame.mixer.pre_init(44100, -16,2,512) 

myfont = pygame.font.SysFont("retro", 40)
smallfont = pygame.font.SysFont("retro", 28)

pygame.display.set_caption('[LEVEL EDITOR][HELPv1]') 

clock = pygame.time.Clock()


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




blue = (146,244,255)
transparent = (255,255,255)
skyblue = (107,140,255)
red   = 255,  0,  0
green =   0,255,  0
blue  =   0,  0,255

dict_index = 0
dict_type_index = 0

dict_type_indexes = ['player','blocks','objects','enemies','pipes','background']

dict_indexes = [['@','@','@'],['a','b','l'],['?','m','F'],['x','k','x'],['q','w','e'],['W','E','R']]

tile_dict = {
    'player':{'@':player_img},
    'blocks':{'a':broken_brick_img,'b':brick_img,'l':block_img},
    'objects':{'?':what_block_img,'m':what_block_img,'F':flag_img},
    'enemies':{'x':goomba_img,'k':koopa_img},
    'pipes':{'q':pipe0_img,'w':pipe1_img,'e':pipe2_img},
    'background':{'W':grass0_img,'E':hill0_img,'R':hill1_img}
    }

tile_names ={
    'player':{'@':'starting player location'},
    'blocks':{'a':'broken_ground','b':'Breakable Bricks','l':'Stair Blocks'},
    'objects':{'?':'Coinblock','m':'Powerup Block','F':'End level flagpole'},
    'enemies':{'x':'Goomba','k':'Koopa'},
    'pipes':{'q':'Short Pipe','w':'Long Pipe','e':'Very much long pipe'},
    'background':{'W':'Grass','E':'Low Hills','R':'High Hills'}
    }

tile_offsets ={
    'player':{'@':0},
    'blocks':{'a':0,'b':0,'l':0},
    'objects':{'?':0,'m':0,'F':152},
    'enemies':{'x':0,'k':0},
    'pipes':{'q':16,'w':32,'e':48},
    'background':{'W':0,'E':16,'R':0}
    }


c_x = 10
c_y = 10
y_offset = 0

placetile = False
moving_left = False
moving_right = False
moving_up = False
moving_down = False

NextLevel = False

scrollx = 0
scrolly = 0

true_scrollx = 0
true_scrolly = 0

level = 0

deletetile = False
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
bombers = []
bricks = []
goombas = []
koopas = []
broken_bricks = []

path = 'map'

def create_map(path):
    f = open(path, 'w+')
    y = 0
    for i in range(15):
        for j in range(500):
            f.write(' ')
            
        f.write('\n')
    
    
    
    
def loadlevels(path): 
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
    try:
        f = open(path)
    except:
        create_map(path)
        f = open(path)
        
    data = f.read()
    f.close()
    data = data.split('\n')
    gamemap = []
    for row in data:
        game_map.append(list(row))
    return game_map

def save_map(path):
    f = open(path, 'w')
    y = 0
    for layer in game_map:
        x = 0
        for tile in layer:
            f.write(tile)
            x += 1
        f.write('\n')
        y += 1
    
    f.close()
    


global player_action
global player_frame
player_action = 'idle' # Player current action
player_frame = 0 # Player frame
player_flip = False # Flip player?

    
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

    
class Mushroom():
    def __init__(self, loc):
        self.loc = [loc[0],loc[1]-16]
        self.img = mushroom_img

    def render(self, surf):
        surf.blit(self.img, (self.loc[0] - scroll[0], self.loc[1] - scroll[1]))

    def get_rect(self):
        return pygame.Rect(self.loc[0], self.loc[1], 16, 16)

class Mushroom_block():
    def __init__(self, loc):
        self.loc = loc
        self.img = what_block_img

    def render(self, surf):
        surf.blit(self.img, (self.loc[0] - scroll[0], self.loc[1] - scroll[1]))

    def get_rect(self):
        return pygame.Rect(self.loc[0], self.loc[1], 16, 16)

    def collision_test(self, rect):
        mushroom_block_rect = self.get_rect()
        return mushroom_block_rect.colliderect(rect)
 
class What_block():
    def __init__(self, loc):
        self.loc = loc
        self.img = what_block_img

    def render(self, surf):
        surf.blit(self.img, (self.loc[0] - scroll[0], self.loc[1] - scroll[1]))

    def get_rect(self):
        return pygame.Rect(self.loc[0], self.loc[1], 16, 16)

    def collision_test(self, rect):
        what_block_rect = self.get_rect()
        return what_block_rect.colliderect(rect)
    
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
    def __init__(self, loc):
        self.loc = loc
        self.img = brick_img

    def render(self, surf):
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
        self.img = goomba_img

    def render(self, surf):
        surf.blit(self.img, (self.loc[0] - scroll[0], self.loc[1] - scroll[1]))

    def get_rect(self):
        return pygame.Rect(self.loc[0], self.loc[1], 16, 16)

    def collision_test(self, rect):
        goomba_rect = self.get_rect()
        return goomba_rect.colliderect(rect)
    

class Koopa():
    def __init__(self, loc):
        self.loc = loc
        self.img = koopa_img
        


    def render(self, surf):
        surf.blit(self.img, (self.loc[0] - scroll[0], self.loc[1] - scroll[1]))

    def get_rect(self):
        return pygame.Rect(self.loc[0], self.loc[1], 16, 22)

    def collision_test(self, rect):
        koopa_rect = self.get_rect()
        return koopa_rect.colliderect(rect)
           

########## Game Main Functions ##############################

loadlevels('levels/map')
load_map(levels[0]) # load the map as tilemap

#Create object\instances from classes according to loaded tilemap

def loadtiles():
    global tile_rects
    tile_rects = []
    y = 0
    for layer in game_map:
        x = 0
        for tile in layer:
                if tile == '@':
                    player_x = x*16
                    player_y = y*16
                elif tile == 'c':
                    coin_objects.append(Coin_obj((x*16,y*16)))
                elif tile == 'x':
                    goombas.append(Goomba([x*16,y*16]))
                elif tile == 'k':
                    koopas.append(Koopa([x*16,y*16]))
                elif tile == '?':
                    what_blocks.append(What_block([x*16,y*16]))
                elif tile == 'm':
                    mushroom_blocks.append(Mushroom_block([x*16,y*16]))
                elif tile == 'b':
                    bricks.append(Brick([x*16,y*16]))
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
    


loadtiles()

while True: # Main game loop
    
    if dict_type_index > 5:
        dict_type_index = 5
    if dict_index > 2:
        dict_index = 2
    
        
    save_map('levels/map'+str(level)+'.txt')
    #UI ELEMENTS
    fpslabel = myfont.render('FPS:' + str(int(clock.get_fps())), 1, (0,0,0))
    screen.blit(fpslabel, (20,20))
    cordinates = myfont.render('X:'+str(c_x)+' Y:'+str(c_y), 1, (0,0,0))
    screen.blit(cordinates, (500,20))
    cordinates = myfont.render('Level:'+str(level), 1, (0,0,0))
    screen.blit(cordinates, (500,50))
    
    
    
    if NextLevel:
        NextLevel = False

        scrollx = 0
        scrolly = 0

        true_scrollx = 0
        true_scrolly = 0     
        
        c_x = 5
        c_y = 5

        levels = []
        scroll = []
        flags = []
        game_map = []
        coin_objects = []
        what_blocks = []
        empty_what_blocks = []
        mushroom_blocks = []
        bricks = []
        goombas = []
        broken_bricks = []
        tile_rects = []
        koopas = []
        level += 1
        print(level)   
        load_map('levels/map'+str(level)+'.txt')
            
    
    loadtiles()
    
    display.fill(skyblue)
    
    true_scrollx += ((c_x*16-true_scrollx) -156)
    true_scrolly += ((c_y*16-true_scrolly) -106)
    
    scrollx = int(true_scrollx)
    scrolly = 16

    scroll = [scrollx,scrolly]
    current_type = dict_type_indexes[dict_type_index]
    current_tile = dict_indexes[dict_type_index][dict_index]
    
    current_name = tile_names[current_type][current_tile]
    y_offset = tile_offsets[current_type][current_tile]
    
    label = smallfont.render(current_type, 1, (0,0,0))
    screen.blit(label, (280,5))
    label = smallfont.render(str(current_name), 1, (0,0,0))
    screen.blit(label, (280,60))
                
    loadtiles()
    render_map()  #draw the whole map on screen
#Move the cursor
    if moving_left:
        if c_x == 0:
            c_x = 0
        else:
            c_x -= 1
            moving_left = False
    if moving_right:
        c_x += 1
        moving_right = False
    if moving_up:
        if c_y == 1:
            c_y = 1
        else:
            c_y -= 1
            moving_up = False
    if moving_down:
        if c_y == 13:
            c_y = 13
        else:
            c_y += 1
            moving_down = False
    
    if deletetile:
        game_map[c_y][c_x] = ' '
        deletetile = False
    
    if placetile:
        game_map[c_y][c_x] = current_tile
        placetile = False
    
    
# Render the level object.
    for brick in bricks:
        brick.render(display)
                
    for emptyblock in empty_what_blocks:
        emptyblock.render(display)
   
    for whatblock in what_blocks:
        whatblock.render(display)
        
    for mushroomblock in mushroom_blocks:
        mushroomblock.render(display)
                              
    for coin in coin_objects:
        coin.render(display)
            
    for goomba in goombas:
        goomba.render(display)
 
    for koopa in koopas:
        koopa.render(display)
  
    for flag in flags:
        flag.render(display)
    
    for objects in [flags,koopas,goombas,coin_objects,mushroom_blocks,what_blocks,bricks]:
        objects.clear()
    
    display.blit(tile_dict[current_type][current_tile],(c_x*16 - scrollx,c_y*16 - y_offset - scrolly))
    
    display.blit(tile_dict[current_type][current_tile],(150,10))

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
        if event.type == KEYDOWN: # Check if any key is pressed
            if event.key == K_LEFT: # Check if the pressed key is left 
                moving_left = True
            if event.key == K_RIGHT: # Check if the pressed key is right 
                moving_right = True
            if event.key == K_UP:
                moving_up = True
            if event.key == K_DOWN:
                moving_down = True
           
            if event.key == K_0:
               NextLevel = True
               
            if event.key == K_x:
                placetile = True
            
            if event.key == K_a:
                dict_index -= 1
                if dict_index < 0:
                    dict_index = 0
            
            if event.key == K_d:
                dict_index += 1
            
            if event.key == K_w:
                dict_type_index -= 1
                if dict_type_index < 0:
                    dict_type_index = 0
            
            if event.key == K_s:
                dict_type_index += 1
                
            if event.key == K_z:
                deletetile = True
               
        if event.type == KEYUP: # Check if any key is released.
            if event.key == K_LEFT : # Check if the pressed key is left 
                moving_left = False
            if event.key == K_RIGHT: # Check if the pressed key is right 
                moving_right = False
            if event.key == K_UP:
                moving_up = False
            if event.key == K_DOWN:
                moving_down = False

    #Debug Console
    #print('\n' * 100)
    print('[x,y]:' + str(c_x) +','+ str(c_y))
    #[y][x]
    pygame.display.update() # Update the display.
    pygame.display.set_caption('[LEVEL EDITOR][HELPv1] FPS:' + str(int(clock.get_fps()))) 
    screen.blit(pygame.transform.scale(display,WINDOW_SIZE),(0,0))
    clock.tick(60) # Cap the frame rate of the game to 60fps.

