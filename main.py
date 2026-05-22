Web VPython 3.2
import random
ball = sphere(pos=vector(0, 0, 0), radius=0.05)
velocity = vector(0.01, 0, 0)

box(pos=vector(-0.8, 0, 0), size=vector(0.1, 0.8, 0.5), color=color.white)
box(pos=vector(0.8, 0, 0), size=vector(0.1, 0.8, 0.5), color=color.white)

color_list = [color.red, color.orange, color.yellow, color.green, color.green, color.blue, color.purple] 
color_index = 0

while True:
    rate(60)
    ball.pos = ball.pos + velocity
   
    if ball.pos.x > 0.71 or ball.pos.x < -0.71:
        velocity.x = -velocity.x
    k = keysdown()
    if ' ' in k and (ball.pos.x > 0.71 or ball.pos.x < -0.71)  :
        ball.color = color_list[random.randint(0,2)]
