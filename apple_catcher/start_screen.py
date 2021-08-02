import pygame
import os

pygame.init()
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Apple Catcher")
background = pygame.image.load(os.path.join("pics", "farm.png"))
icon = pygame.image.load(os.path.join("pics", "farmer.png"))
pygame.display.set_icon(icon)

font = pygame.font.Font("freesansbold.ttf", 32)
text_x = 200
text_y = 550

def start_text(x, y):
    text = font.render("PRESS SPACE TO START", True, (0, 0, 0))
    screen.blit(text, (x,y))

def main():
    run = True
    while run:
        screen.fill((0, 128, 0))
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = False
        start_text(text_x, text_y)
        pygame.display.update()
main()

    