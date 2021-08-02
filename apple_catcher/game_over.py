import pygame
import os
import webbrowser

pygame.init()
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Apple Catcher")
background = pygame.image.load(os.path.join("pics", "farm.png"))
icon = pygame.image.load(os.path.join("pics", "farmer.png"))
pygame.display.set_icon(icon)

font = pygame.font.Font("freesansbold.ttf", 32)
text_x = 260
text_y = 550

def end_text(x, y):
    text = font.render("GAME OVER", True, (0, 0, 0))
    text2 = font.render("Press ESC to exit", True, (0, 0, 0))
    text3 = font.render("Press SPACE for final score", True, (255, 0, 0))
    screen.blit(text, (295,500))
    screen.blit(text2, (x,y))
    screen.blit(text3, (190,450))
dat = open("final_score.html", "r")
def main():
    run = True
    while run:
        screen.fill((0, 128, 0))
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

                if event.key == pygame.K_SPACE:
                    pygame.quit()
                    webbrowser.open("final_score.html")
        end_text(text_x, text_y)
        pygame.display.update()
main()