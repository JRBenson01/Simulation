import pygame, sys
from pygame.locals import *
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
bright_red = (200, 0, 0)
red = (255, 0, 0)

game_length = 1000
game_height = 627

gameDisplay = pygame.display.set_mode((game_length, game_height))
pygame.display.set_caption("Sustainia")
clock = pygame.time.Clock()
mouse = pygame.mouse.get_pos()
gd = gameDisplay

box1_posx = game_length * 0.9
box1_posy = game_height * 0.04

game_map = pygame.image.load("map_use.png")

def societies(xpos, ypos, s_length, s_height, color):
    pygame.draw.rect(gameDisplay, color, (xpos, ypos, s_length, s_height))

def bg(x, y):
    gameDisplay.blit(game_map, (x, y))

def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def menu_display(text):
    header_font = pygame.font.Font("freesansbold.ttf", 22)
    TextSurf, TextRect = text_objects(text, header_font, white)
    TextRect.center = ((game_length * 0.9), (game_height * 0.02))
    gameDisplay.blit(TextSurf, TextRect)

def menu():
    message_display("List of societies")
def game_loop(): 
    gameStay = True      
    while gameStay == True:
        mouse = pygame.mouse.get_pos()
        mousex = float(mouse[0])
        mousey = float(mouse[1])
        gl = float(game_length)
        for event in pygame.event.get():
            print ("(", float(mousex / game_length), ",", float(mousey / game_length), ")")
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            bg(0, 0)
            menu_display("List of Societies")
            societies((box1_posx), (box1_posy), 50, 50, white)
            if mouse[0] > 900 and mouse[0] < 951 and mousey > (box1_posy) and mousey < (box1_posy+50):
                pygame.draw.rect(gameDisplay, red, (box1_posx, box1_posy, 50, 50))
            socText = pygame.font.Font("freesansbold.ttf", 20)
            textSurf1, textRect1 = text_objects("15", socText, black)
            textRect1.center = ((box1_posx + 25), (box1_posy + 25))
            gameDisplay.blit(textSurf1, textRect1)
            pygame.display.update()
game_loop()
