import pgzrun
HEIGHT = 600
WIDTH = 800
p = Actor('ironman', (100,100))
c = Actor('cookie_img')

def draw():
    screen.fill('white')
    p.draw()
    c.draw()
    print('drawing')
def update():
    print('updating')
    p.x +=1
    print(p.x, p.y)
    

pgzrun.go()