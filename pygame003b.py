'''
Demo z rakietą podążającą za piłką.
Symulacja ruchu i odbić piłeczki jak w starej grze wideo.
Kąt odbicia piłeczki zmienia się po odbiciu od rakiety gracza.
Obliczanie położenia piłeczki z funkcji liniowej y = ax + b
Wyliczenie b dla znanych wartości a, x, y po przekształceniu
wzoru funkcji liniowej b = -ax + y jest konieczne w przy każdym
odbiciu piłeczki.
'''
import pygame
import random

pygame.init()
clock = pygame.time.Clock()

window_background = (0, 48, 156) # (R, G, B) Kolor tła
window_size = window_width, window_height = 800, 600

window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Moja zabawa z Pygame") # Tytuł okienka

playing_field_size = window_width - 100, window_height - 100
playing_field = pygame.Surface(playing_field_size)
playing_field_rect = pygame.Surface.get_rect(playing_field)

# player
player_width, player_height = 100, 20 # Rozmiary prostokąta (gracza)
player_color = (20, 200, 20)          # (R, G, B) Kolor prostokąta (gracza)
player_step = 5
# Utworzenie obiektu przechowującego współrzędne prostokąta (gracza).
player = pygame.Rect(0, 0, player_width, player_height)
# Położenie początkowe gracza
player.centerx = playing_field_rect.centerx
player.bottom  = playing_field_rect.bottom

# Utworzenie obiektu piłki
ball = pygame.Rect(0, 0, 30, 30)
# Ustalenia początkowego położenia piłki względem pola gry
ball.centerx = playing_field_rect.centerx
ball.bottom  = playing_field_rect.bottom
# Ustalenia początkowego położenia piłki względem gracza
ball.centerx = player.centerx
ball.bottom  = player.top-1

pygame.draw.rect(playing_field, 'white', ball)

ball_direction = random.uniform(0.4, 2.0) # Losowanie współczynnika kierunkowego a
ball_b_factor = -ball_direction * ball.centerx + ball.bottom # Obliczenie b
ball_step = 5


def kbd(keys):
    global player_step, run

    if keys[pygame.K_ESCAPE]: # ESC - kończy działanie programu
        run = False

    if keys[pygame.K_LEFT]:  # strzałka w lewo
        pass

    if keys[pygame.K_RIGHT]:  # strzałka w prawo
        pass

    if keys[pygame.K_UP]:  # strzałka w górę
        pass

    if keys[pygame.K_DOWN]:  # strzałka w dół
        pass

run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Jeśli okno programu zostanie zamknięte przyciskiem x
            run = False

    keys = pygame.key.get_pressed()
    kbd(keys)

    window.fill(window_background) # wypełnienie okna kolorem zdefiniowanym w zmiennej window_background

    playing_field.fill((150, 180, 255)) # wypełnienie kolorem pola gry
    
    pygame.draw.rect(playing_field, 'white', ball) # rysowanie piłki
    pygame.draw.rect(playing_field, player_color, player) # rysowanie prostokąta
    window.blit(playing_field, (50,50))
    
    # Wyświetlenia na ekranie
    pygame.display.update()
    #pygame.display.flip()

    # Obliczenie nowego położenia piłki
    ball.centerx += ball_step
    ball.bottom = ball_direction * ball.centerx + ball_b_factor
    if ball.right > playing_field_rect.right:
        ball.right = playing_field_rect.right
        ball_step *= -1
        ball_direction *= -1
        ball_b_factor = -ball_direction * ball.centerx + ball.bottom
    if ball.top < 0:
        ball.top = 0
        ball_direction *= -1
        ball_b_factor = -ball_direction * ball.centerx + ball.bottom
    if ball.left < 0:
        ball.left = 0
        ball_step *= -1
        ball_direction *= -1
        ball_b_factor = -ball_direction * ball.centerx + ball.bottom
    '''
    if ball.bottom > playing_field_rect.bottom:
        ball.bottom = playing_field_rect.bottom
        if ball_direction > 0:
            ball_direction = -random.uniform(0.4, 2.0) # Losowanie współczynnika kierunkowego
        else:
            ball_direction = random.uniform(0.4, 2.0) # Losowanie współczynnika kierunkowego
        #ball_direction *= -1
        ball_b_factor = -ball_direction * ball.centerx + ball.bottom
    '''
    if ball.bottom > player.top:
        ball.bottom = player.top
        if ball_direction > 0:
            ball_direction = -random.uniform(0.4, 2.0) # Losowanie współczynnika kierunkowego
        else:
            ball_direction = random.uniform(0.4, 2.0) # Losowanie współczynnika kierunkowego
        #ball_direction *= -1
        ball_b_factor = -ball_direction * ball.centerx + ball.bottom   
    # demo
    player.centerx = ball.centerx
    if player.left < 0: player.left = 0
    if player.right > playing_field_rect.right:
        player.right = playing_field_rect.right
    clock.tick(60) # Ograniczenie powtarzania pętli do 60 FPS

pygame.quit()

