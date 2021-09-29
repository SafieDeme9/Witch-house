import pygame 
from time import sleep
from pygame import mixer

pygame.init()
pygame.mixer.init()

window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

icon = pygame.image.load('witch-hat.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Witch house')

mixer.music.load('suspense.wav')
mixer.music.play()
sleep(5)

mixer.music.load('scary.wav')
mixer.music.play()
sleep(1)

image = pygame.image.load('witch.jpg')

window.blit(image, (0,0))

pygame.display.update()

sleep(5)
