import pygame
import sys
import random
from spritesheet import Spritesheet

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

# Set up the display
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Planet Heatwave")
clock = pygame.time.Clock()
font = pygame.font.SysFont("None", 25)
last_updated = pygame.time.get_ticks()
animation_cooldown = 70

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Music
music=pygame.mixer.music.load("sfx/PHTrack1.mp3")
music2=pygame.mixer.music.load("sfx/PHTrack2.mp3")
pygame.mixer.music.play(-1)

all_sprites = pygame.sprite.Group()

player_sprites = Spritesheet('gfx/Sprite-0007.png')

still_frame = player_sprites.get_sprite(0,0,32,48)
walking_frames = [player_sprites.parse_sprite('Sprite-0007 0.'),player_sprites.parse_sprite('Sprite-0007 1.'),player_sprites.parse_sprite('Sprite-0007 2.'),player_sprites.parse_sprite('Sprite-0007 3.'),player_sprites.parse_sprite('Sprite-0007 4.'),player_sprites.parse_sprite('Sprite-0007 5.'),player_sprites.parse_sprite('Sprite-0007 6.'),player_sprites.parse_sprite('Sprite-0007 7.'),player_sprites.parse_sprite('Sprite-0007 8.'),player_sprites.parse_sprite('Sprite-0007 9.')]
index = 0

# Player class
class Player(pygame.sprite.Sprite):
    global timer
    def __init__(self):
        super().__init__()
        self.image = still_frame
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed = 4
        self.timer = 0
        self.heat = 0
        self.heat_limit = 20

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.rect.y -= self.speed
            player.image = walking_frames[index]
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            player.image = walking_frames[index]
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.rect.y += self.speed    
            player.image = walking_frames[index]
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            player.image = pygame.transform.flip(walking_frames[index], True, False)
        
    def heat_meter(self):
        pygame.draw.rect(SCREEN, BLACK, (SCREEN_WIDTH-50, 50, 30, SCREEN_HEIGHT-100), 1)
        pygame.draw.rect(SCREEN, (255,0,0), (SCREEN_WIDTH-50, 50, 30, self.heat))

        self.timer += 1
        if self.timer >= self.heat_limit:
            self.heat += 10
            self.timer = 0

# Create a player instance
player = Player()
all_sprites.add(player)

guide_status = False
def guide():
    global guide_status
    guide_surf = pygame.image.load('gfx/guide.png'). convert_alpha()
    guide_x = pygame.image.load('gfx/x_btn.png').convert_alpha()
    guide_x_rect = pygame.Rect(585,65,50,50)

    while guide_status:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if guide_x_rect.collidepoint(mouse_pos):
                        guide_status = False
                        main_menu()
        SCREEN.blit(guide_surf, (150,50))
        SCREEN.blit(guide_x, guide_x_rect)
        pygame.display.flip()

# Text and buttons
title_text = pygame.image.load("gfx/title.png").convert_alpha()
play_button_surf = pygame.image.load("gfx\play_btn.png").convert_alpha()
play_button_rect = pygame.Rect(SCREEN_WIDTH/2-150, 90, 300, 80)
guide_button_surf = pygame.image.load("gfx\guide_btn.png").convert_alpha()
guide_button_rect = pygame.Rect(SCREEN_WIDTH/2-150, 290, 300, 80)    
quit_button_surf = pygame.image.load("gfx\quit_btn.png").convert_alpha()
quit_button_rect = pygame.Rect(SCREEN_WIDTH/2-150, 490, 300, 80)

overheated_text = pygame.image.load("gfx/overheated.png").convert_alpha()
restart_surf = pygame.image.load("gfx/restart_btn.png").convert_alpha()
restart_rect = pygame.Rect(SCREEN_WIDTH/2-150,260, 300,80)

stars = pygame.image.load("gfx/stars.png").convert_alpha()

# Main menu
main_menu_status = True
def main_menu():
    global main_menu_status, guide_status
    
    while main_menu_status:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if play_button_rect.collidepoint(mouse_pos):
                    main_menu_status = False
                elif quit_button_rect.collidepoint(mouse_pos):
                    pygame.quit()
                elif guide_button_rect.collidepoint(mouse_pos):
                    guide_status = True
                    guide()

        SCREEN.blit(stars, (0,0))
        SCREEN.blit(title_text, (SCREEN_WIDTH/2-250, 30))
        SCREEN.blit(play_button_surf, play_button_rect)
        SCREEN.blit(quit_button_surf, quit_button_rect)
        SCREEN.blit(guide_button_surf, guide_button_rect)

        pygame.display.flip()
        clock.tick(60)

# go here first
main_menu()

mineral_surf = pygame.image.load("gfx/mineral_F.png")
mineral_surf = pygame.transform.scale(mineral_surf, (40,37))
mineral_rect = pygame.Rect(random.randint(50,720),random.randint(50,550),18,18)
mineral_count = 0

planet1_bg = pygame.image.load("gfx/planet1_bg.png").convert_alpha()

spaceship_surf = pygame.image.load("gfx/ship.png").convert_alpha()
spaceship_surf = pygame.transform.scale(spaceship_surf, (64,64))
spaceship_rect = pygame.Rect(SCREEN_WIDTH-150, 100, 35,35)

