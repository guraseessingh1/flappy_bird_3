import pygame
from pygame.locals import *

pygame.init()

WIDTH = 864
HEIGHT = 736
run = True
ground_scroll = 0
scroll_speed = 4
fps = 60
clock = pygame.time.Clock()
flying = False
game_over = False

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("flappy bird")

bg_image = pygame.image.load("img/bg.png")

ground = pygame.image.load("img/ground.png")


class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for i in range(1,4):
            img = pygame.image.load(f"img/bird{i}.png")
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.velocity = 0
        self.clicked = False

    def change_animation(self):
        if flying == True:
            self.velocity += 0.5
            if self.velocity > 8:
                self.velocity = 8
            if self.rect.bottom < 768:
                self.rect.y += int(self.velocity)

        if game_over == False:
            if self.clicked == False and pygame.mouse.get_pressed()[0] == 1:
                self.clicked = True
                self.velocity = -10
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

            self.counter += 1
            flap_down = 5
            if self.counter > flap_down:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0
            self.image = self.images[self.index]
            self.image = pygame.transform.rotate(self.images[self.index],self.velocity *-2)
        else :
            self.image = pygame.transform.rotate(self.image[self.index],-90)
                
        



while run:


    clock.tick(fps)

    screen.blit(bg_image,(0,0))
    screen.blit(ground,(ground_scroll,568))

    ground_scroll -= scroll_speed
    if abs(ground_scroll) > 35:
        ground_scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()