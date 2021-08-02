import pygame
import os
import random
from pygame import mixer
from start_screen import main as m

pygame.init()
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Apple Catcher")
background = pygame.image.load(os.path.join("pics", "farm.png"))
icon = pygame.image.load(os.path.join("pics", "farmer.png"))
pygame.display.set_icon(icon)

mixer.music.load(os.path.join("sounds", "plain_folks.mp3"))
mixer.music.play(-1)
catch_sound = pygame.mixer.Sound(os.path.join("sounds", "impact.wav"))

basket_img = pygame.image.load(os.path.join("pics", "basket.png")).convert_alpha()
basket_x = 330
basket_y = 480
basket_x_change = 0
basket_y_change = 0
rect_basket = pygame.Rect(basket_x, basket_y, 128, 128)

apple_img = pygame.image.load(os.path.join("pics", "apple.png")).convert_alpha()
apple_x = random.randint(1, 768)
apple_x1 = random.randint(1, 768)
apple_x2= random.randint(1, 768)
apple_y = random.randint(0, 250)
apple_y1 = random.randint(0, 250)
apple_y2 = random.randint(0, 250)
apple_y_change = random.uniform(1, 2.1)
apple_y_change1 = random.uniform(1, 2.1)
apple_y_change2 = random.uniform(1, 2.1)
rect_apple = pygame.Rect(apple_x, apple_y, 32, 32)
rect_apple1 = pygame.Rect(apple_x1, apple_y1, 32, 32)
rect_apple2 = pygame.Rect(apple_x2, apple_y2, 32, 32)

score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
text_x = 10
text_y = 10

score_list = []

def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (0, 0, 0))
    screen.blit(score, (x, y))

def basket():
    screen.blit(basket_img, (rect_basket.x, rect_basket.y))

def apple():
    screen.blit(apple_img, (rect_apple.x, rect_apple.y))
def apple1():
    screen.blit(apple_img, (rect_apple1.x, rect_apple1.y))
def apple2():
    screen.blit(apple_img, (rect_apple2.x, rect_apple2.y))

refresh = pygame.time.Clock()
timer = 45
font2 = pygame.font.Font("freesansbold.ttf", 64)
text = font.render(str(timer), True, (0, 0, 0))
timer_event = pygame.USEREVENT + 1
pygame.time.set_timer(timer_event, 1000)

run = True
while run:
    refresh.tick(120)
    screen.fill((0, 128, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == timer_event:
            timer -= 1
            text = font.render(str(timer), True, (0, 0, 0))
            if timer == 0:
                run = False
                # import game_over
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                basket_x_change = -3
            if event.key == pygame.K_RIGHT:
                basket_x_change = 3
            if event.key == pygame.K_UP:
                basket_y_change = -3
            if event.key == pygame.K_DOWN:
                basket_y_change = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                basket_x_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                basket_y_change = 0
    
    rect_basket.x += basket_x_change
    
    if rect_basket.x <= 0:
        rect_basket.x = 0.0
    elif rect_basket.x >= 672:
        rect_basket.x = 672
    
    rect_basket.y += basket_y_change

    if rect_basket.y <= 350:
        rect_basket.y = 350
    elif rect_basket.y >= 472:
        rect_basket.y = 472

    rect_apple.y += apple_y_change

    if rect_apple.y >= 600:
        rect_apple.x = random.randint(0, 768)
        rect_apple.y = random.randint(0, 230)
        apple_y_change = random.uniform(1, 2)

    if rect_apple.top == rect_basket.top and rect_apple.colliderect(rect_basket):
        pygame.mixer.Sound.play(catch_sound)
        rect_apple.x = random.randint(0, 768)
        rect_apple.y = random.randint(0, 230)
        apple_y_change = random.uniform(1, 2)
        score_value += 1
        score_list.append(score_value)

    rect_apple1.y += apple_y_change1

    if rect_apple1.y >= 600:
        rect_apple1.x = random.randint(0, 768)
        rect_apple1.y = random.randint(0, 230)
        apple_y_change1 = random.uniform(1, 2)

    if rect_apple1.top == rect_basket.top and rect_apple1.colliderect(rect_basket):
        pygame.mixer.Sound.play(catch_sound)
        rect_apple1.x = random.randint(0, 768)
        rect_apple1.y = random.randint(0, 230)
        apple_y_change1 = random.uniform(1, 2)
        score_value += 1
        score_list.append(score_value)

    rect_apple2.y += apple_y_change2

    if rect_apple2.y >= 600:
        rect_apple2.x = random.randint(0, 768)
        rect_apple2.y = random.randint(0, 230)
        apple_y_change2 = random.uniform(1, 2)

    if rect_apple2.top == rect_basket.top and rect_apple2.colliderect(rect_basket):
        pygame.mixer.Sound.play(catch_sound)
        rect_apple2.x = random.randint(0, 768)
        rect_apple2.y = random.randint(0, 230)
        apple_y_change2 = random.uniform(1, 2)
        score_value += 1
        score_list.append(score_value)

    apple()
    apple1()
    apple2()
    basket()
    show_score(text_x, text_y)
    text_rect = text.get_rect(topright = screen.get_rect().topright)
    screen.blit(text, text_rect)
    pygame.display.update()
print(score_list[-1])
dat = open("final_score.html", "w")
dat.write("YOUR FINAL SCORE IS: ")
dat.write(str(score_list[-1]))
import game_over