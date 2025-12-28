import pygame as pg
from pygame import mixer
import random
import math
import pickle

# Innitializing pygame (always do)
pg.init()

# creating a screen
screen = pg.display.set_mode((800,600))

# Setting the caption for the windows
pg.display.set_caption("Bachhan-Bash")

# Setting game icon
icon = pg.image.load("amitab.png")
pg.display.set_icon(icon)

# baackground
Background = pg.image.load("bg.jpg")

# background music
mixer.music.load('background.wav')
mixer.music.play(-1)
# player
playerImg = pg.image.load("space-game.png")
playerX= 368
playerY= 480
Xrate=1
Player_X_compensate=1
Player_Y_compensate=0

# enemy
num_enemy=6
enemyImg=[]
enemyX=[]
enemyY=[]
Enemy_X_compensate= []
Enemy_Y_compensate= []
for i in range (num_enemy):
    enemyImg.append(pg.image.load("amitab.png"))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    Enemy_X_compensate.append(0.5)
    Enemy_Y_compensate.append(40)

    def enemy(x,y):
        screen.blit(enemyImg[i],(x,y))

# bullet
bulletImg = pg.image.load("fire.png")
bulletX= 0
bulletY= 480
Bullet_X_compensate= 0
Bullet_Y_compensate= 2
bullet_state='ready'

# game over text
ov_font = pg.font.Font('freesansbold.ttf',64)

def save_high_score(score):
    with open("highscore.dat", "wb") as file:
        pickle.dump(score, file)

def load_high_score():
    try:
        with open("highscore.dat", "rb") as file:
            return pickle.load(file)
    except (FileNotFoundError, EOFError):
        return 0 

# Score 
score=0

high_score = load_high_score()
font = pg.font.Font('freesansbold.ttf',22)
textX=0
textY=0

def show_score(x,y):
    score_val = font.render("score: "+str(score),True,(240,240,200))
    high_score_val = font.render("High-score: "+str(high_score),True,(240,240,200))
    screen.blit(high_score_val,(x,y))
    screen.blit(score_val,(x,20))

def game_over_text(s,hs):
    ov_txt = ov_font.render("GAME OVER",True,(240,240,200))
    screen.blit(ov_txt,(200,250))
    if s==hs:
        score_val = font.render("NEW HIGHSCORE: "+str(score),True,(240,240,200))
        screen.blit(score_val,(300,320))
    else:
        score_val = font.render("SCORE: "+str(score),True,(240,240,200))
        screen.blit(score_val,(330,320))

def player(x,y):
    screen.blit(playerImg,(x,y))

def bullet(x,y):
    global bullet_state 
    bullet_state = 'fire'
    screen.blit(bulletImg,(x+16,y+10))

def is_collision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((bulletX-enemyX)**2+(bulletY-enemyY)**2)
    if distance<50:
        return True 
    else:
        return False
    
#  for ome time play of game over sound  
single_count=0 
# Game loop
running = True
while running:     
    screen.fill((29,29,29))

    # Background Image
    screen.blit(Background,(0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        # 1. Handle Key Presses
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                Player_X_compensate = -Xrate
            if event.key == pg.K_RIGHT:
                Player_X_compensate = Xrate
            if event.key == pg.K_SPACE:
                if bullet_state == 'ready': 
                    bulletX = playerX
                    bullet(bulletX, bulletY)

        # 2. Handle Key Releases 
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT and Player_X_compensate < 0:
                # Only stop if we were moving left
                Player_X_compensate = 0
            if event.key == pg.K_RIGHT and Player_X_compensate > 0:
                # Only stop if we were moving right
                Player_X_compensate = 0
                
    #setting horizontal boundaries
    playerX+=Player_X_compensate 

    # for player
    if playerX<0:
        playerX=0
    elif playerX>736:
        playerX=736

    for i in range (num_enemy):
        enemyX[i]+=Enemy_X_compensate[i] 

        # game over
        if enemyY[i]>430:
            for j in range (num_enemy):
                enemyY[j]=2000
                if single_count<1:
                     mixer.Sound('mkb_aagg.mp3').play()
                     single_count+=1
            game_over_text(score,high_score)
            if score>high_score:
                high_score=score
                save_high_score(high_score)
            break
        else:
            show_score(textX,textY)
            pg.draw.line(screen, (200,200,200) ,(0, 520), (800, 520), 2)

        # for enemy
        if enemyX[i]<0:
            enemyX[i]=0
            Enemy_X_compensate[i]=0.4
            enemyY[i]+=Enemy_Y_compensate[i]
        elif enemyX[i]>736:
            enemyX[i]=736
            Enemy_X_compensate[i]=-0.4
            enemyY[i]+=Enemy_Y_compensate[i]
        enemyY[i]+=0.05

        # collision
        collision=is_collision(enemyX[i],enemyY[i],bulletX,bulletY)
        if collision:
            mixer.Sound('aagg.mp3').play()
            bulletY=480
            bullet_state='ready'
            score+=1
            enemyX[i]= random.randint(0,735)
            enemyY[i]= random.randint(50,150)
        enemy(enemyX[i],enemyY[i])

    # bullet
    if bulletY <0:
        bulletY=480
        bullet_state='ready'

    if bullet_state == 'fire':
        bullet(bulletX,bulletY)
        bulletY-=Bullet_Y_compensate

    player(playerX,playerY)
    pg.display.update()