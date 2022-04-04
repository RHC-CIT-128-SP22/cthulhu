#!/usr/bin/env python3
'''
    Rio Hondo College
    CIT 128: Python Programming II
    Student Directed Project
'''

import pygame
from pygame import mixer
import scenes
from scenes import Display_Scene

def main():
    #initialize variables
    curr_game = Display_Scene()

    mixer.music.play(-1)

 ########  MAIN GAME LOOP ########
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        curr_game.scene_manager()

 ####### END OF GAME LOOP ########


if __name__ == '__main__':
    main()
