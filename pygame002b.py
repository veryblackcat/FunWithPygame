''' Rysowanie prostokąta bounding box
Efekt działania tego skrypyu jest taki sam jak skryptu pygame002a.py
Wykorzystanie atrybutów wirtualnych obiektu pygame.Rect
oraz metody pygame.Rect.union() umożliwiło uproszczenie kodu.
'''
import pygame

pygame.init()
clock = pygame.time.Clock()

window_background = (24, 164, 240) # (R, G, B) Kolor tła
window_size = window_width, window_height = 800, 600

window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Moja zabawa z Pygame - Bounding Box ver. 2") # Tytuł okienka

# player
player_pos_x, player_pos_y = 70, 70   # Początkowe położenie prostokąta (gracza)
player_width, player_height = 40, 100 # Rozmiary prostokąta (gracza)
player_color = (20, 200, 20)          # (R, G, B) Kolor prostokąta (gracza)
player_step = 5

# Utworzenie obiektu przechowującego współrzędne prostokąta (gracza).
player = pygame.Rect(player_pos_x, player_pos_y, player_width, player_height)

# tekst
txt_pos_x, txt_pos_y = 100, 300 # Położenie tekstu
txt_color = (0, 0, 0)
font = pygame.font.SysFont("Calibri", 48)

def kbd(keys):
    global player_step, run

    if keys[pygame.K_ESCAPE]: # ESC - kończy działanie programu
        run = False

    if keys[pygame.K_LEFT]:  # strzałka w lewo
        if player.left - player_step > 0:
            player.left -= player_step
        else:
            player.left = 0

    if keys[pygame.K_RIGHT]:  # strzałka w prawo
        if player.right + player_step < window_width:
            player.right += player_step
        else:
            player.right = window_width

    if keys[pygame.K_UP]:  # strzałka w górę
        if player.top - player_step > 0:
            player.top -= player_step
        else:
            player.top = 0

    if keys[pygame.K_DOWN]:  # strzałka w dół
        if player.bottom + player_step < window_height:
            player.bottom += player_step
        else:
            player.bottom = window_height

run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Jeśli okno programu zostanie zamknięte przyciskiem x
            run = False

    keys = pygame.key.get_pressed()
    kbd(keys)

    # Napisy - współrzędne gracza - przygotowanie tekstu jako grafiki
    playerXY_txt = f"x = {player.left}, y = {player.top}"
    playerXY_txt2image = font.render(playerXY_txt, True, txt_color)

    # Przygotowanie do wyświetlenia
    window.fill(window_background)                 # wypełnienie okna kolorem zdefiniowanym w zmiennej window_background
    pygame.draw.rect(window, player_color, player) # rysowanie prostokąta (gracza)
    txt_rect = window.blit(playerXY_txt2image, (txt_pos_x, txt_pos_y))  # umieszczenie grafiki zawierającej tekst na ekranie
    
    # Utworzenie (bounding box) obrysu prostokąta (gracza) i tekstu.
    # union() - zwraca współrzędne i rozmiary prostokąta obejmującego dwa prostokąty
    bounding_box = pygame.Rect.union(player, txt_rect)
    pygame.draw.rect(window, (128,0,0), bounding_box, width=2) # rysowanie prostokąta bounding box

    # Wyświetlenia na ekranie
    pygame.display.update()
    #pygame.display.flip()
        
    clock.tick(60) # Ograniczenie powtarzania pętli do 60 FPS

pygame.quit()

