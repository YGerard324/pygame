import pygame

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)

pygame.init()

screen = pygame.display.set_mode((640, 480))

pygame.display.set_caption('Simple Movement')
square = pygame.Rect(300, 230, 20, 20)
left_pad = pygame.Rect(20, 210, 20, 60)
right_pad = pygame.Rect(600, 210, 20, 60)
pads = [left_pad, right_pad]


velocity_x = 0.5
velocity_y = 0.5
clock = pygame.time.Clock()

# Flags para verificar se a tecla está pressionada
up_pressed = False
down_pressed = False

while True:
    dt = clock.tick(30)
    pygame.draw.line(screen, WHITE, [0, 0], [640,0], 5)
    pygame.draw.line(screen, WHITE, [0, 300], [640,300], 50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
            elif event.key == pygame.K_UP:
                up_pressed = True
            elif event.key == pygame.K_DOWN:
                down_pressed = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                up_pressed = False
            elif event.key == pygame.K_DOWN:
                down_pressed = False

    square.move_ip(velocity_x * dt, 0)

    if square.collidelist(pads) >= 0:
        velocity_x = -velocity_x
    # if square.collidelist(margins) >= 0:
    #     velocity_y = -velocity_y

    # Atualiza a posição do pad de acordo com as teclas pressionadas
    if up_pressed:
        left_pad.move_ip(0, -velocity_y * dt)
    if down_pressed:
        left_pad.move_ip(0, velocity_y * dt)

    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, square)

    # Desenha os pads
    for pad in pads:
        pygame.draw.rect(screen, WHITE, pad)

    pygame.display.flip()