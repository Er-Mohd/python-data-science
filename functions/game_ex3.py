import pgzrun
from random import randint

HEIGHT = 600
WIDTH = 1200

p = Actor('ironman',center = (WIDTH//2,HEIGHT//2))
c = Actor('cookie_img',(randint(0,WIDTH), randint(0,HEIGHT)))
title = "IRON-MAN GAME"
score = 0
music.play('lovebgm')
def draw():
      screen.fill('white')
      screen.draw.text(title,center=(WIDTH//2,30),fontsize = 60,
          color = 'black', align = 'center', shadow=(.2,1),scolor = "red")
      screen.draw.text(f'score: {score}', (10,10), fontsize=10, color='black')
      #screen.draw.text(title,(10,10),fontsize = 30,color = 'black') 
      p.draw()
      c.draw()
def p_move():
      if keyboard.left and p.right < WIDTH:
            p.x += 3
      elif keyboard.right and p.left > 0:
            p.x -=3
      elif keyboard.up and p.top > 0:
            p.y -=3
      elif keyboard.down and p.bottom < HEIGHT:
            p.y +=3
      pass

def update():
      global score # tell python,that we want to change the value of global variable score
      p_move()    #function Call    # Function Call
      if p.colliderect(c):
          score +=1
          c.pos = (randint(0,WIDTH), randint(0,HEIGHT))
          sound.s1.play()
      print(p.x,p.y, p.angle)

pgzrun.go()