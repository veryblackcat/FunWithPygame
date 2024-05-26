import pygame

pygame.init()
clock = pygame.time.Clock()

window_background = (24, 164, 240) # (R, G, B) Kolor tła
window_size = window_width, window_height = 800, 600

window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Moja zabawa z Pygame") # Tytuł okienka

player_pos_x, player_pos_y = 70, 70   # Początkowe położenie prostokąta (gracza)
player_width, player_height = 40, 100 # Rozmiary prostokąta (gracza)
player_color = (20, 200, 20)          # (R, G, B) Kolor prostokąta (gracza)
player_step = 5

# Utworzenie obiektu przechowującego współrzędne prostokąta bounding box.
# Współrzędne i rozmiar w tym miejscu są bez znaczenia,
# ponieważ są obliczane w głównej pętli programu.
box = pygame.Rect(0, 0, 0, 0)

# Utworzenie obiektu przechowującego współrzędne prostokąta (gracza).
player = pygame.Rect(player_pos_x, player_pos_y, player_width, player_height)

player_limit_max_x = window_width -1 - player_width
player_limit_max_y = window_height -1 - player_height

txt_pos_x, txt_pos_y = 100, 300 # Położenie tekstu
font = pygame.font.SysFont("Calibri", 48)

def kbd(keys):
    global player_pos_x, player_pos_y, player_width, player_width, player_step, run

    if keys[pygame.K_ESCAPE]: # ESC - kończy działanie programu
        run = False

    if keys[pygame.K_LEFT]:  # strzałka w lewo
        if player_pos_x - player_step > 0:
            player_pos_x -= player_step
        else:
            player_pos_x = 0

    if keys[pygame.K_RIGHT]:  # strzałka w prawo
        if player_pos_x + player_step < player_limit_max_x:
            player_pos_x += player_step
        else:
            player_pos_x = player_limit_max_x

    if keys[pygame.K_UP]:  # strzałka w górę
        if player_pos_y - player_step > 0:
            player_pos_y -= player_step
        else:
            player_pos_y = 0

    if keys[pygame.K_DOWN]:  # strzałka w dół
        if player_pos_y + player_step < player_limit_max_y:
            player_pos_y += player_step
        else:
            player_pos_y = player_limit_max_y

run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Jeśli okno programu zostanie zamknięte przyciskiem x
            run = False

    keys = pygame.key.get_pressed()
    kbd(keys)

    player.update(player_pos_x, player_pos_y, player_width, player_height)

    # Napisy - współrzędne gracza - przygotowanie tekstu jako grafiki
    playerXY_txt = f"x = {player_pos_x}, y = {player_pos_y}"
    playerXY_txt2image = font.render(playerXY_txt, True, (0, 0, 0))

    # Rozmiar obrazu z tekstem pygame.Surface.get_size zwraca krotkę zawierającą szerokość i wysokość
    # playerXY_txt2img_size = pygame.Surface.get_size(playerXY_txt2image) # zwraca krotkę
    playerXY_txt2img_width, playerXY_txt2img_height = pygame.Surface.get_size(playerXY_txt2image)

    # Obrys (bounding box)
    # left x
    if player_pos_x < txt_pos_x:
        box_pos_x = player_pos_x
    else: 
        box_pos_x = txt_pos_x
    # top y
    if player_pos_y < txt_pos_y:
        box_pos_y = player_pos_y
    else:
        box_pos_y = txt_pos_y
    # width
    if player_pos_x + player_width > txt_pos_x + playerXY_txt2img_width:
        box_width = player_pos_x + player_width - box_pos_x
    else:
        box_width = txt_pos_x + playerXY_txt2img_width - box_pos_x
    # height
    if player_pos_y + player_height > txt_pos_y + playerXY_txt2img_height:
        box_height = player_pos_y + player_height - box_pos_y
    else:
        box_height = txt_pos_y + playerXY_txt2img_height - box_pos_y

    box.update(box_pos_x, box_pos_y, box_width, box_height)
    
    # Przygotowanie do wyświetlenia
    window.fill(window_background)                           # wypełnienie okna kolorem zdefiniowanym w zmiennej window_background
    pygame.draw.rect(window, player_color, player)           # rysowanie prostokąta (gracza)
    window.blit(playerXY_txt2image, (txt_pos_x, txt_pos_y))  # umieszczenie grafiki zawierającej tekst na ekranie
    pygame.draw.rect(window, (128,0,0), box, width=2)        # rysowanie prostokąta (obrysu)

    # Wyświetlenia na ekranie
    pygame.display.update()
    #pygame.display.flip()
        
    clock.tick(60) # Ograniczenie powtarzania pętli do 60 FPS

pygame.quit()

