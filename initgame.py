
import pygame

pygame.init()

class Init_Game():
    #create game window
    X, Y = 800, 600
    SCREEN = pygame.display.set_mode((X, Y))
    pygame.display.set_caption("The Call of Cthulhu - Survival Horror Game")
    ICON = pygame.image.load("assets/icon.png")
    pygame.display.set_icon(ICON)

    #load buttons and icons
    TITLE = pygame.image.load("assets/mainTitle.png")
    START_BUTTON = pygame.image.load("assets/startButton.png")
    DIAL_BOX = pygame.image.load("assets/rectangle.png")

    #load background images
    START_SCREEN = pygame.image.load("assets/startBG.png")
    PORTRAIT_SCENE = pygame.image.load("assets/portrait.png")
    HORROR_IN_CLAY = pygame.image.load("assets/horrorInClay.jpg")
    UNIVERSITY = pygame.image.load("assets/UNIVERSITY.jpg")

    #declare colors and font
    FONT = pygame.font.SysFont('Rockwell', 16)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    #set item transparency
    DIAL_BOX.set_alpha(190)
    START_BUTTON.set_alpha(150)

    #set sound fx
    START_SOUND = pygame.mixer.Sound("assets/wildBeastRoar.wav")