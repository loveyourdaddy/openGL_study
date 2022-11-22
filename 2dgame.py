import pygame

# def main():
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("First Game")
path = 'Game/'

walkRight = [pygame.image.load(path+'R1.png'),
    pygame.image.load(path+'R2.png'), 
    pygame.image.load(path+'R3.png'), 
    pygame.image.load(path+'R4.png'), 
    pygame.image.load(path+'R5.png'), 
    pygame.image.load(path+'R6.png'), 
    pygame.image.load(path+'R7.png'), 
    pygame.image.load(path+'R8.png'), 
    pygame.image.load(path+'R9.png')]

walkLeft = [pygame.image.load(path+'L1.png'), 
    pygame.image.load(path+'L2.png'), 
    pygame.image.load(path+'L3.png'), 
    pygame.image.load(path+'L4.png'), 
    pygame.image.load(path+'L5.png'), 
    pygame.image.load(path+'L6.png'), 
    pygame.image.load(path+'L7.png'), 
    pygame.image.load(path+'L8.png'), 
    pygame.image.load(path+'L9.png')]

bg = pygame.image.load(path+'bg.jpg')
char = pygame.image.load(path+'standing.png')

x = 50
y = 400 # 50
width = 40
height = 60
vel = 5

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0

def redrawGameWindow():
    # We have 9 images for our walking animation, I want to show the same image for 3 frames
    # so I use the number 27 as an upper bound for walkCount because 27 / 3 = 9. 9 images shown
    # 3 times each animation.
    global walkCount
    
    win.blit(bg, (0,0))  

    if walkCount + 1 >= 27:
        walkCount = 0
        
    if left:  # If we are facing left
        win.blit(walkLeft[walkCount//3], (x,y))  # We integer divide walkCounr by 3 to ensure each
        walkCount += 1                           # image is shown 3 times every animation
    elif right:
        win.blit(walkRight[walkCount//3], (x,y))
        walkCount += 1
    else:
        win.blit(char, (x, y))  # If the character is standing still
        walkCount = 0
    
        
    pygame.display.update() 
    
run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel: 
        x -= vel
        left = True
        right = False

    elif keys[pygame.K_RIGHT] and x < 500 - vel - width:  
        x += vel
        left = False
        right = True
        
    else: # If the character is not moving we will set both left and right false and reset the animation counter (walkCount)
        left = False
        right = False
        walkCount = 0
        
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False 
            left = False 
            walkCount = 0
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else: 
            jumpCount = 10
            isJump = False

    redrawGameWindow()                
pygame.quit()

# main()