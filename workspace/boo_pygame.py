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

# 캐릭터(봄, 여름, 가을, 겨울) 설정

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
    
    # 캐릭터 위치 정의 (좌, 우로만 움직이며 대쉬가 있음)

    # 학점 위치 정의 (A+, B+, C+, D+, F마다 다르게 설정) 

    # 충돌 처리 (A+: 10점, B+: 7점, C+: 5점, D+: 3점, F: -5점)
    
    # 배경, 캐릭터 그리기 (봄, 여름, 가을, 겨울)
        
    screen.blit(timer, (10, 10))

    pygame.display.update()

pygame.quit()