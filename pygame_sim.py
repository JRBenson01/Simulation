import pygame, sys
from pygame.locals import *
pygame.init()

white = (255, 255, 255)

game_length = 1000
game_height = 627

gameDisplay = pygame.display.set_mode((game_length, game_height))
pygame.display.set_caption("Sustainia")
clock = pygame.time.Clock()

game_map = pygame.image.load("map_use.png")

def bg(x, y):
    gameDisplay.blit(game_map, (x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def menu_display(text):
    header_font = pygame.font.Font("freesansbold.ttf", 22)
    TextSurf, TextRect = text_objects(text, header_font)
    TextRect.center = ((game_length * 0.9), (game_height * 0.02))
    gameDisplay.blit(TextSurf, TextRect)

def menu():
    message_display("List of societies")
    
       

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            

        bg(0, 0)
        menu
        menu_display("List of Societies")
        pygame.display.update()
