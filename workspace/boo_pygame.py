import pygame
import random

#branch : test

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

BOO_size = BOO.get_rect().size
BOO_width = BOO_size[0] 
BOO_height = BOO_size[1] 
BOO_x_pos = screen_width/2-BOO_width/2 #화면 가로 크기의 절반에 해당하도록, 중앙에 놓이도록
BOO_y_pos = screen_height-BOO_height #화면 맨 아래에 캐릭터를 설치 
BOO_speed = 0.25


# 학점(A+, B+, C+, D+, F) 설정
score = 0

A = pygame.image.load("./../resource/images/scores/autumn_A.png")
A_size = A.get_rect().size # 이미지의 크기를 구해옴
A_width = A_size[0] # 캐릭터의 가로 크기
A_height = A_size[1] # 캐릭터의 세로 크기
A_x_pos = random.randint(0, screen_width - A_width)
A_y_pos = random.randint(-1000, 0)
A_speed = 0.25

B = pygame.image.load("./../resource/images/scores/spring_A.png")
B_size = B.get_rect().size # 이미지의 크기를 구해옴
B_width = B_size[0] # 캐릭터의 가로 크기
B_height = B_size[1] # 캐릭터의 세로 크기
B_x_pos = random.randint(0, screen_width - B_width)
B_y_pos = random.randint(-500, 0)
B_speed = 0.32

C = pygame.image.load("./../resource/images/scores/spring_B.png")
C_size = C.get_rect().size # 이미지의 크기를 구해옴
C_width = C_size[0] # 캐릭터의 가로 크기
C_height = C_size[1] # 캐릭터의 세로 크기
C_x_pos = random.randint(0, screen_width - C_width)
C_y_pos = random.randint(-250, 0)
C_speed = 0.37

D = pygame.image.load("./../resource/images/scores/summer_A.png")
D_size = D.get_rect().size # 이미지의 크기를 구해옴
D_width = D_size[0] # 캐릭터의 가로 크기
D_height = D_size[1] # 캐릭터의 세로 크기
D_x_pos = random.randint(0, screen_width - D_width)
D_y_pos = random.randint(-120, 0)
D_speed = 0.43

F = pygame.image.load("./../resource/images/scores/winter_A.png")
F_size = F.get_rect().size # 이미지의 크기를 구해옴
F_width = F_size[0] # 캐릭터의 가로 크기
F_height = F_size[1] # 캐릭터의 세로 크기
F_x_pos = random.randint(0, screen_width - F_width)
F_y_pos = 0
F_speed = 0.66



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
    get_point = game_font.render(str(int(score)), True, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # 키보드 입력 설정 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= BOO_speed
            elif event.key == pygame.K_RIGHT:
                to_x += BOO_speed
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
                
    # 부가 화면 밖으로 넘어가지 않도록 조치          
    if BOO_x_pos < 0:
        BOO_x_pos = 0
    elif BOO_x_pos > screen_width-BOO_width:
        BOO_x_pos =screen_width-BOO_width 
    
    BOO_x_pos += to_x * dt

    # 캐릭터 위치 정의 (좌, 우로만 움직이며 대쉬가 있음)
    A_y_pos += A_speed * dt
    if A_y_pos > screen_height:
        A_y_pos = random.randint(-1000, 0)
        A_x_pos = random.randint(0, screen_width - A_width)

    B_y_pos += B_speed * dt
    if B_y_pos > screen_height:
        B_y_pos = random.randint(-500, 0)
        B_x_pos = random.randint(0, screen_width - B_width)
    
    C_y_pos += C_speed * dt
    if C_y_pos > screen_height:
        C_y_pos = random.randint(-250, 0)
        C_x_pos = random.randint(0, screen_width - C_width)
    
    D_y_pos += D_speed * dt
    if D_y_pos > screen_height:
        D_y_pos = random.randint(-125, 0)
        D_x_pos = random.randint(0, screen_width - D_width)

    F_y_pos += F_speed * dt
    if F_y_pos > screen_height:
        F_y_pos = 0
        F_x_pos = random.randint(0, screen_width - F_width)


    # 학점 위치 정의 (A+, B+, C+, D+, F마다 다르게 설정) 

    # 충돌 처리 (A+: 10점, B+: 7점, C+: 5점, D+: 3점, F: -5점)
    BOO_rect = BOO.get_rect()
    BOO_rect.left = BOO_x_pos
    BOO_rect.top = BOO_y_pos

    A_rect = A.get_rect()
    A_rect.left = A_x_pos
    A_rect.top = A_y_pos

    B_rect = B.get_rect()
    B_rect.left = B_x_pos
    B_rect.top = B_y_pos

    C_rect = C.get_rect()
    C_rect.left = C_x_pos
    C_rect.top = C_y_pos

    D_rect = D.get_rect()
    D_rect.left = D_x_pos
    D_rect.top = D_y_pos

    F_rect = F.get_rect()
    F_rect.left = F_x_pos
    F_rect.top = F_y_pos

    if BOO_rect.colliderect(A_rect):
        score += 10
        A_y_pos = random.randint(-1000, 0)
    elif BOO_rect.colliderect(B_rect):
        score += 7
        B_y_pos = random.randint(-500, 0)
    elif BOO_rect.colliderect(C_rect):
        score += 5
        C_y_pos = random.randint(-250, 0)
    elif BOO_rect.colliderect(D_rect):
        score += 3
        D_y_pos = random.randint(-125, 0)
    elif BOO_rect.colliderect(F_rect):
        score -= 5
        F_y_pos = 0

    
    

    if (total_time-elapsed_time) >30: #시간이 30초 이상 남았을 때 1학기 배경화면 출력 
        screen.blit(background_1,(0,0))
        screen.blit(timer, (10, 10))
        screen.blit(get_point, (screen_width-50, 10))
    elif (total_time-elapsed_time) >0: #시간이 30초 이하 남았을 때 2학기 배경화면 출력 
        screen.blit(background_2,(0,0))
        screen.blit(timer, (10, 10))
        screen.blit(get_point, (screen_width-50, 10))
    else:
        BOO_x_pos = 10000 #남은 시간이 0 일 때 부를 화면에 뜨지 않도록 처리 
        A_x_pos, B_x_pos, C_x_pos, D_x_pos, F_x_pos = 10000, 10000, 10000, 10000, 10000
        screen.blit(GameOver,(0,0)) #남은 시간이 0 일 때 게임오버 화면 출력 
        screen.blit(get_point, (screen_width/2, screen_height/2))

    screen.blit(BOO_brown, (BOO_x_pos,BOO_y_pos)) #부를 화면에 출력 
    screen.blit(A, (A_x_pos, A_y_pos))
    screen.blit(B, (B_x_pos, B_y_pos))
    screen.blit(C, (C_x_pos, C_y_pos))
    screen.blit(D, (D_x_pos, D_y_pos))
    screen.blit(F, (F_x_pos, F_y_pos))

    pygame.display.update()

pygame.quit()

# 원격 업로드 실험