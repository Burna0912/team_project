import pygame
import random


pygame.init()

# 화면 크기 설정
screen_width = 1000 # 가로 크기
screen_height = 700 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("BOO GAME")

# FPS
clock = pygame.time.Clock()

# 배경(봄, 여름, 가을, 겨울) 설정

background_1 = pygame.image.load("./../resource/images/BACK1.png") #1학기 배경
background_2 = pygame.image.load("./../resource/images/BACK2.png") #2학기 배경
GameOver = pygame.image.load("./../resource/images/game_over.png") #게임 오버  
#파일경로 수정, 배경이미지 수정 요망

# 캐릭터(봄, 여름, 가을, 겨울) 설정
BOO = pygame.image.load("./../resource/images/BOO.png")

#파일경로 수정, 캐릭터 이미지 수정 및 추가 요망 
BOO_size = BOO.get_rect().size
BOO_width = BOO_size[0] 
BOO_height = BOO_size[1] 
BOO_x_position = screen_width/2-BOO_width/2 #화면 가로 크기의 절반에 해당하도록, 중앙에 놓이도록
BOO_y_position = screen_height-BOO_height #화면 맨 아래에 캐릭터를 설치 


# 학점(A+, B+, C+, D+, F) 설정

# 이동 좌표 설정
to_x, to_y = 0, 0

# 이동 속도 설정 (캐릭터, A+, B+, C+, D+, F, 대쉬)



# 폰트 정의
game_font = pygame.font.Font(None, 40)

# 총 시간
total_time = 60

# 시작 시간
start_ticks = pygame.time.get_ticks()

running = True 
while running:
    dt = clock.tick(60)

    # 경과 시간 계산
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # 키보드 입력 설정
        
        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: #캐릭터를 왼쪽으로
                to_x -= 5
            elif event.key == pygame.K_RIGHT:
                to_x += 5
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
                
    # 부가 화면 밖으로 넘어가지 않도록 조치          
    if BOO_x_position < 0:
        BOO_x_position = 0
    elif BOO_x_position > screen_width-BOO_width:
        BOO_x_position =screen_width-BOO_width 
        
    BOO_x_position += to_x
    # 캐릭터 위치 정의 (좌, 우로만 움직이며 대쉬가 있음)

    # 학점 위치 정의 (A+, B+, C+, D+, F마다 다르게 설정) 

    # 충돌 처리 (A+: 10점, B+: 7점, C+: 5점, D+: 3점, F: -5점)
    
    

    # 배경, 캐릭터 그리기 (봄, 여름, 가을, 겨울)
    # 60초를 4분할하여 각 15초마다 봄, 여름, 가을, 겨울 순으로 배경이 바뀜
    
    if (total_time-elapsed_time) >30:
        screen.blit(background_1,(0,0))
    elif (total_time-elapsed_time) >0:
        screen.blit(background_2,(0,0))
    else:
        screen.blit(GameOver,(0,0)) 
       
    if(total_time-elapsed_time > 0): #게임이 종료되면 타이머가 안보이도록 설정
        screen.blit(timer, (10, 10))
    else:
        screen.blit(timer, (-100, -100))
        BOO_y_position = 100000

    #부 위치 설정    
    screen.blit(BOO, (BOO_x_position,BOO_y_position))
        
    

    pygame.display.update()

pygame.quit()

# 원격 업로드 실험