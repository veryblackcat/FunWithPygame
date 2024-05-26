import pygame

pygame.init()
clock = pygame.time.Clock()

window_background = (24, 164, 240) # (R, G, B) Kolor tła
window_size = window_width, window_height = 800, 600

window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Moja zabawa z Pygame") # Tytuł okienka

player_pos_x, player_pos_y = 70, 70   # Początkowe położenie prostokąta (gracza)
player_width, player_height = 40, 100 # Rozmiary prostokąta (gracza)

# Utworzenie obiektu przechowującego współrzędne prostokąta.
player = pygame.Rect(player_pos_x, player_pos_y, player_width, player_height)

player_color = (20, 200, 20)          # (R, G, B) Kolor prostokąta (gracza)
player_step = 5

txt_pos_x, txt_pos_y = 100, 300       # Położenie tekstu
font = pygame.font.SysFont("Calibri", 48)

run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Jeśli okno programu zostanie zamknięte przyciskiem x
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]: # ESC - kończy działanie programu
        run = False

    
    if keys[pygame.K_LEFT]:  # strzałka w lewo
        player_pos_x -= player_step

    if keys[pygame.K_RIGHT]:  # strzałka w prawo
        player_pos_x += player_step

    if keys[pygame.K_UP]:  # strzałka w górę
        player_pos_y -= player_step

    if keys[pygame.K_DOWN]:  # strzałka w dół
        player_pos_y += player_step

    # Napisy - współrzędne gracza - przygotowanie tekstu jako grafiki
    playerXY_txt = f"x = {player_pos_x}, y = {player_pos_y}"
    playerXY_txt2image = font.render(playerXY_txt, True, (0, 0, 0))

    player.update(player_pos_x, player_pos_y, player_width, player_height)
    
    # Przygotowanie do wyświetlenia
    window.fill(window_background)                           # wypełnienie okna kolorem zdefiniowanym w zmiennej window_background
    pygame.draw.rect(window, player_color, player)           # rysowanie prostokąta (gracza)
    window.blit(playerXY_txt2image, (txt_pos_x, txt_pos_y))  # umieszczenie grafiki zawierającej tekst na ekranie

    # Wyświetlenie na ekranie
    pygame.display.update()
    #pygame.display.flip()

    # Ograniczenie powtarzania pętli do 60 FPS
    clock.tick(60)

pygame.quit()
