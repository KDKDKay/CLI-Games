import pygame
from pygame import mixer
import random
import math

# Initializes the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# background
backgroundImg = pygame.image.load("Background.jpg")

# background sound
mixer.music.load("background.wav")
mixer.music.play(-1)  # -1 plays on loop

# title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("spaceship_img.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("rocket.png")
playerX = 370
playerY = 480
playerX_change = 0

# Alien
alienImg = []
alienX = []
alienY = []
alienX_change = []
alienY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    alienImg.append(pygame.image.load("alien.png"))
    alienX.append(random.randint(0, 735))
    alienY.append(random.randint(50, 150))
    alienX_change.append(4)
    alienY_change.append(40)

# Bullet
bulletImg = pygame.image.load("spaceship_img.png")
bulletX = 0
bulletY = 480  # as the spaceship is stationary here
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"  # ready = can't see bullet on screen, fire = bullet is moving

# Score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)

textX = 10
textY = 10

# Game over text
over_font = pygame.font.Font("freesansbold.ttf", 64)


def game_over_text():
    over_text = over_font.render(f"GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def show_score(x, y):
    score = font.render(f"Score: {score_value}", True, (255, 255, 255))
    screen.blit(score, (x, y))


def player(x, y):
    # blit draws image onto the game window
    screen.blit(playerImg, (x, y))


def alien(x, y, i):
    # blit draws image onto the game window
    screen.blit(alienImg[i], (x, y))


def fire_bullet(x, y):
    # blit draws image onto the game window
    global bullet_state
    bullet_state = "fire"
    screen.blit(
        bulletImg, (x + 16, y + 10)
    )  # so the bullet appears at the centre, nose of the spaceship


def isCollision(alienX, alienY, bulletX, bulletY):
    distance = math.sqrt(
        (math.pow((alienX - bulletX), 2)) + (math.pow((alienY - bulletY), 2))
    )
    if distance < 27:
        return True
    else:
        return False


# Game Loop
running = True
while running:
    # RGB
    screen.fill((0, 0, 0))
    # keeps background image running
    screen.blit(backgroundImg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check if it is right or left
        # keydown is pressing key and key up in releasing
        if event.type == pygame.KEYDOWN:
            # print("keystroke is pressed")
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound("laser.wav")
                    bullet_sound.play()
                    # get current location of spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # setting spaceship boundaries
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX > 736:  # change this number as 800 - the image size 32/64
        playerX = 736

    # enemy movement
    for i in range(num_of_enemies):
        # Game over
        if alienY[i] > 440:
            for j in range(num_of_enemies):
                alienY[j] = 2000
            game_over_text()
            break

        alienX[i] += alienX_change[i]
        if alienX[i] <= 0:
            alienX_change[i] = 2
            alienY[i] += alienY_change[i]
        elif alienX[i] > 736:  # change this number as 800 - the image size 32/64
            alienX_change[i] = -2
            alienY[i] += alienY_change[i]
        # Collision
        collision = isCollision(alienX[i], alienY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound("explosion.wav")
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            print(f"Your score is: {score_value}")
            # respawn the alien
            alienX[i] = random.randint(0, 735)
            alienY[i] = random.randint(50, 150)

        alien(alienX[i], alienY[i], i)

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)

    # ensures the screen continually updates - need to make sure you code this after each action
    pygame.display.update()
