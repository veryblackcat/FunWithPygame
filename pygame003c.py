'''
Demo z rakietą podążającą za piłką - wersja obiektowa.
Symulacja ruchu i odbić piłeczki jak w starej grze wideo.
Kąt odbicia piłeczki zmienia się po odbiciu od rakiety gracza.
Obliczanie położenia piłeczki z funkcji liniowej y = ax + b
Wyliczenie b dla znanych wartości a, x, y po przekształceniu
wzoru funkcji liniowej otrzymujemy b = -ax + y jest to konieczne 
przy każdym odbiciu piłeczki.
'''
import pygame
import random

class myGame:
    window_background = (0, 16, 0) # (R, G, B) Kolor tła
    window_size = window_width, window_height = 800, 600
    window_name = "Moja zabawa z Pygame" # Tytuł okienka programu

    # playing field
    playing_field_size = window_width - 100, window_height - 100
    playing_field_color = (0, 48, 0)

    # player
    player_width, player_height = 100, 20 # Rozmiary prostokąta (gracza)
    player_color = (196, 196, 196)          # (R, G, B) Kolor prostokąta (gracza)
    player_step = 5

    # Utworzenie obiektu przechowującego współrzędne prostokąta (gracza).
    player = pygame.Rect(0, 0, player_width, player_height)

    # out
    out_size = playing_field_size[0], player_height
    out_color = (48, 48, 48)

    # ball
    ball = pygame.Rect(0, 0, 30, 30) # Utworzenie obiektu przechowującego współrzędne piłki
    ball_color = (0, 204, 0)
    ball_step = 5

    keys = None

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()

        # window
        self.window = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption(self.window_name) # Ustaw tytuł okienka progamu
        
        # playing field
        self.playing_field = pygame.Surface(self.playing_field_size)
        self.playing_field_rect = pygame.Surface.get_rect(self.playing_field)

        # out
        self.out = pygame.Surface(self.out_size)

        # player
        # Położenie początkowe gracza
        self.player.centerx = self.playing_field_rect.centerx
        self.player.bottom  = self.playing_field_rect.bottom

        # Ustalenia początkowego położenia piłki względem gracza
        self.ball.centerx = self.player.centerx
        self.ball.bottom  = self.player.top-1

        pygame.draw.rect(self.playing_field, self.ball_color, self.ball)

        self.ball_direction = random.uniform(0.4, 2.0) # Losowanie współczynnika kierunkowego a
        self.ball_b_factor = -self.ball_direction * self.ball.centerx + self.ball.bottom # Obliczenie b

        self.run = True

    def kbd(self):
        self.keys = pygame.key.get_pressed()

        if self.keys[pygame.K_ESCAPE]: # ESC - kończy działanie programu
            self.run = False

        if self.keys[pygame.K_LEFT]:  # strzałka w lewo
            pass

        if self.keys[pygame.K_RIGHT]: # strzałka w prawo
            pass

        if self.keys[pygame.K_UP]:    # strzałka w górę
            pass

        if self.keys[pygame.K_DOWN]:  # strzałka w dół
            pass

    def calculate_ball(self):
        y = lambda a, x, b : a * x + b  # y = a*x+b      
        b = lambda a, x, y : -a * x + y # b = -a*x + y
        
        # Obliczenie nowego położenia piłki
        self.ball.centerx += self.ball_step
        self.ball.bottom = y(self.ball_direction, self.ball.centerx, self.ball_b_factor) # y=a*x+b

        # Odbijanie piłki
        if self.ball.right > self.playing_field_rect.right:
            self.ball.right = self.playing_field_rect.right
            self.ball_step *= -1
            self.ball_direction *= -1
            self.ball_b_factor = b(self.ball_direction, self.ball.centerx, self.ball.bottom)
        if self.ball.top < 0:
            self.ball.top = 0
            self.ball_direction *= -1
            self.ball_b_factor = b(self.ball_direction, self.ball.centerx, self.ball.bottom)
        if self.ball.left < 0:
            self.ball.left = 0
            self.ball_step *= -1
            self.ball_direction *= -1
            self.ball_b_factor = b(self.ball_direction, self.ball.centerx, self.ball.bottom)

        # Odbicie piłki od rakiety gracza.
        if self.ball.bottom > self.player.top:
            self.ball.bottom = self.player.top
            # Losowanie współczynnika kierunkowego
            self.ball_direction = -random.uniform(0.4, 2.0) if self.ball_direction > 0 else random.uniform(0.4, 2.0)
            # Obliczenie parametru b funkcji liniowej.
            self.ball_b_factor = b(self.ball_direction, self.ball.centerx, self.ball.bottom)
    
    def moving_player(self):
        # demo - podążanie rakiety gracza za piłką
        self.player.centerx = self.ball.centerx
        if self.player.left < 0: self.player.left = 0
        if self.player.right > self.playing_field_rect.right:
            self.player.right = self.playing_field_rect.right

    def draw(self):
        self.window.fill(self.window_background) # wypełnienie okna kolorem zdefiniowanym w zmiennej window_background

        self.playing_field.fill(self.playing_field_color) # wypełnienie kolorem pola gry

        self.out.fill(self.out_color)
        self.playing_field.blit(self.out, (0, self.playing_field_rect.bottom - self.out_size[1]))
    
        pygame.draw.rect(self.playing_field, self.ball_color, self.ball) # rysowanie piłki
        pygame.draw.rect(self.playing_field, self.player_color, self.player) # rysowanie prostokąta (gracza)
        
        self.window.blit(self.playing_field, (50, 50))
    
        # Wyświetlenia na ekranie
        pygame.display.update()
        #pygame.display.flip()

    def start(self):
        while self.run:
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT: # Jeśli okno programu zostanie zamknięte przyciskiem x
                    self.run = False
        
            self.kbd()
            self.draw()
            self.calculate_ball()
            self.moving_player()

            self.clock.tick(60) # Ograniczenie powtarzania pętli do 60 FPS


game = myGame()

game.start()

pygame.quit()

