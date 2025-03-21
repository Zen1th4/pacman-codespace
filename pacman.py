import pygame
import random

# Inizializza Pygame
pygame.init()

# Imposta le dimensioni dello schermo
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pac-Man")

# Imposta i colori
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# Imposta le dimensioni del personaggio e del labirinto
pacman_size = 20
maze_width = 20
maze_height = 20

# Crea il labirinto
maze = [
    "####################",
    "#........##........#",
    "#.#####.##.#####.#",
    "#.#...#.##.#...#.#",
    "#.#.###.##.###.#.#",
    "#.#.....  .....#.#",
    "#.#####.##.#####.#",
    "#........##........#",
    "####################",
]

# Imposta la posizione iniziale di Pac-Man
pacman_x = 10
pacman_y = 10

# Imposta la velocità di Pac-Man
pacman_speed = 5

# Imposta la posizione iniziale dei fantasmi
ghost_x = 280
ghost_y = 280

# Imposta la velocità dei fantasmi
ghost_speed = 3

# Imposta la direzione iniziale di Pac-Man
pacman_direction = "right"

# Imposta la direzione iniziale dei fantasmi
ghost_direction = "left"

# Imposta il punteggio
score = 0

# Imposta il font
font = pygame.font.Font(None, 36)

# Ciclo principale del gioco
running = True
while running:
    # Gestisci gli eventi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pacman_direction = "left"
            elif event.key == pygame.K_RIGHT:
                pacman_direction = "right"
            elif event.key == pygame.K_UP:
                pacman_direction = "up"
            elif event.key == pygame.K_DOWN:
                pacman_direction = "down"

    # Muovi Pac-Man
    if pacman_direction == "left":
        pacman_x -= pacman_speed
    elif pacman_direction == "right":
        pacman_x += pacman_speed
    elif pacman_direction == "up":
        pacman_y -= pacman_speed
    elif pacman_direction == "down":
        pacman_y += pacman_speed

    # Controlla la collisione con i muri
    if maze[pacman_y // maze_height][pacman_x // maze_width] == "#":
        if pacman_direction == "left":
            pacman_x += pacman_speed
        elif pacman_direction == "right":
            pacman_x -= pacman_speed
        elif pacman_direction == "up":
            pacman_y += pacman_speed
        elif pacman_direction == "down":
            pacman_y -= pacman_speed

    # Controlla la collisione con i puntini
    if maze[pacman_y // maze_height][pacman_x // maze_width] == ".":
        score += 10
        maze[pacman_y // maze_height] = maze[pacman_y // maze_width].replace(".", " ", 1)

    # Muovi i fantasmi
    if ghost_direction == "left":
        ghost_x -= ghost_speed
    elif ghost_direction == "right":
        ghost_x += ghost_speed
    elif ghost_direction == "up":
        ghost_y -= ghost_speed
    elif ghost_direction == "down":
        ghost_y += ghost_speed

    # Controlla la collisione con i muri per i fantasmi
    if maze[ghost_y // maze_height][ghost_x // maze_width] == "#":
        if ghost_direction == "left":
            ghost_x += ghost_speed
        elif ghost_direction == "right":
            ghost_x -= ghost_speed
        elif ghost_direction == "up":
            ghost_y += ghost_speed
        elif ghost_direction == "down":
            ghost_y -= ghost_speed

    # Controlla la collisione con Pac-Man
    if pacman_x == ghost_x and pacman_y == ghost_y:
        running = False

    # Disegna lo schermo
    screen.fill(black)

    # Disegna il labirinto
    for y, row in enumerate(maze):
        for x, char in enumerate(row):
            if char == "#":
                pygame.draw.rect(screen, blue, (x * maze_width, y * maze_height, maze_width, maze_height))
            elif char == ".":
                pygame.draw.circle(screen, white, (x * maze_width + maze_width // 2, y * maze_height + maze_height // 2), 5)

    # Disegna Pac-Man
    pygame.draw.circle(screen, yellow, (pacman_x, pacman_y), pacman_size)

    # Disegna i fantasmi
    pygame.draw.circle(screen, red, (ghost_x, ghost_y), pacman_size)

    # Disegna il punteggio
    text = font.render(f"Punteggio: {score}", True, white)
    screen.blit(text, (10, 10))

    # Aggiorna lo schermo
    pygame.display.flip()

# Esci da Pygame
pygame.quit()
