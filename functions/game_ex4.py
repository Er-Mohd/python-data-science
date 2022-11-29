import pgzrun

WIDTH = 1240
HEIGHT = 900
scr = 0

def gamescr(bgcolor, title, info="Play the game"):
    screen.fill(bgcolor)
    screen.draw.text(title,
        center=(WIDTH/2, HEIGHT/2),
        fontsize=100, color='white',align='center')
    screen.draw.text(info,
        center=(WIDTH/2, HEIGHT/2+100),
        fontsize=50, color='white',align='center')



def draw():
     if scr==0:
       gamescr('black', 'Amazing game', 'press space to start')
     elif scr ==1:
         gamescr('green', 'game is running', )
     elif scr == 2:
         gamescr('red', 'game over', 'press enter to restart')

        
    
def update():
    global scr
    if keyboard.SPACE and scr == 0:
        scr = 1
    if keyboard.ESCAPE and scr == 1:
        scr = 2
    if keyboard.RETURN and scr == 2:
        scr = 0

    pass

pgzrun.go()