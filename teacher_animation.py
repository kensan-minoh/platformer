import pygame
import random
from pygame.math import Vector2


class Game():
    def __init__(self, main_tile_group, dirt_tile_group, grass_tile_group, water_tile_group, player_group):
        self.dirt_image = pygame.image.load('dirt.png')
        self.grass_image = pygame.image.load('grass.png')
        self.water_image = pygame.image.load('water.png')
        self.game_music = pygame.mixer.music.load('game_music.wav')

        self.player = None
        self.main_tile_group = main_tile_group
        self.dirt_tile_group = dirt_tile_group
        self.grass_tile_group = grass_tile_group
        self.water_tile_group = water_tile_group
        self.player_group = player_group

        # create the tile map: 0 -> no tile, 1 -> dirt, 2 - > grass, 3 - > water
        # 20 rows and 30 columns
        self.tile_map = [
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [ 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [ 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2],
            [ 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [ 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2],
            [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [ 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2],
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1],
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1, 1, 1]
        ]

        self.create_tile()

    def update(self):
        pass

    def play_music(self):
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(loops=-1)

    def create_tile(self):
        for i in range(len(self.tile_map)):
            for j in range(len(self.tile_map[i])):
                if self.tile_map[i][j] == 1:
                    Tile(self.dirt_image, j*32, i*32, [self.main_tile_group, self.dirt_tile_group])
                elif self.tile_map[i][j] == 2:
                    Tile(self.grass_image, j*32, i*32, [self.main_tile_group, self.grass_tile_group])
                elif self.tile_map[i][j] == 3:
                    Tile(self.water_image, j*32, i*32, [self.main_tile_group, self.water_tile_group])
                elif self.tile_map[i][j] == 4:
                    self.player = Player(j*32, i*32-32, self.dirt_tile_group, self.grass_tile_group, self.water_tile_group,self.player_group)

class Tile(pygame.sprite.Sprite):
    def __init__(self, image, x, y, group):
        super().__init__(group)
        self.image = image
        self.rect = self.image.get_rect(topleft=(x,y))

    def update(self):
        pass

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, dirt_tile_group, grass_tile_group, water_tile_group, group):
        super().__init__(group)
        
        self.splash_sound = pygame.mixer.Sound("splash_sound.mp3")
        self.jump_sound = pygame.mixer.Sound("jump_sound.mp3")
        self.jump_sound.set_volume(0.2)
        # self.animation_run_right = []
        # for i in range(8):
        #     self.animation_run_right.append(pygame.image.load(f"boy/Run ({i+1}).png"))
        self.animation_idle_right = [pygame.transform.scale(pygame.image.load(f"boy/Idle ({i+1}).png").convert_alpha(),(64, 64)) for i in range(10)]
        self.animation_idle_left = [pygame.transform.flip(surf, True, False) for surf in self.animation_idle_right]
        self.animation_run_right = [pygame.transform.scale(pygame.image.load(f"boy/Run ({i+1}).png").convert_alpha(),(64, 64)) for i in range(8)]
        self.animation_run_left = [pygame.transform.flip(surf, True, False) for surf in self.animation_run_right]
        self.animation_jump_right = [pygame.transform.scale(pygame.image.load(f"boy/Jump ({i+1}).png").convert_alpha(),(64, 64)) for i in range(12)]
        self.animation_jump_left = [pygame.transform.flip(surf, True, False) for surf in self.animation_jump_right]


        self.animation_sprite= self.animation_idle_right
        self.current_sprite = 0

        self.facing = "right"

        self.starting_x = x
        self.starting_y = y
        self.image = self.animation_sprite[self.current_sprite]
        self.rect = self.image.get_rect(topleft=(self.starting_x, self.starting_y))
        self.dirt_tile_group = dirt_tile_group
        self.grass_tile_group = grass_tile_group
        self.water_tile_group = water_tile_group

        # kinematic constants
        self.HORIZONTAL_ACCELERATION = 0.5
        self.HORIZONTAL_FRICTION = 0.05
        self.VERTICAL_ACCELERATION = 0.5  # gravity
        self.VERTICAL_JUMP_SPEED = 15   # determine how high we can jump

        # kinematic values
        self.position = Vector2(x, y)
        self.velocity = Vector2(0, 0)

        # vertical acceleration (gravity) is present always regardless of key presses
        self.acceleration = Vector2(0, self.VERTICAL_ACCELERATION)

        # flags
        self.is_grounded =False
        
    def update(self):
        self.move()
        self.check_touch_dirt()
        self.check_touch_grass()
        self.check_touch_water()
        self.animation()


    def animation(self):
        self.current_sprite += 0.4
        if self.current_sprite >= len(self.animation_sprite):
            if self.is_grounded:
                self.current_sprite = 0
            else:
                self.current_sprite = len(self.animation_sprite) - 1
        # print(self.current_sprite, int(self.current_sprite))
        self.image = self.animation_sprite[int(self.current_sprite)]

        pygame.time.wait(0)


    
    def check_touch_dirt(self):
        collided_platform = pygame.sprite.spritecollideany(self, self.dirt_tile_group)
        if collided_platform:
            
            self.velocity.y = 0
            self.position.y = collided_platform.rect.bottom

    def move(self):
        # horizontal movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.acceleration.x = self.HORIZONTAL_ACCELERATION
            self.facing = 'right'

            self.animation_sprite =  self.animation_run_right

        elif keys[pygame.K_LEFT]:
            self.acceleration.x = - self.HORIZONTAL_ACCELERATION
            self.facing = 'left'
            self.animation_sprite =  self.animation_run_left

        # if there is no force(no key presses) acting on the player then acceleration should be 0
        else:
            self.acceleration.x = 0
            if self.facing == "right":
                self.animation_sprite = self.animation_idle_right
                if not self.is_grounded and self.velocity.y < 0:
                    self.animation_sprite = self.animation_jump_right
            else:
                self.animation_sprite = self.animation_idle_left
                if not self.is_grounded and self.velocity.y < 0:
                    self.animation_sprite = self.animation_jump_left
                        

           


        # calculate new kinematic values　摩擦力を速度に比例する加速度として計算し、運動方程式に組み込む
        self.acceleration.x -= self.velocity.x * self.HORIZONTAL_FRICTION
        self.velocity += self.acceleration

        # more simply 速度に減衰率をかける方法(上記２行に代えて)
        # self.velocity += self.acceleration
        # self.velocity.x *= 0.95

        # self.position += self.velocity #後退オイラー法
        self.position += self.velocity + 0.5 * self.acceleration #速度ベルレ法

        # wrap around motion
        if self.position.x >= WINDOW_WIDTH:
            self.position.x = 0
        elif self.position.x <= -64:
            self.position.x = WINDOW_WIDTH
        
        # new rect based on kinematic calculations
        self.rect.topleft = (int(self.position.x), int(self.position.y))  

    def check_touch_grass(self):
        # check for collisions with the grass tile
        collided_platform = pygame.sprite.spritecollideany(self, self.grass_tile_group)
        if collided_platform and self.velocity.y > 0:
            self.position.y = collided_platform.rect.top - 62 
            # ここがポイント　確実にcollidedの状態にしておく
            # -64とすると２つのspriteはcollideしないことになるのでelseの処理になって不都合
            # -62としてcollide状態を保っておく
            self.velocity.y = 0
            #self.acceleration.y = 0.5
            self.is_grounded = True
        else:
            #self.acceleration.y = 0.5
            self.is_grounded = False
        

    def check_touch_water(self):  
        # check for collisions with the water tile
        if pygame.sprite.spritecollideany(self, self.water_tile_group):
            self.splash_sound.play()
            self.reset_player()

    def jump(self):
        if self.is_grounded:
            self.velocity.y = -1 * self.VERTICAL_JUMP_SPEED
            self.jump_sound.play()
            self.current_sprite = 0
            # if self.facing == "right":
            #     self.animation_sprite = self.animation_jump_right
            # else:
            #     self.animation_sprite = self.animation_jump_left
            self.is_grounded = False


    def reset_player(self):
        self.position = Vector2(self.starting_x, self.starting_y)
        self.velocity = Vector2(0, 0)

# initialize pygame
pygame.init()

# set display surface ( tile size is 32 by 32 so 30 tiles wide and 20 tiles high)
WINDOW_WIDTH = 960
WINDOW_HEIGHT = 640

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Making a tile map")

# load the background image
background_image = pygame.image.load('background1.png')
background_rect = background_image.get_rect(topleft=(0,0))

# set FPS and clock
FPS = 60
clock = pygame.time.Clock()

# create sprite groups
main_tile_group = pygame.sprite.Group()
dirt_tile_group = pygame.sprite.Group()
grass_tile_group = pygame.sprite.Group()
water_tile_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

my_game = Game(main_tile_group, dirt_tile_group, grass_tile_group, water_tile_group, player_group)
my_game.play_music()
# player = Player(WINDOW_WIDTH//2, WINDOW_HEIGHT-96, player_group)
my_player = player_group.sprites()[0]


# main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # player wants to jump
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                my_player.jump()

    # fill the background
    display_surface.blit(background_image, background_rect)

    main_tile_group.update()
    main_tile_group.draw(display_surface)
    player_group.update()
    player_group.draw(display_surface)

    pygame.display.update()

    clock.tick(FPS)

# end the game

pygame.quit()




