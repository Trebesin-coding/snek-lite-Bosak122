import pygame
import random

pygame.init()


SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sbírání mince")
clock = pygame.time.Clock()


WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


player_size = 20
player_x, player_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
player_speed = 5


coin_size = 10
coin_x, coin_y = random.randint(0, SCREEN_WIDTH - coin_size), random.randint(0, SCREEN_HEIGHT - coin_size)


score = 0
font = pygame.font.Font(None, 36)

running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_y -= player_speed
    if keys[pygame.K_s]:
        player_y += player_speed
    if keys[pygame.K_a]:
        player_x -= player_speed
    if keys[pygame.K_d]:
        player_x += player_speed
    
    
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    coin_rect = pygame.Rect(coin_x, coin_y, coin_size, coin_size)
    
    if player_rect.colliderect(coin_rect):
        score += 1
        coin_x, coin_y = random.randint(0, SCREEN_WIDTH - coin_size), random.randint(0, SCREEN_HEIGHT - coin_size)
    
   
    pygame.draw.rect(screen, GREEN, player_rect)
    pygame.draw.rect(screen, RED, coin_rect)
    

    score_text = font.render(f"Skóre: {score}", True, (0, 0, 0))
    screen.blit(score_text, (SCREEN_WIDTH - 100, 10))
    
    pygame.display.update()
    clock.tick(30)

pygame.quit()
