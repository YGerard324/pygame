import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

screen = pygame.display.set_mode((640, 480))

pygame.display.set_caption('Game Loop')

# variáveis da bola
position_x = 300
position_y = 200
velocity_x = 0.2
velocity_y = 0.2

while True:
    #Captura eventos
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break

    #ATUALIZANDO O JOGO

    #movendo a bola
    position_x += velocity_x
    position_y += velocity_y

    #mudando a direção do eixo x nas bordas
    if position_x > 600:
        velocity_x = -0.2
    elif position_x < 0:
        velocity_x = 0.2
    
    #mudando a direção do eixo y nas bordas
    if position_y > 440:
        velocity_y = -0.2
    elif position_y < 0:
        velocity_y = 0.2

    #DESENHO
    
    #preenchendo o fundo com preto
    screen.fill(BLACK)

    #desenhando a bola
    pygame.draw.ellipse(screen, RED, [position_x, position_y, 40, 40])

    #atualizando a tela
    pygame.display.flip()


