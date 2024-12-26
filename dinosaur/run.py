# Example file showing a basic pygame "game loop"
import pygame
import random
# pygame setup
#畫布大小
pygame.init()
screen = pygame.display.set_mode((1280, 400))

#放圖片 img
img_dino=pygame.image.load("dino.png")
img_cactus=pygame.image.load("cactus.png")
img_dinorun=[pygame.image.load("DinoRun1.png"),pygame.image.load("DinoRun2.png")]
img_dinoduck=[pygame.image.load("DinoDuck1.png"),pygame.image.load("DinoDuck2.png")]
img_birdrun=[pygame.image.load("Bird1.png"),pygame.image.load("Bird2.png")]
img_dino=pygame.transform.scale(img_dino,(90,90))#原本是(100,100)
img_bird=pygame.image.load("Bird1.png")
img_track=pygame.image.load("track.png")
#設定角色
dino_rect=img_dino.get_rect()
dino_rect.x=50#座標
dino_rect.y=300
is_jumping=False
is_ducking=False
jump=20#跳高度 原本是12
g=1
nowjump=jump

cactus_rect=img_cactus.get_rect()
cactus_rect.x=1200#座標
cactus_rect.y=315
initspeed=5
speed=initspeed

bird_rect=img_bird.get_rect()
bird_rect.x=2400
bird_rect.y=250
initspeed=5
speed=initspeed

#設定分數
score=0
highscore=0#最高紀錄
font=pygame.font.Font(None,36)

#等級
level=0
speedlist=[5,6,7,8,9]

clock = pygame.time.Clock()#時鐘
running = True
gameover=False
lasttime=0
frame=0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    score+=1
    #if score>2000:
        #speed+=1
    for event in pygame.event.get():
            if event.type == pygame.QUIT:#事件 吧
                running = False#停止運行
            if event.type == pygame.KEYDOWN: #and not is_jumping:#事件 吧
                if event.key==pygame.K_SPACE:
                    is_jumping=True
                if event.key==pygame.K_r:
                    score=0
                    cactus_rect.x=1500#老師設2000
                    bird_rect.x=2000
                    gameover=False
                if event.key==pygame.K_UP:
                    is_jumping=True
                if event.key==pygame.K_DOWN:
                    dino_rect.y=330
                    is_ducking=True

            if event.type==pygame.KEYUP:
                if is_ducking:
                    dino_rect.y=300
                    is_ducking=False

            if event.type == pygame.MOUSEBUTTONDOWN:
                is_jumping=True
                if gameover:
                    score=0
                    cactus_rect.x=1500#老師設3000
                    bird_rect.x=2400#老師設2000
                    gameover=False

    if not gameover:
        if score>2000:
            speed+=1

        if is_jumping:
            dino_rect.y-=nowjump
            nowjump-=g
            if dino_rect.y>300:
                dino_rect.y=300
                nowjump=jump
                is_jumping=False

        #仙人掌移動
        cactus_rect.x-=speed
        if cactus_rect.x<0:
            cactus_rect.x= random.randint(1280, 3000)
            

        #天上恐龍移動
        bird_rect.x-=speed
        if bird_rect.x<0:
            bird_rect.x= random.randint(1280, 2000)
            
        #撞仙人掌
        if dino_rect.colliderect(cactus_rect) or dino_rect.colliderect(bird_rect):
            if score>highscore:
                highscore=score
            gameover=True

        

        if score>3000:
            speed = speedlist[3]
            level = 3
        elif score >2000:
            speed = speedlist[2]
            level =2
        elif score >1000:
            speed = speedlist[1]
            level = 1




        

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("white")#填滿顏色
        screen.blit(img_track,(0,370))

        score_show=font.render(f"Score:{score}",True,(0,0,0))
        screen.blit(score_show,(10,10))

        highscore_show=font.render(f"High Score:{highscore}",True,(0,0,0))
        screen.blit(highscore_show,(10,30))

        level_show=font.render(f"Level:{level}  Speed: {speed}",True,(0,0,0))
        screen.blit(level_show,(10,50))

        if gameover:
            gameover_show=font.render(f"Game Over",True,(0,0,0))
            screen.blit(gameover_show,(550,150))
        
        #更新跑步動畫
        nowtime=pygame.time.get_ticks()
        if nowtime - lasttime>300:
            #0.3秒
            frame=(frame+1)%2
            lasttime=nowtime

        if is_ducking:
            screen.blit(img_dinoduck[frame],dino_rect)
        else:
            screen.blit(img_dinorun[frame],dino_rect)
        
        
        #screen.blit(img_dinorun[frame],dino_rect)
        # RENDER YOUR GAME HERE
        # screen.blit(img_dino,dino_rect)
        screen.blit(img_cactus,cactus_rect)
        screen.blit(img_birdrun[frame],bird_rect)

        # flip() the display to put your work on screen
        pygame.display.flip()
        

        clock.tick(60)  # limits FPS to 60

pygame.quit()
