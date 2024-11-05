import pygame
import sys

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Пинг-Понг")

white = (255, 255, 255)
black = (0, 0, 0)

paddle_width, paddle_height = 10, 100
paddle_speed = 5

ball_size = 20
ball_speed_x, ball_speed_y = 5, 5

left_paddle = pygame.Rect(10, height // 2 - paddle_height // 2, paddle_width, paddle_height)
right_paddle = pygame.Rect(width - 10 - paddle_width, height // 2 - paddle_height // 2, paddle_width, paddle_height)

ball = pygame.Rect(width // 2 - ball_size // 2, height // 2 - ball_size // 2, ball_size, ball_size)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Исправлены отступы для обработки ввода
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= paddle_speed
    if keys[pygame.K_s] and left_paddle.bottom < height:
        left_paddle.y += paddle_speed
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle.bottom < height:
        right_paddle.y += paddle_speed

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= height:
        ball_speed_y *= -1

    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_speed_x *= -1

    if ball.left <= 0 or ball.right >= width:
        ball.x, ball.y = width // 2 - ball_size // 2, height // 2 - ball_size // 2
        ball_speed_x *= -1

    # Исправлен отступ для очистки экрана
    screen.fill(black)

    pygame.draw.rect(screen, white, left_paddle)
    pygame.draw.rect(screen, white, right_paddle)
    pygame.draw.ellipse(screen, white, ball)
    pygame.draw.aaline(screen, white, (width // 2, 0), (width // 2, height))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()