
import pygame
from pygame import mixer
    
#initializing pygame
pygame.init()
pygame.mixer.init ()

screen = pygame.display.set_mode((800,400))#creating a screen with 800px height and 400px width
clock= pygame.time.Clock() #creating a clock
font = pygame.font.Font('C:/Users/Elève/Desktop/shit/Pixeltype.ttf',50)#creating font variable
mixer.music.load('C:/Users/Elève/Desktop/shit/travis.wav')
mixer.music.play()


gameActive = True
img = pygame.image.load("C:/Users/Elève/Desktop/shit/Sky.png").convert_alpha()#importing img
img = pygame.transform.scale(surface=img, size=(800,400))#img size wholescreen
ground = pygame.image.load("C:/Users/Elève/Desktop/shit/ground.png").convert_alpha()#idem
ground = pygame.transform.scale(surface=ground, size=(800,100))#idem
character = pygame.image.load("C:/Users/Elève/Desktop/shit/chrctr.png").convert_alpha()#idem
character = pygame.transform.scale(surface=character, size=(50,60))#idem
characterRect = character.get_rect(topleft=(600,258))  #creating a rectangle for img character
character2 = pygame.image.load("C:/Users/Elève/Desktop/shit/chrctr.png").convert_alpha()#idem
character2 = pygame.transform.scale(surface=character2, size=(80,95))#idem
character2Rect = character2.get_rect(topleft=(585,230))
maincr = pygame.image.load("C:/Users/Elève/Desktop/shit/maincr.png").convert_alpha()#idem
maincr = pygame.transform.scale(surface=maincr, size=(120,70))#idem
maincrRect = maincr.get_rect(topleft=(80,244))#creating character for img maincr
textintro = font.render('Game', False, 'Black')#putting text and using font variable
textintroRect = textintro.get_rect(topleft= (350,50))
gravity = 25
uaaaa = font.render('UAAAAAAAA', False, 'Black')
#Game loop
while True:
    for event in pygame.event.get():#in pygame
     if event.type == pygame.QUIT:#if you quit
         pygame.quit()#quit pygame
         exit()#exit
     #if event.type == pygame.MOUSEMOTION:
        # if maincrRect.collidepoint(event.pos): print("collision")
     #if event.type == pygame.MOUSEBUTTONDOWN:
         #if maincrRect.collidepoint(event.pos):
             # gravity -= 20
     
     if event.type == pygame.KEYDOWN: 
         if event.key == pygame.K_p and maincrRect.bottom >= 300: 
             gravity = -7

     if event.type == pygame.KEYDOWN: 
         if event.key == pygame.K_o and maincrRect.bottom >= 300: 
             gravity = -10
            
     
     #if  event.type == pygame.KEYUP:
        # print("keyup")
    if gameActive:
        screen.blit(img,(0,0))#display img
        characterRect.x -=9 #moving img rectangle to left at a rate of 3px per frame
        if characterRect.right < -100: characterRect.left = 800#if the character depasse -100 px move to 800 right
        screen.blit(character,characterRect)#display img with height of 258px and variable width
        character2Rect.x -=9
        if character2Rect.right < -100: character2Rect.left = 8900
        screen.blit(character2,character2Rect)
        screen.blit(ground,(0,300))#display img down 300px
        screen.blit(textintro,textintroRect)#diplay text down 50px and left 300px
        gravity += 0.2
        maincrRect.y += gravity
        if maincrRect.bottom >= 300: maincrRect.bottom = 300  
        screen.blit(maincr,maincrRect)#display pos using variable maincrRect
        
        
    if maincrRect.colliderect(characterRect):
        scream = mixer.Sound('C:/Users/Elève/Desktop/shit/scream.wav')
        scream.play()

    if maincrRect.colliderect(characterRect):
        gameActive = False
        screen.fill("Yellow")
        screen.blit(uaaaa,(300,170))

    if maincrRect.colliderect(character2Rect):
        gameActive = False
        screen.fill("Yellow")
        screen.blit(uaaaa,(300,170))

    if maincrRect.colliderect(character2Rect):
        scream = mixer.Sound('C:/Users/Elève/Desktop/shit/scream.wav')
        scream.play()

    
    pygame.display.update()#updtate screen
    clock.tick(60) #game locked at 60fps