win_text = pygame.image.load("gfx/win.png").convert_alpha()
warning_text = font.render("Get back to your ship!", True, BLACK)

# The levels
planet1_status = False
def planet1_env():
    global planet1_status, main_menu_status, mineral_count, last_updated, animation_cooldown, index
    player.rect.x = SCREEN_WIDTH-150
    player.rect.y = 100
    while planet1_status:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if player.heat == 500 or player.heat == 0:
                    if restart_rect.collidepoint(mouse_pos):
                        player.heat = 0
                        mineral_count = 0
                        planet1_env()
                    elif quit_button_rect.collidepoint(mouse_pos):
                        planet1_status = False
                        main_menu_status = True
                        player.heat = 0
                        mineral_count = 0
                        main_menu()
        
        current_time = pygame.time.get_ticks()
        if current_time - last_updated > animation_cooldown:  
            index = (index + 1) % len(walking_frames)
            last_updated = current_time

        if player.rect.colliderect(mineral_rect):
            mineral_rect.x = random.randint(50,750)
            mineral_rect.y = random.randint(50,550)
            mineral_count += 1

        all_sprites.update()
        SCREEN.blit(planet1_bg, (0,0))
        SCREEN.blit(spaceship_surf, spaceship_rect)

        SCREEN.blit(mineral_surf, mineral_rect)
        mineral_count_text = font.render(f"Minerals: {mineral_count}/10", True, BLACK)
        SCREEN.blit(mineral_count_text, (50,50))

        if mineral_count >= 10:
            SCREEN.blit(warning_text, (SCREEN_WIDTH-200, 20))
        
            
        if player.rect.colliderect(spaceship_rect):
            if mineral_count >= 10:
                player.heat = 0
                SCREEN.blit(win_text, (SCREEN_WIDTH/2-150, 100))
                SCREEN.blit(restart_surf, restart_rect)
                SCREEN.blit(quit_button_surf, quit_button_rect)

        player.heat_meter()
        if player.heat >= 500:
            player.rect.x = SCREEN_WIDTH-150
            player.rect.y = 100
            player.heat = 500
            SCREEN.blit(overheated_text, (SCREEN_WIDTH/2-230,100))
            SCREEN.blit(restart_surf, restart_rect)
            SCREEN.blit(quit_button_surf, quit_button_rect)
            
        all_sprites.draw(SCREEN)

        pygame.display.flip()
        clock.tick(60)

# i dont think planet 2 or 3 will get done
planet2_status = False
def planet2_env():
    print("Planet 2 environment")
    while planet2_status:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        

        all_sprites.update()
        SCREEN.fill(WHITE)
        player.heat_meter()
        if player.heat >= 500:
            print("You overheated!")
            planet2_status = False
        all_sprites.draw(SCREEN)

        pygame.display.flip()
        clock.tick(60)
    # what kind of loot is here?
    # background image?

planet3_status = False
def planet3_env():
    print("Planet 3 environment")
    while planet3_status:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        

        all_sprites.update()
        SCREEN.fill(WHITE)
        player.heat_meter()
        if player.heat >= 500:
            print("You overheated!")
            planet1_status = False
        all_sprites.draw(SCREEN)

        pygame.display.flip()
        clock.tick(60)
    # what kind of loot is here?
    # background image?

# menu planet objects
locked_surf = pygame.image.load("gfx/planet_select/lock.png").convert_alpha()

planet1_select_text = font.render("Planet Glarbin Shmargin", None, WHITE)
planet1_select_surf = pygame.image.load("gfx/planet_select/planet1.png").convert_alpha()
planet1_select_rect = pygame.Rect(100,130, 100,100)
planet1_locked = False

planet2_select_text = font.render("Planet Wikky Blikky", None, WHITE)
planet2_select_surf = pygame.image.load("gfx/planet_select/planet2.png").convert_alpha()
planet2_select_rect = pygame.Rect(250,350, 100,100)
planet2_locked = True

planet3_select_text = font.render("Planet Ronuld Bukets", None, WHITE)
planet3_select_surf = pygame.image.load("gfx/planet_select/planet3.png").convert_alpha()
planet3_select_rect = pygame.Rect(560,240, 100,100)
planet3_locked = True

# Select planet
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("Pause")
                main_menu_status = True
                main_menu()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if planet1_select_rect.collidepoint(mouse_pos):
                if planet1_locked != True:
                    planet1_status = True
                    planet1_env()
                else:
                    print("Planet is locked")
            elif planet2_select_rect.collidepoint(mouse_pos):
                if planet2_locked != True:
                    planet2_env()
                else:
                    print("Planet is locked")
            elif planet3_select_rect.collidepoint(mouse_pos):
                if planet3_locked != True:
                    planet3_env()
                else:
                    print("Planet is locked")

    # Draw everything
    SCREEN.blit(stars, (0,0))

    SCREEN.blit(planet1_select_text, (60, 100))
    SCREEN.blit(planet1_select_surf, planet1_select_rect)

    SCREEN.blit(planet2_select_text, (230, 320))
    SCREEN.blit(planet2_select_surf, planet2_select_rect)
    SCREEN.blit(locked_surf, (260,360))

    SCREEN.blit(planet3_select_text, (540, 210))
    SCREEN.blit(planet3_select_surf, planet3_select_rect)
    SCREEN.blit(locked_surf, (570,250))


    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()