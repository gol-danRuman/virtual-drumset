
from pygame.locals import *
import pygame
pygame.mixer.init(44100, -16,2,2048)
BD = pygame.mixer.music.load('bassdrum1.wav')
pygame.mixer.music.play(-1)
