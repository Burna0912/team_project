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

background_1 = pygame.image.load("./../resource/images/BACK1.png") #1학기 배경
background_2 = pygame.image.load("./../resource/images/BACK2.png") #2학기 배경
GameOver = pygame.image.load("./../resource/images/game_over.png") #게임 오버  

BOO = pygame.image.load("./../resource/images/BOO.png") # 기본 부
BOO_pink = pygame.image.load("./../resource/images/BOO_pink.png") #핑크색 부
BOO_brown = pygame.image.load("./../resource/images/BOO_brown.png") #갈색 부
BOO_sky = pygame.image.load("./../resource/images/BOO_sky.png") #하늘색 부

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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
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
    

    if (total_time-elapsed_time) >30: #시간이 30초 이상 남았을 때 1학기 배경화면 출력 
        screen.blit(background_1,(0,0))
    elif (total_time-elapsed_time) >0: #시간이 30초 이하 남았을 때 2학기 배경화면 출력 
        screen.blit(background_2,(0,0))
    else:
        BOO_x_position = 10000 #남은 시간이 0 일 때 부를 화면에 뜨지 않도록 처리 
        screen.blit(GameOver,(0,0)) #남은 시간이 0 일 때 게임오버 화면 출력 
        
    if(total_time-elapsed_time > 0): #시간이 남았을 경우 10,10 좌표에 타이며 출력
        screen.blit(timer, (10, 10))
    else:                           #시간이 끝났을 경우 좌포 -100,-100에 타이머룰 출력해 화면에 보이지 않게 함
        screen.blit(timer, (-100, -100))
   
    screen.blit(BOO, (BOO_x_position,BOO_y_position)) #부를 화면에 출력 
        
    

    pygame.display.update()

pygame.quit()

# 원격 업로드 실험