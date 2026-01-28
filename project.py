import pgzrun

HEIGHT = 1000
WIDTH = 1000

def draw():
    screen.fill("red")

    x = 0
    y = 0
    for row in range (10):    
        for colomn in range (5):
            if is_even(row):
                screen.draw.filled_circle((x +50, y + 50), 50,(65,105,225))

                rect = Rect((x + 100, y), (100, 100))
                screen.draw.filled_rect(rect, (124,252,0))
            else:
                screen.draw.filled_circle((x +50, y + 50), 50,(65,105,225))

                rect = Rect((x + 0, y), (100, 100))
                screen.draw.filled_rect(rect, (124,252,0))
                

            x += 200
        x = 0
        y += 100

def is_even(n):
    return n % 2 == 0
        
def update():
   pass   

pgzrun.go()