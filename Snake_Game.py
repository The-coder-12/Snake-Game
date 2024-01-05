#Import modules
import pygame
import time
import random

#Variables
dis_width = 1000
dis_height = 500
bg = pygame.image.load("la_table.jpg")
bg1 = pygame.transform.scale(bg, (dis_width, dis_height))
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Snake Game")

#Initialize the Pygame
pygame.init()

#Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

#More variables
font = pygame.font.SysFont("microsoftsansserif", 36)
snake_size = 30

#Functions
def WR(WRvalue, colour):
    record=font.render("World Record: " + str(WRvalue), True, colour)
    dis.blit(record, [0, 0])

def border():
    pygame.draw.rect(dis, black, [0, 0, dis_width, dis_height], 10)

def snake1(snake_size, snake):
    for x in snake:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_size, snake_size])

def death_message(deathmsg, color):
    content=font.render(deathmsg, True, color)
    dis.blit(content, [0, 0])

def points(score):
    value=font.render("Score: " + str(score), True, blue)
    dis.blit(value, [6, 450])

#Even more variables
clock = pygame.time.Clock()
NOMNOM = pygame.mixer.Sound("carrotnom-92106.mp3")
BUMPBUMP = pygame.mixer.Sound("punch-140236.mp3")

#Last function
def game(): #Main game loop
    the_record = 9
    game_running = False
    game_close = False
    snake_len = 1

    snake = []

    x1 = 300
    y1 = 300
    x1change = 0
    y1change = 0

    foodx = round(random.randrange(0, dis_width - snake_size) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_size) / 10.0) * 10.0

    while not game_running:
        cloud = [the_record]

        while game_close == True:
            death_message("You died! R = Restart or Q = Quit.", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit
                    quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit
                        quit()
                    if event.key == pygame.K_r:
                        game()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1change = -10
                    y1change = 0
                elif event.key == pygame.K_RIGHT:
                    x1change = 10
                    y1change = 0
                elif event.key == pygame.K_UP:
                    x1change = 0
                    y1change = -10
                elif event.key == pygame.K_DOWN:
                    x1change = 0
                    y1change = 10
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            BUMPBUMP.play()
            BUMPBUMP.set_volume(0.85742)
            game_close = True

        x1 += x1change
        y1 += y1change

        dis.fill(white)
        dis.blit(bg1, [0, 0])

        pygame.draw.rect(dis, red, [foodx, foody, snake_size, snake_size])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake.append(snake_head)

        if len(snake) > snake_len:
            del snake[0]

        for x in snake[:-1]:
            if x == snake_head:
                game_close = True

        #Sub-fonctions
        border()
        snake1(snake_size, snake)
        points(snake_len - 1)
        WR(cloud[-1], blue)
        score = snake_len - 1
        if score > the_record:
            the_record = score
            cloud.append(the_record)


        #Update the display
        pygame.display.update()
        clock.tick(10)

        #If the snake eats the food
        if x1 == foodx and y1 == foody:
            #Food eating sound
            NOMNOM.play()
            NOMNOM.set_volume(0.85742)
            #Random food ganeration
            foodx = round(random.randrange(0, dis_width - snake_size) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_size) / 10.0) * 10.0
            #Become longer
            snake_len += 1


    #What to do after "dying"
    time.sleep(5)
    pygame.quit()
    quit()

#DO IT BABY!
game()