import pygame
import random

def game_start():
    keyC = True
    GameStart_screen = pygame.image.load("./../resource/images/START.png")
    screen.blit(GameStart_screen,(0,0))

    pygame.display.update()
    while keyC:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_c:
                    keyC = False

#테스트

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
GameOver = pygame.image.load("./../resource/images/OVER.png") #게임 오버  

BOO = pygame.image.load("./../resource/images/BOO.png") # 기본 부
BOO_right = pygame.image.load("./../resource/images/BOO_brown_right.png")
#BOO_brown = pygame.image.load("./../resource/images/BOO_brown.png") #갈색 부

BOO_size = BOO.get_rect().size
BOO_width = BOO_size[0] 
BOO_height = BOO_size[1] 
BOO_x_pos = screen_width/2-BOO_width/2 #화면 가로 크기의 절반에 해당하도록, 중앙에 놓이도록
BOO_y_pos = screen_height-BOO_height #화면 맨 아래에 캐릭터를 설치 
BOO_speed = 0.25


# 학점(A+, B+, C+, D+, F) 설정
score = 0

A = pygame.image.load("./../resource/images/scores/A+.png")
A_size = A.get_rect().size # 이미지의 크기를 구해옴
A_width = A_size[0] # 캐릭터의 가로 크기
A_height = A_size[1] # 캐릭터의 세로 크기
A_x_pos = random.randint(0, screen_width - A_width)
A_y_pos = random.randint(-1000, 0)
A_speed = random.uniform(0.2, 0.5)
#A_speed = 0.25

B = pygame.image.load("./../resource/images/scores/B+.png")
B_size = B.get_rect().size # 이미지의 크기를 구해옴
B_width = B_size[0] # 캐릭터의 가로 크기
B_height = B_size[1] # 캐릭터의 세로 크기
B_x_pos = random.randint(0, screen_width - B_width)
B_y_pos = random.randint(-500, 0)
B_speed = 0.32

C = pygame.image.load("./../resource/images/scores/C+.png")
C_size = C.get_rect().size # 이미지의 크기를 구해옴
C_width = C_size[0] # 캐릭터의 가로 크기
C_height = C_size[1] # 캐릭터의 세로 크기
C_x_pos = random.randint(0, screen_width - C_width)
C_y_pos = random.randint(-250, 0)
C_speed = 0.37

D = pygame.image.load("./../resource/images/scores/D+.png")
D_size = D.get_rect().size # 이미지의 크기를 구해옴
D_width = D_size[0] # 캐릭터의 가로 크기
D_height = D_size[1] # 캐릭터의 세로 크기
D_x_pos = random.randint(0, screen_width - D_width)
D_y_pos = random.randint(-120, 0)
D_speed = 0.43

F = pygame.image.load("./../resource/images/scores/F.png")
F_size = F.get_rect().size # 이미지의 크기를 구해옴
F_width = F_size[0] # 캐릭터의 가로 크기
F_height = F_size[1] # 캐릭터의 세로 크기
F_x_pos = random.randint(0, screen_width - F_width)
F_y_pos = random.randint(-100, 0)
F_speed = random.uniform(0.6, 0.8)
#F_speed = 0.66

F1 = pygame.image.load("./../resource/images/scores/F.png")
F1_size = F1.get_rect().size # 이미지의 크기를 구해옴
F1_width = F1_size[0] # 캐릭터의 가로 크기
F1_height = F1_size[1] # 캐릭터의 세로 크기
F1_x_pos = random.randint(0, screen_width - F1_width)
F1_y_pos = random.randint(-10, 0)
F1_speed = random.uniform(0.48, 0.59)
#F1_speed = 0.5

F2 = pygame.image.load("./../resource/images/scores/F.png")
F2_size = F2.get_rect().size # 이미지의 크기를 구해옴
F2_width = F2_size[0] # 캐릭터의 가로 크기
F2_height = F2_size[1] # 캐릭터의 세로 크기
F2_x_pos = random.randint(0, screen_width - F2_width)
F2_y_pos = random.randint(-40, 0)
F2_speed = random.uniform(0.75, 0.89)
#F2_speed = 0.8

F3 = pygame.image.load("./../resource/images/scores/F.png")
F3_size = F3.get_rect().size # 이미지의 크기를 구해옴
F3_width = F3_size[0] # 캐릭터의 가로 크기
F3_height = F3_size[1] # 캐릭터의 세로 크기
F3_x_pos = random.randint(0, screen_width - F3_width)
F3_y_pos = random.randint(-50, 0)
F3_speed = random.uniform(0.48, 0.89)

F4 = pygame.image.load("./../resource/images/scores/F.png")
F4_size = F4.get_rect().size # 이미지의 크기를 구해옴
F4_width = F4_size[0] # 캐릭터의 가로 크기
F4_height = F4_size[1] # 캐릭터의 세로 크기
F4_x_pos = random.randint(0, screen_width - F4_width)
F4_y_pos = random.randint(-50, 0)
F4_speed = random.uniform(0.48, 0.89)

# 이동 좌표 설정
to_x, to_y = 0, 0
status = 0

# 폰트 정의
game_font = pygame.font.Font(None, 40)

# 총 시간
total_time = 60

