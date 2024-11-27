import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# Configuración de pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Galaga")

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Carga x segundo en pantalla
clock = pygame.time.Clock()
FPS = 60

# Agregar fondo
background = pygame.image.load("imagenes/fondo.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Cargar imágenes jugador y enemigos
player_image = pygame.image.load("imagenes/A1.png")
player_image = pygame.transform.scale(player_image, (50, 50))

enemy_image = pygame.image.load("imagenes/E1.png")
enemy_image = pygame.transform.scale(enemy_image, (50, 50))

# Tamaño y velocidad del jugador
player_width, player_height = 50, 50
player_speed = 5

# Proyectiles del jugador
bullet_speed = 7
bullet_width, bullet_height = 5, 15

# Enemigos y proyectil de enemigos
enemy_speed = 2
enemy_bullet_speed = 6

# Generar enemigos
def create_enemy():
    x = random.randint(0, WIDTH - 50)
    y = random.randint(50, 150)
    return [x, y]

# Dibujar el jugador
def draw_player(x, y):
    screen.blit(player_image, (x, y))

# Dibujar enemigos
def draw_enemies(enemy_list):
    for enemy in enemy_list:
        screen.blit(enemy_image, (enemy[0], enemy[1]))

# Dibujar proyectiles
def draw_bullets(bullets, color):
    for bullet in bullets:
        pygame.draw.rect(screen, color, (bullet[0], bullet[1], bullet_width, bullet_height))

# Mover enemigos
def move_enemies(enemy_list):
    for enemy in enemy_list:
        enemy[1] += random.choice([-0.5, 0.5])  # Movimiento vertical 
        enemy[0] += random.choice([-1, 1])  # Movimiento horizontal 
        enemy[0] = max(0, min(enemy[0], WIDTH - 10))  # Limitar movimiento dentro de la pantalla
        enemy[1] = max(0, min(enemy[1], HEIGHT // 2)) # Limitar altura de enemigos a la mitad de la pantalla

# Detectar colisiones
def detect_collision(rect1, rect2):
    return pygame.Rect(rect1).colliderect(pygame.Rect(rect2))

# Menú de controles
def show_controls():
    controls_running = True
    while controls_running:
        screen.blit(background, (0, 0))  # Mostrar fondo

        font = pygame.font.Font(None, 74)
        title_text = font.render("Controles", True, WHITE)
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4))

        font = pygame.font.Font(None, 36)
        controls_text = font.render("Mover: Flechas Izq/Der", True, WHITE)
        shoot_text = font.render("Disparar: ESPACIO", True, WHITE)
        screen.blit(controls_text, (WIDTH // 2 - controls_text.get_width() // 2, HEIGHT // 2))
        screen.blit(shoot_text, (WIDTH // 2 - shoot_text.get_width() // 2, HEIGHT // 2 + 40))

        font = pygame.font.Font(None, 28)
        back_text = font.render("Presiona ESC para volver", True, WHITE)
        screen.blit(back_text, (WIDTH // 2 - back_text.get_width() // 2, HEIGHT - 40))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                controls_running = False

# Menú de objetivo
def show_objective():
    objective_running = True
    while objective_running:
        screen.blit(background, (0, 0))  # Mostrar fondo

        font = pygame.font.Font(None, 74)
        title_text = font.render("Objetivo del Juego", True, WHITE)
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4))

        font = pygame.font.Font(None, 36)
        objective_text = font.render("Acaba con las naves alienígenas", True, WHITE)
        score_text = font.render("y consigue el mayor puntaje posible.", True, WHITE)
        lives_text = font.render("¡Cuidado! Tienes 3 vidas.", True, WHITE)
        screen.blit(objective_text, (WIDTH // 2 - objective_text.get_width() // 2, HEIGHT // 2))
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 + 40))
        screen.blit(lives_text, (WIDTH // 2 - lives_text.get_width() // 2, HEIGHT // 2 + 80))

        font = pygame.font.Font(None, 28)
        back_text = font.render("Presiona ESC para volver", True, WHITE)
        screen.blit(back_text, (WIDTH // 2 - back_text.get_width() // 2, HEIGHT - 40))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                objective_running = False

# Menú inicial
def show_menu():
    menu_running = True
    while menu_running:
        screen.blit(background, (0, 0))  # Mostrar fondo

        font = pygame.font.Font(None, 74)
        title_text = font.render("GALAGA", True, WHITE)
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4))

        font = pygame.font.Font(None, 36)
        start_text = font.render("Presiona ENTER para comenzar", True, WHITE)
        controls_text = font.render("Presiona C para ver controles", True, WHITE)
        objective_text = font.render("Presiona O para ver objetivo", True, WHITE)
        screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2))
        screen.blit(controls_text, (WIDTH // 2 - controls_text.get_width() // 2, HEIGHT // 2 + 40))
        screen.blit(objective_text, (WIDTH // 2 - objective_text.get_width() // 2, HEIGHT // 2 + 80))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Comenzar juego
                    menu_running = False
                if event.key == pygame.K_c:  # Ver controles
                    show_controls()
                if event.key == pygame.K_o:  # Ver objetivo
                    show_objective()

def show_game_over_menu():
    menu_running = True
    while menu_running:
        screen.blit(background, (0, 0))  # Mostrar fondo

        font = pygame.font.Font(None, 74)
        game_over_text = font.render("¡GAME OVER!", True, RED)
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 4))

        font = pygame.font.Font(None, 36)
        retry_text = font.render("Presiona R para reintentar", True, WHITE)
        menu_text = font.render("Presiona M para volver al menú", True, WHITE)
        quit_text = font.render("Presiona ESC para salir", True, WHITE)
        screen.blit(retry_text, (WIDTH // 2 - retry_text.get_width() // 2, HEIGHT // 2))
        screen.blit(menu_text, (WIDTH // 2 - menu_text.get_width() // 2, HEIGHT // 2 + 50))
        screen.blit(quit_text, (WIDTH // 2 - quit_text.get_width() // 2, HEIGHT // 2 + 100))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Reintentar
                    menu_running = False
                    game()
                if event.key == pygame.K_m:  # Volver al menú principal
                    menu_running = False
                    show_menu()  # Volver al menú principal
                if event.key == pygame.K_ESCAPE:  # Salir
                    pygame.quit()
                    sys.exit()

# Juego principal
def game():
    player_x = WIDTH // 2
    player_y = HEIGHT - 70
    player_bullets = []
    enemy_bullets = []
    enemy_list = [create_enemy() for _ in range(8)]
    score = 0
    lives = 3  # Vidas del jugador
    running = True

    while running:
        screen.blit(background, (0, 0))  # Dibujar fondo

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Movimiento del jugador
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
            player_x += player_speed
        if keys[pygame.K_SPACE]:  # Disparar
            if len(player_bullets) < 5:
                player_bullets.append([player_x + player_width // 2 - bullet_width // 2, player_y])

        # Mover proyectiles del jugador
        for bullet in player_bullets:
            bullet[1] -= bullet_speed
        player_bullets = [bullet for bullet in player_bullets if bullet[1] > 0]

        # Mover enemigos
        move_enemies(enemy_list)

        # Enemigos disparan
        if enemy_list and random.randint(1, 25) == 1:  # Verificar que la lista no esté vacía
            random_enemy = random.choice(enemy_list)
            enemy_bullets.append([random_enemy[0] + 25, random_enemy[1] + 50])

        # Regenerar enemigos si todos han sido eliminados
        if not enemy_list:
            for _ in range(8):  # Generar nuevos enemigos
                enemy_list.append(create_enemy())

        # Mover balas enemigas
        for bullet in enemy_bullets:
            bullet[1] += enemy_bullet_speed
        enemy_bullets = [bullet for bullet in enemy_bullets if bullet[1] < HEIGHT]

        # Detectar colisiones entre balas del jugador y enemigos
        for bullet in player_bullets:
            for enemy in enemy_list:
                if detect_collision(
                    (bullet[0], bullet[1], bullet_width, bullet_height),
                    (enemy[0], enemy[1], player_width, player_height),
                ):
                    enemy_list.remove(enemy)
                    score += 10
                    break

        # Detectar colisiones entre balas enemigas y el jugador
        for bullet in enemy_bullets:
            if detect_collision(
                (bullet[0], bullet[1], bullet_width, bullet_height),
                (player_x, player_y, player_width, player_height),
            ):
                enemy_bullets.remove(bullet)
                lives -= 1
                if lives == 0:
                    running = False

        # Detectar colisiones entre enemigos y el jugador
        for enemy in enemy_list:
            if detect_collision(
                (enemy[0], enemy[1], player_width, player_height),
                (player_x, player_y, player_width, player_height),
            ):
                lives -= 1
                enemy_list.remove(enemy)
                if lives == 0:
                    running = False

        # Dibujar elementos
        draw_player(player_x, player_y)
        draw_enemies(enemy_list)
        draw_bullets(player_bullets, YELLOW)
        draw_bullets(enemy_bullets, RED)

        # Mostrar puntaje y vidas
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Puntaje: {score}", True, WHITE)
        lives_text = font.render(f"Vidas: {lives}", True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (10, 50))

        pygame.display.flip()
        clock.tick(FPS)
    show_game_over_menu()

# Ejecutar el juego
if __name__ == "__main__":
    show_menu()
    game()