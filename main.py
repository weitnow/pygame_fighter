import pygame
from fighter import Fighter

pygame.init()

# create game window
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Gemetzel')

#set framerate
clock = pygame.time.Clock()
FPS = 60

# load background image
bg_image = pygame.image.load('assets/images/background/background.jpg').convert_alpha()


# function for drawing background
def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))

#create two instances of fighters
fighter_1 = Fighter(200, 310)
fighter_2 = Fighter(700, 310)


# game loop
run = True
while run:

    clock.tick(FPS)

    #draw background
    draw_bg()

    #move fighters
    fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT)

    #draw the fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #update display
    pygame.display.update()

# exit pygame
pygame.quit()
