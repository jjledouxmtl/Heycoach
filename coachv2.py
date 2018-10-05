import pygame, sys, os

#Currently set to size of court.png file
screen = pygame.display.set_mode((1239,690))

#Initialize variables
draw_on = False
last_pos = (0,0)
color = (0,0,255)
radius = 3

pygame.init()

button_green = pygame.Rect(585, 30, 30, 30)
button_red = pygame.Rect(643, 30, 30, 30)
image_dft = "court.png"

def resetApp(image):
#Set background image of court
    bg = pygame.image.load(image)
    screen.blit(bg, (0,0))
#Setting buttons
    pygame.draw.rect(screen, [0,255,0], button_green)
    pygame.draw.rect(screen, [255,0,0], button_red)
    pygame.display.update()

#Function to draw the lines
def roundline(srf, color, start, end, radius=1):
    dx = end[0]-start[0]
    dy = end[1]-start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        x = int( start[0]+float(i)/distance*dx)
        y = int( start[1]+float(i)/distance*dy)
        pygame.display.update(pygame.draw.circle(srf, color, (x,y), radius))

resetApp(image_dft)

#Pygame loop
try:
    while True:
        e= pygame.event.wait()
        if e.type == pygame.QUIT:
           os.remove("temp.png")
           raise StopIteration
        if e.type == pygame.MOUSEBUTTONDOWN:
            if button_green.collidepoint(e.pos):
                resetApp(image_dft)
            elif button_red.collidepoint(e.pos):
                os.remove("temp.png")
                raise StopIteration
            else:
                if os.path.isfile("temp.png"):
                    resetApp("temp.png")
                pygame.draw.circle(screen, color, e.pos, radius)
                draw_on = True
        if e.type == pygame.MOUSEBUTTONUP:
            draw_on = False
            pygame.image.save(screen, "temp.png")
        if e.type == pygame.MOUSEMOTION:
            if draw_on:
                pygame.display.update(pygame.draw.circle(screen, color, e.pos, radius))
                roundline(screen, color, e.pos, last_pos, radius)
            last_pos = e.pos

except StopIteration:
    pass

pygame.quit()
