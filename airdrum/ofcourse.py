import pygame,time

pygame.init()
pygame.mixer.init()
sounda= pygame.mixer.Sound("bassdrum1.wav")

sounda.play()
time.sleep(0.08)
