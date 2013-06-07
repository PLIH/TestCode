#Source File Name: GUIAttemptPyGame.py
#Author's Name: Paige Harvey
#Last Modified By: Paige Harvey
#Last Modified On: 2012-06-03
#Program Description: Slot Machine based on Star Trek
#Revision History:
#  - GUI attempt 2

import pygame, Buttons

##                    Buttons.py was NOT written by Paige Harvey
##                        It was written by Simon H. Larsen,
##                        who then made it avaliable for download,
##                        which was linked to PYGAME.org.
##                    P Harvey downloaded it on June 3, 2013.
##
##                !~ REPEAT ~!
##                    P Harvey did NOT write Buttons.py

def texts(toPrint):
    font = pygame.font.SysFont("None", 30)
    label = font.render(toPrint, 1, (255,255,255))
    return label

def main():
    pygame.init()

    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Trouble with Tribbles: Slot Machine")

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background = pygame.image.load("background.png")
    

    #Buttons?
    button1 = Buttons.Button()

    
    clock = pygame.time.Clock()
    keepGoing = True
    caption = ""

    while keepGoing:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button1.pressed(pygame.mouse.get_pos()):
                        caption = "Give me a command!"

        screen.blit(background, (0, 0))
        button1.create_button(screen, (107,142,35), 150, 135, 50, 25, 0, " 5 ", (255,255,255))
        myLabel = texts(caption)
        screen.blit(myLabel, (450,450))
        pygame.display.flip()

if __name__ == "__main__": main()
