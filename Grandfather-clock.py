#!/usr/bin/env python
import pygame
import time
import os

'''Script for Grandfather clock tutorial linuxleech Youtube'''

def main():
    pygame.mixer.init()
    dir_path = os.path.dirname(os.path.abspath(__file__)) 
    on_the_hour = pygame.mixer.Sound(os.path.join(dir_path, 'Audio-sfx/tolling1.wav')) 
    single_ding = pygame.mixer.Sound(os.path.join(dir_path, 'Audio-sfx/hour-chime-single1.wav'))
    
    now = int(time.strftime("%I"))
    
    on_the_hour.play()
    time.sleep(6)


    i = 0
    while i <  now:
        single_ding.play()
        time.sleep(2.5)
        i+= 1
    pygame.quit()

if __name__ == "__main__":
    main()
