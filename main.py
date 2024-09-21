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
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("gfx/img.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed = 5
        self.heat = 0
        self.heat_limit = 1500
        self.timer = 0

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
        self.timer += 1
        if self.timer >= 2000:
            self.heat += 1
            self.timer = 0
        print(self.heat)

# Create a player instance
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Main menu
main_menu_status = True
def main_menu():
    global main_menu_status
    print("mainmenu")
    title_text = font.render("Planet Heatwave", None, BLACK)
    play_button_surf = pygame.image.load("gfx\play_btn.png").convert_alpha()
    play_button_rect = pygame.Rect(SCREEN_WIDTH/2, 100, 300, 80)
    quit_button_surf = pygame.image.load("gfx\quit_btn.png").convert_alpha()
    quit_button_rect = pygame.Rect(SCREEN_WIDTH/2, 300, 300, 80)

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
        SCREEN.blit(title_text, (SCREEN_WIDTH/2, 50))
        SCREEN.blit(play_button_surf, play_button_rect)
        SCREEN.blit(quit_button_surf, quit_button_rect)

        pygame.display.flip()
        clock.tick(60)

# go here first
main_menu()

# Heat meter is broken
planet1_status = False
def planet1_env():
    print("Planet 1 environment")
    while planet1_status:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        player.heat_meter()

        all_sprites.update()
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
        player.heat_meter()

        all_sprites.update()
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
        player.heat_meter()

        all_sprites.update()
        all_sprites.draw(SCREEN)

        pygame.display.flip()
        clock.tick(60)
    # what kind of loot is here?
    # background image?

# menu planet objects
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

# Main game loop
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

    # Update all sprites
    all_sprites.update()

    # Draw everything
    SCREEN.fill(WHITE)
    all_sprites.draw(SCREEN)

    SCREEN.blit(planet1_select_text, (100, 100))
    SCREEN.blit(planet1_select_surf, planet1_select_rect)
    SCREEN.blit(planet2_select_text, (250, 250))
    SCREEN.blit(planet2_select_surf, planet2_select_rect)
    SCREEN.blit(planet3_select_text, (400, 400))
    SCREEN.blit(planet3_select_surf, planet3_select_rect)


    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()