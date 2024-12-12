import pygame, sys, random, time, logging, threading
from pygame.locals import QUIT
pygame.init()
global gravity, collision_immune, collision_time


#----------//Variables//----------

A_R_time = 3000
R_time = A_R_time#will be in milliseconds, count it with clocks like animation
Dmg = 10
Spd = 5
Ammo = 3
Ammo_count = Ammo
Size = 1
Num_Shots = 1
T_between_shots = 100
difficulty = "easy"
easy = 2
medium = 4
hard = 6
scale = 0.5
gravity = 0
clock = pygame.time.Clock()
collision_time = None

#----------//Variables End//----------

#----------//Boolean//----------
move_left = False
move_right = False
play = True
SR = False
SL = False
reload = False
shoot = False
right = False
left = False
collision = True
collision_immune = False
gravity_t = True
on_block = False
on_plat = False
Chest = True

#----------//Boolean End//----------



#----------//Colours//----------
colour = (255,0,0)
WHITE = (255,255,255)
font_color = (0,255,145)
GREY = (173,173,173)
BLACK = (000,000,000)
RED = (255,000,000)
GREEN = (000,255,000)


#----------//Colours End//----------

#----------//Co-ordinates//----------
x = 100
y = 100
xx = 800
yy = 800
sprite_sheet_image_x = 0
sprite_sheet_image_y = 760

#---------//Co-ordinates End//------------

#---------//Screen//----------

screen = pygame.display.set_mode((xx, yy))

#---------//Screen End//----------
#---------//Lists and Arrays//------------
level_design = [[]]

array1_1 = [[0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 2, 2, 0, 0, 0],
          [0, 0, 0, 2, 2, 0, 0, 0],
          [2, 2, 0, 0, 0, 0, 0, 0],
          [2, 2, 0, 0, 0, 0, 0, 0],
          ]
