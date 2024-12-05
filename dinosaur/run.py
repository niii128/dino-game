# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
#畫布大小
pygame.init()
screen = pygame.display.set_mode((1280, 400))

#放圖片 img
img_dino=pygame.image.load("dino.png")
img_cactus=pygame.image.load("cactus.png")
img_dino=pygame.transform.scale(img_dino,(90,90))#原本是(100,100)
#設定角色
dino_rect=img_dino.get_rect()
dino_rect.x=50#座標
dino_rect.y=300
is_jumping=False
jump=16#跳高度 原本是12
g=1
nowjump=jump

cactus_rect=img_cactus.get_rect()
cactus_rect.x=1200#座標
cactus_rect.y=315
speed=5

#設定分數
score=0
font=pygame.font.Font(None,36)

clock = pygame.time.Clock()#時鐘
running = True

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    score+=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:#事件 吧
            running = False#停止運行
        if event.type == pygame.KEYDOWN:#事件 吧
            if event.key==pygame.K_SPACE:
                is_jumping=True

    if is_jumping:
        dino_rect.y-=nowjump
        nowjump-=g
        if dino_rect.y>300:
            dino_rect.y=300
            nowjump=jump
            is_jumping=False

    cactus_rect.x-=speed
    if cactus_rect.x<0:
        cactus_rect.x=1280
        


    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")#填滿顏色
    score_show=font.render(f"Score:{score}",True,(0,0,0))
    screen.blit(score_show,(10,10))

    # RENDER YOUR GAME HERE
    screen.blit(img_dino,dino_rect)
    screen.blit(img_cactus,cactus_rect)

    # flip() the display to put your work on screen
    pygame.display.flip()
    

    clock.tick(60)  # limits FPS to 60

pygame.quit()