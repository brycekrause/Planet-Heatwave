import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

# Set up the display
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Planet Heatwave")
clock = pygame.time.Clock()
font = pygame.font.SysFont("None", 25)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Player class
class Player(pygame.sprite.Sprite):
    global timer
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("gfx/img.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed = 5
        self.timer = 0
        self.heat = 0
        self.heat_limit = 20

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.rect.y += self.speed    
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        
    def heat_meter(self):
        pygame.draw.rect(SCREEN, BLACK, (SCREEN_WIDTH-50, 50, 30, SCREEN_HEIGHT-100), 1)
        pygame.draw.rect(SCREEN, (255,0,0), (SCREEN_WIDTH-50, 50, 30, self.heat))

        self.timer += 1
        print(self.timer)
        if self.timer >= self.heat_limit:
            self.heat += 10
            self.timer = 0
        print(self.heat)

# Create a player instance
player = Player()
all_sprites = pygame.sprite.Group()
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

# Main menu
main_menu_status = True
def main_menu():
    global main_menu_status, guide_status
    print("mainmenu")
    title_text = font.render("Planet Heatwave", None, BLACK)
    play_button_surf = pygame.image.load("gfx\play_btn.png").convert_alpha()
    play_button_rect = pygame.Rect(SCREEN_WIDTH/2-150, 60, 300, 80)
    guide_button_surf = pygame.image.load("gfx\guide_btn.png").convert_alpha()
    guide_button_rect = pygame.Rect(SCREEN_WIDTH/2-150, 260, 300, 80)    
    quit_button_surf = pygame.image.load("gfx\quit_btn.png").convert_alpha()
    quit_button_rect = pygame.Rect(SCREEN_WIDTH/2-150, 460, 300, 80)
    


    while main_menu_status:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if play_button_rect.collidepoint(mouse_pos):
                    print("start")
                    main_menu_status = False
                elif quit_button_rect.collidepoint(mouse_pos):
                    print('quit')
                    pygame.quit()
                elif guide_button_rect.collidepoint(mouse_pos):
                    print('guide')
                    guide_status = True
                    guide()

        SCREEN.fill(BLACK)
        SCREEN.blit(title_text, (SCREEN_WIDTH/2, 50))
        SCREEN.blit(play_button_surf, play_button_rect)
        SCREEN.blit(quit_button_surf, quit_button_rect)
        SCREEN.blit(guide_button_surf, guide_button_rect)

        pygame.display.flip()
        clock.tick(60)

# go here first
main_menu()

# The levels
planet1_status = False
def planet1_env():
    global planet1_status
    print("Planet 1 environment")
    while planet1_status:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        

        all_sprites.update()
        SCREEN.fill(WHITE)

        player.heat_meter()
        if player.heat >= 500:
            player.heat = 0
            print("You overheated!")
            planet1_status = False
            
        all_sprites.draw(SCREEN)

        pygame.display.flip()
        clock.tick(60)
    # what kind of loot is here?
    # background image?

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

planet1_select_text = font.render("Planet Glarbin Shmargin", None, BLACK)
planet1_select_surf = pygame.image.load("gfx/planet_select/planet1.png").convert_alpha()
planet1_select_rect = pygame.Rect(100,130, 100,100)
planet1_locked = False

planet2_select_text = font.render("Planet Wikky Blikky", None, BLACK)
planet2_select_surf = pygame.image.load("gfx/planet_select/planet2.png").convert_alpha()
planet2_select_rect = pygame.Rect(250,280, 100,100)
planet2_locked = True

planet3_select_text = font.render("Planet Ronuld Bukets", None, BLACK)
planet3_select_surf = pygame.image.load("gfx/planet_select/planet3.png").convert_alpha()
planet3_select_rect = pygame.Rect(400,430, 100,100)
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
    SCREEN.fill(WHITE)

    SCREEN.blit(planet1_select_text, (100, 100))
    SCREEN.blit(planet1_select_surf, planet1_select_rect)

    SCREEN.blit(planet2_select_text, (250, 250))
    SCREEN.blit(planet2_select_surf, planet2_select_rect)
    SCREEN.blit(locked_surf, (250,250))

    SCREEN.blit(planet3_select_text, (400, 400))
    SCREEN.blit(planet3_select_surf, planet3_select_rect)
    SCREEN.blit(locked_surf, (400,400))


    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()