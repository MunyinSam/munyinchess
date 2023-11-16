
import pygame

pygame.init()
WIDTH = 1000
HEIGHT = 700
screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption('Two Player pygame Chess')
font = pygame.font.Font('freesansbold.ttf', 20)
big_font = pygame.font.Font('freesansbold.ttf', 50)
timer = pygame.time.Clock()
fps = 60

# game variables and images


#main gameloop
run = True
while run:
    timer.tick(fps)
    screen.fill('dark grey')
    
    for event in pygame.event.get(): # getting all input
        if event.type == pygame.QUIT: # prebuilt pygame
            run = False
        
    pygame.display.flip()
pygame.quit()