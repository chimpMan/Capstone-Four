# getting the pygame library and random library

import pygame 
import random 

# initializing the pygame modules

pygame.init() 

# specifying screen width and height

screen_width = 1000
screen_height = 680

# creating the screen 
screen = pygame.display.set_mode((screen_width,screen_height))


# creating the player

player = pygame.image.load("goodguy.png")

# creating the prize

prize = pygame.image.load("prize.png")

#creating the enemies

enemy = pygame.image.load("enemy.png")
enemy1 = pygame.image.load("enemy1.png")
enemy2 = pygame.image.load("enemy2.png")

# Get the width and height of the images to set object and screen boundaries 

player_height = player.get_height()
player_width = player.get_width()

prize_height = player.get_height()
prize_width = player.get_width()

enemy_height = enemy.get_height()
enemy_width = enemy.get_width()

enemy1_height = enemy.get_height()
enemy1_width = enemy.get_width()

enemy2_height = enemy.get_height()
enemy2_width = enemy.get_width()

print(f"This is the height of the player image:  {(player_height)}")
print(f"This is the width of the player image: {(player_width)}")

# Store the positions of the player, prize and the enemy 

playerXPosition = 100
playerYPosition = 50

prizeXPosition = random.randint(0,screen_width-prize_width)
prizeYPosition = random.randint(0,screen_height-prize_height)


# Make the enemies start off screen and at a random y position.

enemyXPosition =  screen_width
enemyYPosition =  random.randint(0, screen_height - enemy_height)

enemy1XPosition =  screen_width
enemy1YPosition =  random.randint(0, screen_height - enemy_height - enemy1_height)

enemy2XPosition =  screen_width
enemy2YPosition =  random.randint(0, screen_height - enemy_height - enemy1_height - enemy2_height)

# declaring variables for motion keys as boolean types

keyUp = False
keyDown = False
keyLeft = False
keyRight = False

# Creating a loop to cycle through game events

#The indeted code first clears the screen then draws the objects in the game at specified coordinates.

while 1:

    screen.fill(0)
    
    screen.blit(player, (playerXPosition, playerYPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))
    screen.blit(enemy, (enemyXPosition, enemyYPosition))
    screen.blit(enemy1, (enemy1XPosition, enemy1YPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))

    # This updates the screen. 
    
    pygame.display.flip()
    
    # creating a loop to detect quiting the game, pressing buttons down and releasing buttons
    
    for event in pygame.event.get():
    
        # This event checks if the user quits the program, then if so it exits the program. 
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
            
        # This event checks if the user press a key down.
        
        if event.type == pygame.KEYDOWN:
        
            # Test if the key pressed is pressed down K_UP is shorthand for up arrow key etc... .
            
            if event.key == pygame.K_UP: 
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:
                keyLeft = True
            if event.key == pygame.K_RIGHT:
                keyRight = True
        
        # This event checks if the key is up(i.e. not pressed by the user).
        
        if event.type == pygame.KEYUP:
        
            # Test if the key is no longer pressed down
            
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT: 
                keyLeft = False
            if event.key == pygame.K_RIGHT:
                keyRight = False
            
    
    # manipulating the coordinate system to bind motion commands to the arrow keys 
    
    if keyUp == True:
        if playerYPosition > 0 : 
            playerYPosition -= 1
            
    if keyDown == True:
        if playerYPosition < screen_height - player_height:
            playerYPosition += 1

    if keyLeft == True:
        if playerXPosition >0 : 
            playerXPosition -= 1
            
    if keyRight == True:
        if playerXPosition < screen_width: 
            playerXPosition += 1
    
    # Checking the object's interactions by bounding the objects into rectangles.
    
    playerBox = pygame.Rect(player.get_rect())

    prizeBox = pygame.Rect(prize.get_rect())

    enemyBox = pygame.Rect(enemy.get_rect())

    enemy1Box = pygame.Rect(enemy1.get_rect())

    enemy2Box = pygame.Rect(enemy2.get_rect())
 
    # since the object's postions are changing or randomized, the bounding boxes must also be updated with the object's postion. 
    
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition

    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition

    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition

    enemy1Box.top = enemy1YPosition
    enemy1Box.left = enemy1XPosition

    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition
    
    # Test collision of the boxes:

    if (playerBox.colliderect(prizeBox)== False and (playerBox.colliderect(enemyBox) or playerBox.colliderect(enemy1Box) or playerBox.colliderect(enemy2Box))) :
    
        # Display losing status to the user: 
        
        print("You lose!")
       
        # Quite game and exit window: 
        
        pygame.quit()
        exit(0)
        
    # If the player gets the prize, the user wins the game:
    
    if (playerBox.colliderect(prizeBox)):
    
        # Display wining status to the user: 
        
        print("You win!")
        
        # Quite game and exit window: 
        pygame.quit()
        
        exit(0)
   
 
    
    # Make enemy approach the player.
    
    enemyXPosition -= 0.35
    enemy1XPosition -= 0.25
    enemy2XPosition -= 0.50


#A large portion of this code has been heavily borrowed from the example game in Task 15 Level 1.
#The code assisted me to understand how to create a game and I was able to add on 2 extra enemies from the original and also add a prize to the game.
