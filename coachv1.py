import pygame

#Currently set to size of court.png file
screen = pygame.display.set_mode((826,460))

#Initialize variables
draw_on = False
last_pos = (0,0)
color = (0,0,255)
radius = 3

pygame.init()

#Set background image of court
bg = pygame.image.load("court.png")
screen.blit(bg, (0,0))
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

#Pygame loop
try:
    while True:
        e= pygame.event.wait()
        if e.type == pygame.QUIT:
            raise StopIteration
        if e.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.circle(screen, color, e.pos, radius)
            draw_on = True
        if e.type == pygame.MOUSEBUTTONUP:
            draw_on = False
        if e.type == pygame.MOUSEMOTION:
            if draw_on:
                pygame.display.update(pygame.draw.circle(screen, color, e.pos, radius))
                roundline(screen, color, e.pos, last_pos, radius)
            last_pos = e.pos

except StopIteration:
    pass

pygame.quit()