array1_2 = [[0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 2, 0],
          [0, 0, 0, 0, 0, 0, 2, 0],
          [0, 2, 2, 2, 2, 0, 2, 0],
          [0, 0, 0, 2, 2, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [2, 2, 0, 0, 0, 0, 0, 0],
          [2, 2, 0, 0, 0, 0, 0, 0],
          ]

array1_3 = [[0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 2, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 2, 2, 2, 0, 0, 0],
          [0, 0, 2, 2, 2, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          ]

array2_1 = [[2, 2, 0, 0, 0, 0, 0, 0],
          [2, 2, 0, 0, 0, 0, 0, 0],
          [2, 2, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 2, 2, 0, 0, 0],
          [0, 0, 0, 2, 2, 0, 0, 0],
          [0, 0, 0, 2, 2, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 2, 2],
          [0, 0, 0, 0, 0, 0, 2, 2],
          ]

array2_2 = [[2, 2, 0, 0, 0, 0, 0, 0],
          [2, 2, 0, 0, 0, 0, 0, 0],
          [2, 2, 0, 0, 0, 0, 2, 0],
          [0, 0, 0, 0, 0, 0, 2, 0],
          [0, 0, 0, 0, 0, 0, 2, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [2, 2, 2, 2, 2, 2, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 2],
          [0, 0, 0, 0, 0, 0, 0, 2],
          ]

array2_3 = [[2, 2, 0, 0, 0, 0, 0, 0],
          [2, 2, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 2, 0, 0, 2],
          [0, 0, 0, 0, 2, 0, 0, 2],
          [0, 0, 0, 0, 2, 0, 0, 2],
          [0, 0, 0, 0, 2, 0, 0, 0],
          [2, 0, 0, 0, 2, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 2],
          [0, 0, 0, 0, 0, 0, 0, 2],
          ]

array3_1 = [[0, 0, 0, 0, 0, 2, 0, 0],
          [0, 0, 2, 0, 0, 2, 0, 0],
          [0, 0, 2, 0, 0, 2, 0, 0],
          [0, 0, 0, 0, 0, 2, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [2, 2, 2, 0, 0, 0, 0, 0],
          [2, 2, 2, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          ]

array3_2 = [[0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [2, 2, 2, 0, 0, 0, 0, 0],
          [2, 2, 2, 0, 0, 2, 2, 0],
          [2, 2, 2, 0, 0, 2, 2, 0],
          [2, 2, 2, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          ]

array3_3 = [[0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 2, 0, 0, 2, 2, 2],
          [0, 0, 2, 0, 0, 2, 2, 2],
          [0, 0, 0, 0, 0, 2, 2, 2],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [2, 2, 2, 2, 0, 0, 0, 0],
          [2, 2, 2, 2, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          ]


array4_1 = [[0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 2, 2, 2, 2, 2, 0, 0],
          [0, 2, 2, 2, 2, 2, 0, 0],
          [0, 2, 2, 2, 2, 2, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          ]

array4_2 = [[0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 2, 2, 2, 2, 2, 0, 0],
          [0, 2, 2, 2, 2, 2, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 2, 0, 0, 2, 0, 0],
          [0, 0, 2, 0, 0, 2, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          ]

array4_3 = [[0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 2, 2, 2, 2, 2, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0],
          [0, 2, 2, 2, 0, 0, 2, 2],
          [0, 0, 0, 0, 0, 0, 2, 2],
          ]


         
#----------//Lists and Arrays End//----------

#----------//Establishing Images//----------
Background = pygame.image.load('Assets/background 2.png').convert()
sprite_sheet_image = pygame.image.load('Assets/Fridge Sprite.png').convert_alpha()
bullet_image = pygame.image.load('Assets/Meat1.png').convert_alpha()
bullet_image.set_colorkey(WHITE)
back = pygame.image.load('Assets/background.1.png').convert_alpha()
spike = pygame.image.load('Assets/spikes.png').convert_alpha()
wall = pygame.image.load('Assets/wall.png').convert_alpha()
platform = pygame.image.load('Assets/platform.png').convert_alpha()
floor = pygame.image.load('Assets/wall.png').convert_alpha()
space = pygame.image.load('Assets/background.png').convert_alpha()
c_door = pygame.image.load('Assets/door.png').convert_alpha()
o_door = pygame.image.load('Assets/door.png').convert_alpha()
chest = pygame.image.load('Assets/chest.png').convert_alpha()
spike = pygame.transform.scale(spike, (50,50))
wall = pygame.transform.scale(wall, (50,50))
platform = pygame.transform.scale(platform, (50,50))
back = pygame.transform.scale(back, (50,50))
floor = pygame.transform.scale(floor, (50,50))
space = pygame.transform.scale(back, (50,50))
chest = pygame.transform.scale(chest, (50,50))
bullet_sprite = pygame.sprite.Sprite()
bullet_sprite.image = bullet_image
bullet_sprite.rect = bullet_image.get_rect()

#----------//Establishing Images End//----------

#----------//Defining Classes//----------

#-----//Enemy Classes//-----
class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, image, E_hp):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Assets/Enemy.png').convert_alpha()
        self.image.convert_alpha()
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.counter = 0 #counter variable
        self.Eshoot = None
        self.E_hp = E_hp
       
       
    def move(self):
        distance = 160
        speed = 4 #will eventually change

        if self.counter >= 0 and self.counter <= distance:
            self.rect.x += speed
            Prob_shot = random.randint(1,100)
            if Prob_shot == 1:
                E_bullet_group_R.add(E_Bullet_R(self.rect.x, self.rect.y+50))
        elif self.counter >= distance and self.counter <= distance*2:
            self.rect.x -= speed
            Prob_shot = random.randint(1,100)
            if Prob_shot == 1:
                E_bullet_group_L.add(E_Bullet_L(self.rect.x, self.rect.y+50))
        else:
            self.counter = 0
           
        self.counter += 1

    def update(self):
        if self.E_hp > 0:
            hit_list = pygame.sprite.spritecollide(self, bullet_group_R, True)#built in collisions
            for bullet in hit_list:
                self.E_hp -= Dmg
                if self.E_hp < 0:
                    self.kill()
            hit_list = pygame.sprite.spritecollide(self, bullet_group_L, True)#built in collisions
            for bullet in hit_list:
                self.E_hp -= Dmg
                if self.E_hp < 0:
                    self.kill()
        elif self.E_hp <= 0:
            self.kill()
            #upgrade dropped function
           

#-----//Enemy Classes End//------

#-----//Player Class//-----

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.movex = 0
        self.movey = 0
        self.health = 10
        img = pygame.image.load('Assets/Fridge Sprite(1).png').convert()
        img.convert_alpha()#optimise alpha
        img.set_colorkey(GREY)
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

    def control(self, x, y):
        self.movex += x
        self.movey += y

    def create_bullet():
        if SR:
            return Bullet_R(player.rect.x, player.rect.y)
        if SL:
            return Bullet_L(player.rect.x, player.rect.y)
        else:
            pass

    def jump(self):
        global gravity, gravity_t
        if self.rect.y >= 760 or gravity == 0:
            gravity = - 30
        collide_list = pygame.sprite.spritecollide(self, block_list, False)
        for block in collide_list:
            if self.rect.y == block.rect.y+40:
                gravity -= 30

    def upgrade(self):
        rand_upgrade = random.randint(1,1)
        if rand_upgrade == 1:
            R_Time_mod(0.5)
            dmg_mod(0.5)
            Ammo_mod(3)
            Num_Shots_mod(5)
            print("stock up for winter")
        elif rand_upgrade == 2:
            R_Time_mod(2)
            dmg_mod(1.75)
            Spd_mod(0.75)
            #Size(1.5)
            print("Extra cool")
        elif rand_upgrade == 3:
            dmg_mod(1.5)
            Spd_mod(0.5)
            R_Time_mod(1.5)
            Num_Shots_mod(0.25)
            print("Freezer")
        elif rand_upgrade == 4:
            Spd_mod(2)
            dmg_mod(0.75)
            Num_Shots_mod(2)
            print("Ice Deposit")
        elif rand_upgrade == 5:
            Spd_mod(5)
            dmg_mod(0.25)
            R_time_mod(0.1)
            Ammo_mod(0.2)
            print("Turbo Charge")
        elif rand_upgrade == 6:
            #Size(2)
            Num_Shots_mod(1.5)
            dmg_mod(0.5)
       

    def update(self):
        global gravity, collision, collision_immune, collision_time, gravity_t, on_block, on_plat
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
        gravity += 1
        self.rect.y += gravity
        collide_list = pygame.sprite.spritecollide(self, block_list, False)
        for block in collide_list:
            if self.rect.x >= block.rect.x -50 and right == True and on_block == False:#left block collision
                self.rect.x = block.rect.x -50 #new variable
            elif self.rect.x <= block.rect.x +50 and left == True and on_block == False:#right block collision
                self.rect.x = block.rect.x +50#new variable
            elif self.rect.y >= block.rect.y-40:
                gravity = 0
                self.rect.y = block.rect.y-40
                on_block = True #new variable
            elif self.rect.y <= block.rect.y+40 and on_block == True:
                self.rect.y = block.rect.y+50
            elif self.rect.y == block.rect.y:
                self.rect.y = block.rect.y
        if self.rect.y >= 760:
            self.rect.y = 760
            gravity = 0
        if collision == True:
            if collision_immune == False:
                hit_list = pygame.sprite.spritecollide(self, enemy_list, False)#built in collisions
                for enemy in hit_list:
                    self.health -= 1
                    collision_time = pygame.time.get_ticks()
                    collision_immune = True
            elif collision_immune == True:
                if pygame.time.get_ticks() - collision_time > 500:
                    collision_immune = False
        plat_list = pygame.sprite.spritecollide(self, platform_list, False)
        for platform in plat_list:
            if self.rect.y >= platform.rect.y-40 and on_plat == False:
                gravity = 0
                self.rect.y = platform.rect.y-40
                on_plat = True
        if gravity >= 1:#gravity only goes up if player sprite isnt on a block, it gets set back to zero each time,
            on_block = False
            on_plat = False
        chest_collide = pygame.sprite.spritecollide(self, chest_list, True)
        for chest in chest_collide:
            player.upgrade()
            #upgradeclass
           

#-----//Player Class End//-----

class drop_chest(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load('Assets/chest.png').convert_alpha()
        self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

       
#-----//Bullet Classes//-----

class Bullet_R(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()#gives __init __ access to methods and properties of parent/sibling class
        self.image = pygame.Surface((50*scale, 10*scale))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(center = (pos_x, pos_y))
       
    def update(self, vel):#runs when update class which updates everything.
        if x <= 820:
            self.rect.x += vel
       

class Bullet_L(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()#gives __init __ access to methods and properties of parent/sibling class
        self.image = pygame.Surface((50*scale, 10*scale))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(center = (pos_x, pos_y))
       
    def update(self, vel):#runs when update class which updates everything.
        if x >= 0:
            self.rect.x -= vel

class E_Bullet_R(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()#gives __init __ access to methods and properties of parent/sibling class
        self.image = pygame.Surface((50*scale, 10*scale))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(center = (pos_x, pos_y))
       
    def update(self, vel):#runs when update class which updates everything.
        if x <= 820:
            self.rect.x += vel

class E_Bullet_L(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()#gives __init __ access to methods and properties of parent/sibling class
        self.image = pygame.Surface((50*scale, 10*scale))
        self.image.fill((255,0,0))
        self.rect = self.image.get_rect(center = (pos_x, pos_y))
       
    def update(self, vel):#runs when update class which updates everything.
        if x <= 820:
            self.rect.x -= vel
   

#-----//Bullet Classes End//-----

#-----//Collision Object//-----

class collision(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
       

    def blocks(self, array_1, array_2, array_3, array_4):
        V = 16
        TILE_WIDTH = 50
        TILE_HEIGHT = 50
        row_count = 0
        for row in array_1:
            column_count = 0
            for tile in row:
                if tile == 0:
                    backSprite = pygame.sprite.Sprite()
                    backSprite.image = back
                    backSprite.rect = back.get_rect()
                    backSprite.rect.x = TILE_WIDTH * row_count
                    backSprite.rect.y = TILE_HEIGHT * column_count
                    level_list.add(backSprite)
                if tile == 1:
                    backSprite = pygame.sprite.Sprite()
                    backSprite.image = back
                    backSprite.rect = back.get_rect()
                    backSprite.rect.x = TILE_WIDTH * row_count
                    backSprite.rect.y = TILE_HEIGHT * column_count
                    level_list.add(backSprite)
                if tile == 2:
                    wallSprite = pygame.sprite.Sprite()
                    wallSprite.image = wall
                    wallSprite.rect = wall.get_rect()
                    wallSprite.rect.x = TILE_WIDTH * row_count
                    wallSprite.rect.y = TILE_HEIGHT * column_count
                    level_list.add(wallSprite)
                    block_list.add(wallSprite)
                if tile == 3:
                    platformSprite = pygame.sprite.Sprite()
                    platformSprite.image = platform
                    platformSprite.rect = platform.get_rect()
                    platformSprite.rect.x = TILE_WIDTH * row_count
                    platformSprite.rect.y = TILE_HEIGHT * column_count
                    level_list.add(platformSprite)
                    platform_list.add(platformSprite)
                if tile == 4:
                    spikesSprite = pygame.sprite.Sprite()
                    spikesSprite.image = spike
                    spikesSprite.rect = spike.get_rect()
                    spikesSprite.rect.x = TILE_WIDTH * row_count
                    spikesSprite.rect.y = TILE_HEIGHT * column_count
                    level_list.add(spikesSprite)
                    spike_list.add(spikesSprite)
                column_count += 1
            row_count += 1

        row_count = 0
        for row in array_2:
            column_count = 0
            for tile in row:
                if tile == 0:
                    backSprite = pygame.sprite.Sprite()
                    backSprite.image = back
                    backSprite.rect = back.get_rect()
                    backSprite.rect.x = TILE_WIDTH * row_count
                    backSprite.rect.y = TILE_HEIGHT * column_count
                    backSprite.rect.x += 400
                    level_list.add(backSprite)
                if tile == 1:
                    backSprite = pygame.sprite.Sprite()
                    backSprite.image = back
                    backSprite.rect = back.get_rect()
                    backSprite.rect.x = TILE_WIDTH * row_count
                    backSprite.rect.y = TILE_HEIGHT * column_count
                    backSprite.rect.x += 400
                    level_list.add(backSprite)
                if tile == 2:
                    wallSprite = pygame.sprite.Sprite()
                    wallSprite.image = wall
                    wallSprite.rect = wall.get_rect()
                    wallSprite.rect.x = TILE_WIDTH * row_count
                    wallSprite.rect.y = TILE_HEIGHT * column_count
                    wallSprite.rect.x += 400
                    level_list.add(wallSprite)
                    block_list.add(wallSprite)
                if tile == 3:
                    platformSprite = pygame.sprite.Sprite()
                    platformSprite.image = platform
                    platformSprite.rect = platform.get_rect()
                    platformSprite.rect.x = TILE_WIDTH * row_count
                    platformSprite.rect.y = TILE_HEIGHT * column_count
                    platformSprite.rect.x += 400
                    level_list.add(platformSprite)
                    platform_list.add(platformSprite)
                if tile == 4:
                    spikesSprite = pygame.sprite.Sprite()
                    spikesSprite.image = spike
                    spikesSprite.rect = spike.get_rect()
                    spikesSprite.rect.x = TILE_WIDTH * row_count
                    spikesSprite.rect.y = TILE_HEIGHT * column_count
                    spikesSprite.rect.x += 400
                    level_list.add(spikesSprite)
                    spike_list.add(spikesSprite)
                column_count += 1
            row_count += 1

        row_count = 0
        for row in array_3:
            column_count = 0
            for tile in row:
                if tile == 0:
                    backSprite = pygame.sprite.Sprite()
                    backSprite.image = back
                    backSprite.rect = back.get_rect()
                    backSprite.rect.x = TILE_WIDTH * row_count
                    backSprite.rect.y = TILE_HEIGHT * column_count
                    backSprite.rect.y += 400
                    level_list.add(backSprite)
                if tile == 1:
                    backSprite = pygame.sprite.Sprite()
                    backSprite.image = back
                    backSprite.rect = back.get_rect()
                    backSprite.rect.x = TILE_WIDTH * row_count
                    backSprite.rect.y = TILE_HEIGHT * column_count
                    backSprite.rect.y += 400
                    level_list.add(backSprite)
                if tile == 2:
                    wallSprite = pygame.sprite.Sprite()
                    wallSprite.image = wall
                    wallSprite.rect = wall.get_rect()
                    wallSprite.rect.x = TILE_WIDTH * row_count
                    wallSprite.rect.y = TILE_HEIGHT * column_count
                    wallSprite.rect.y += 400
                    level_list.add(wallSprite)
                    block_list.add(wallSprite)
                if tile == 3:
                    platformSprite = pygame.sprite.Sprite()
                    platformSprite.image = platform
                    platformSprite.rect = platform.get_rect()
                    platformSprite.rect.x = TILE_WIDTH * row_count
                    platformSprite.rect.y = TILE_HEIGHT * column_count
                    platformSprite.rect.y += 400
                    level_list.add(platformSprite)
                    platform_list.add(platformSprite)
                if tile == 4:
                    spikesSprite = pygame.sprite.Sprite()
                    spikesSprite.image = spike
                    spikesSprite.rect = spike.get_rect()
                    spikesSprite.rect.x = TILE_WIDTH * row_count
                    spikesSprite.rect.y = TILE_HEIGHT * column_count
                    spikesSprite.rect.y += 400
                    level_list.add(spikesSprite)
                    spike_list.add(spikesSprite)
                column_count += 1
            row_count += 1

        row_count = 0
        for row in array_4:
            column_count = 0
            for tile in row:
                if tile == 0:
                    backSprite = pygame.sprite.Sprite()
                    backSprite.image = back
                    backSprite.rect = back.get_rect()
                    backSprite.rect.x = TILE_WIDTH * row_count
                    backSprite.rect.y = TILE_HEIGHT * column_count
                    backSprite.rect.x += 400
                    backSprite.rect.y += 400
                    level_list.add(backSprite)
                if tile == 1:
                    backSprite = pygame.sprite.Sprite()
                    backSprite.image = back
                    backSprite.rect = back.get_rect()
                    backSprite.rect.x = TILE_WIDTH * row_count
                    backSprite.rect.y = TILE_HEIGHT * column_count
                    backSprite.rect.x += 400
                    backSprite.rect.y += 400
                    level_list.add(backSprite)
                if tile == 2:
                    wallSprite = pygame.sprite.Sprite()
                    wallSprite.image = wall
                    wallSprite.rect = wall.get_rect()
                    wallSprite.rect.x = TILE_WIDTH * row_count
                    wallSprite.rect.y = TILE_HEIGHT * column_count
                    wallSprite.rect.x += 400
                    wallSprite.rect.y += 400
                    level_list.add(wallSprite)
                    block_list.add(wallSprite)
                if tile == 3:
                    platformSprite = pygame.sprite.Sprite()
                    platformSprite.image = platform
                    platformSprite.rect = platform.get_rect()
                    platformSprite.rect.x = TILE_WIDTH * row_count
                    platformSprite.rect.y = TILE_HEIGHT * column_count
                    platformSprite.rect.x += 400
                    platformSprite.rect.y += 400
                    level_list.add(platformSprite)
                    platform_list.add(platformSprite)
                if tile == 4:
                    spikesSprite = pygame.sprite.Sprite()
                    spikesSprite.image = spike
                    spikesSprite.rect = spike.get_rect()
                    spikesSprite.rect.x = TILE_WIDTH * row_count
                    spikesSprite.rect.y = TILE_HEIGHT * column_count
                    spikesSprite.rect.x += 400
                    spikesSprite.rect.y += 400
                    level_list.add(spikesSprite)
                    spike_list.add(spikesSprite)
                column_count += 1
            row_count += 1


#----------//Classes End//----------

#----------//Functions//----------

def random_level():
        random.shuffle(partial_1_1)
        tile_list = partial_1_1
        tile_ = read_level_1(tile_list)
        draw_level(tile_)
        pygame.display.update()
        return tile_

def ammo_dis(b):#ammo display, #b is for bullets
    x_co = 650
    y_co = 25
    for i in range(b):
        ammo_rect = pygame.draw.rect(screen, (255,255,0), pygame.Rect(x_co, y_co, 10, 10))
        x_co += 15
        if x_co >= 790:
            y_co += 15
            x_co = 650

def i_r():#increase reload
    global R_time
    global A_R_time
    R_time += A_R_time


def reload_(r_t):#r_t is the relaod time
    tck = pygame.time.get_ticks()
    n_tck = tck - r_t
    if n_tck >= 0:
        reload = False
        Ammo_count = Ammo
        i_r()#increase reload function
        return Ammo_count
    elif n_tck < 0:
        reload = True
        Ammo_count = 0
        return Ammo_count

def R_Time_mod(mod):
    global R_time
    R_time = R_time*mod

def dmg_mod(mod):
    global Dmg
    Dmg = Dmg*mod

def Spd_mod(mod):
    global Spd
    Spd = Spd*mod

def Ammo_mod(mod):
    global Ammo
    Ammo = Ammo*mod

def Size_mod(mod):
    Size = Size*mod

def Num_Shots_mod(mod):
    global Num_Shots
    Num_Shots = Num_Shots*mod

   
#-----//Object Collisions//-------




#-----------//Functions End//----------

#-----------//Creating Sprites//----------
player = Player()   # spawn player
player.rect.x = sprite_sheet_image_x#go to x
player.rect.y = sprite_sheet_image_y#go to y
player_list = pygame.sprite.Group()
player_list.add(player)
bullet_group_R = pygame.sprite.Group()
bullet_group_L = pygame.sprite.Group()
E_bullet_group_R = pygame.sprite.Group()
E_bullet_group_L = pygame.sprite.Group()
enemy = Enemy(0, 700, 'Enemy.png', 40)
enemy_list = pygame.sprite.Group()
enemy_list.add(enemy)
level_list = pygame.sprite.Group()
block_list = pygame.sprite.Group()
platform_list = pygame.sprite.Group()
door_list = pygame.sprite.Group()
spike_list = pygame.sprite.Group()
chest_list = pygame.sprite.Group()

#----------//Creating Sprites End//------------
level = collision()
level.blocks(array1_1, array2_2, array3_2, array4_3)
#----------//Main Loop//------------
while True:
#-----//Background//-----
    screen.blit(Background, (0,0))
#-----//Background End//------
   
#-----//Controls//-----
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
           
        if event.type == pygame.KEYDOWN:#makes the key pressed only happen once
            if event.key == pygame.K_ESCAPE:#checks if it is the escape key
                pygame.quit()
                sys.exit()#if it is it quits
               
            if event.key == pygame.K_a:
                player.control(-Spd, 0)
                left = True
                action = 2
               
            elif event.key == pygame.K_d:
                player.control(Spd, 0)
                right = True
                action = 2
               
            elif event.key == pygame.K_SPACE:
                player.jump()#player class                

            elif event.key == pygame.K_RIGHT:
                SR = True
                SL = False
                if Ammo_count > 0:
                    Ammo_count -= Num_Shots #add if statement where if it goes to less than zero you reload instead.
                    for i in range(Num_Shots):
                        bullet_group_R.add(Player.create_bullet())
                elif Ammo_count <=0:
                    reload = True
           
            elif event.key == pygame.K_LEFT:
                SR = False
                SL = True
                if Ammo_count > 0:
                    Ammo_count -= Num_Shots #add if statement where if it goes to less than zero you reload instead.
                    for i in range(Num_Shots):#shoots the amount of shots that come out at once.
                        bullet_group_L.add(Player.create_bullet())
                elif Ammo_count <=0:
                    reload = True
               
            frame = 0
           
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                player.control(-Spd, 0)
                right = False
           
            elif event.key == pygame.K_a:
                player.control(Spd, 0)
                left = False
               
            action = 0
            frame = 0
    if reload:
        Ammo_count = reload_(R_time)
        reload = False
    if right:
        sprite_sheet_image_x += Spd
    if left:
        sprite_sheet_image_x -= Spd
    if left and right != True:
        pass

    if not enemy_list and Chest == True:
        Chest = False
        chest = drop_chest(40, 750)
        chest_list.add(chest)
       
#-----//Controls End//-----


#-----//Processes//-----
    bullet_group_R.update(Spd)
    bullet_group_L.update(Spd)
    E_bullet_group_R.update(Spd)
    E_bullet_group_L.update(Spd)
    player.update()
    enemy.update()
    ammo_dis(Ammo_count)
    bullet_group_R.draw(screen)
    bullet_group_L.draw(screen)
    E_bullet_group_R.draw(screen)
    E_bullet_group_L.draw(screen)
    player_list.draw(screen)
    enemy_list.draw(screen)
    level_list.draw(screen)
    chest_list.draw(screen)

#-----//Processes End//-----

#-----//Enemy Movement//-----
    for e in enemy_list:
        e.move()
#-----//Updating Screen//-----
    pygame.display.update()
    clock.tick(60)
