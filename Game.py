import pgzrun
import pygame
import random
WIDTH = 500
HEIGHT = 500
#make actor
vector = Actor("rabbit")
vector2 = Actor("rabbit")
vector.x = WIDTH / 2
vector.y = HEIGHT / 2
points = 0
font = pygame.font.Font("fonts/arial.ttf",36)
def draw() :
    screen.fill("black")
    vector.draw()
    screen.draw.text(f"points:{points}",(100,50),fontname = "arial", fontsize=32,color = "white")

def on_mouse_down(pos) :
    global points
    if vector.collidepoint(pos) :
        vector.x = random.randint(50,450)
        vector.y = random.randint(50,450)
        points += 1
           
pgzrun.go()  
  