game_start()

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
        A_speed = random.uniform(0.2, 0.5)

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
        F_y_pos = random.randint(-100, 0)
        F_x_pos = random.randint(0, screen_width - F_width)
        F_speed = random.uniform(0.6, 0.8)

    F1_y_pos += F1_speed * dt
    if F1_y_pos > screen_height:
        F1_y_pos = random.randint(-10, 0)
        F1_x_pos = random.randint(0, screen_width - F1_width)
        F1_speed = random.uniform(0.48, 0.59)

    F2_y_pos += F2_speed * dt
    if F2_y_pos > screen_height:
        F2_y_pos = random.randint(-40, 0)
        F2_x_pos = random.randint(0, screen_width - F2_width)
        F2_speed = random.uniform(0.75, 0.89)

    F3_y_pos += F3_speed * dt
    if F3_y_pos > screen_height:
        F3_y_pos = random.randint(-50, 0)
        F3_x_pos = random.randint(0, screen_width - F3_width)
        F3_speed = random.uniform(0.48, 0.89)

    F4_y_pos += F4_speed * dt
    if F4_y_pos > screen_height:
        F4_y_pos = random.randint(-50, 0)
        F4_x_pos = random.randint(0, screen_width - F4_width)
        F4_speed = random.uniform(0.48, 0.89)


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

    F1_rect = F1.get_rect()
    F1_rect.left = F1_x_pos
    F1_rect.top = F1_y_pos

    F2_rect = F2.get_rect()
    F2_rect.left = F2_x_pos
    F2_rect.top = F2_y_pos

    F3_rect = F3.get_rect()
    F3_rect.left = F3_x_pos
    F3_rect.top = F3_y_pos

    F4_rect = F4.get_rect()
    F4_rect.left = F4_x_pos
    F4_rect.top = F4_y_pos

    if BOO_rect.colliderect(A_rect):
        score += 10
        A_y_pos = random.randint(-1000, 0)
        A_x_pos = random.randint(0, screen_width - A_width)
        A_speed = random.uniform(0.2, 0.5)
    elif BOO_rect.colliderect(B_rect):
        score += 7
        B_y_pos = random.randint(-500, 0)
        B_x_pos = random.randint(0, screen_width - B_width)
    elif BOO_rect.colliderect(C_rect):
        score += 5
        C_y_pos = random.randint(-250, 0)
        C_x_pos = random.randint(0, screen_width - C_width)
    elif BOO_rect.colliderect(D_rect):
        score += 3
        D_y_pos = random.randint(-125, 0)
        D_x_pos = random.randint(0, screen_width - D_width)
    elif BOO_rect.colliderect(F_rect):
        score -= 5
        F_y_pos = random.randint(-100, 0)
        F_x_pos = random.randint(0, screen_width - F_width)
        F_speed = random.uniform(0.6, 0.8)
    elif BOO_rect.colliderect(F1_rect):
        score -= 5
        F1_y_pos = random.randint(-10, 0)
        F1_x_pos = random.randint(0, screen_width - F1_width)
        F1_speed = random.uniform(0.48, 0.59)
    elif BOO_rect.colliderect(F2_rect):
        score -= 5
        F2_y_pos = random.randint(-40, 0)
        F2_x_pos = random.randint(0, screen_width - F2_width)
        F2_speed = random.uniform(0.75, 0.89)
    elif BOO_rect.colliderect(F3_rect):
        score -= 5
        F3_y_pos = random.randint(-50, 0)
        F3_x_pos = random.randint(0, screen_width - F3_width)
        F3_speed = random.uniform(0.48, 0.89)
    elif BOO_rect.colliderect(F4_rect):
        score -= 5
        F4_y_pos = random.randint(-50, 0)
        F4_x_pos = random.randint(0, screen_width - F4_width)
        F4_speed = random.uniform(0.48, 0.89)

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
        A_x_pos, B_x_pos, C_x_pos, D_x_pos, F_x_pos, F1_x_pos, F2_x_pos, F3_x_pos, F4_x_pos= 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000
        screen.blit(GameOver,(0,0)) #남은 시간이 0 일 때 게임오버 화면 출력 
        screen.blit(get_point, (screen_width/2, screen_height/2-20))


    if to_x > 0:    #부를 화면에 출력
        screen.blit(BOO_right, (BOO_x_pos,BOO_y_pos))
        status = 1
    elif to_x < 0: 
        screen.blit(BOO, (BOO_x_pos,BOO_y_pos)) 
        status = 0
    if status == 1: screen.blit(BOO_right, (BOO_x_pos,BOO_y_pos))
    else: screen.blit(BOO, (BOO_x_pos,BOO_y_pos)) 
    screen.blit(A, (A_x_pos, A_y_pos))
    screen.blit(B, (B_x_pos, B_y_pos))
    screen.blit(C, (C_x_pos, C_y_pos))
    screen.blit(D, (D_x_pos, D_y_pos))
    screen.blit(F, (F_x_pos, F_y_pos))
    screen.blit(F1, (F1_x_pos, F1_y_pos))
    screen.blit(F2, (F2_x_pos, F2_y_pos))
    screen.blit(F3, (F3_x_pos, F3_y_pos))
    screen.blit(F4, (F4_x_pos, F4_y_pos))

    pygame.display.update()

pygame.quit()

# 원격 업로드 실험