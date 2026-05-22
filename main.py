Web VPython 3.2
import random
scene = canvas(title = 'ping pong!', width = 650, height = 400)
bar1 = box(pos=vector(-0.8, 0, 0), size=vector(0.1, 0.8, 0.5), color=color.white)
bar2 = box(pos=vector(0.8, 0, 0), size=vector(0.1, 0.8, 0.5), color=color.white) 
velocity = vector(0.05, 0, 0)
t = 0
dt = 0.05
speed = 0.5
amplitude = 1

ball = sphere(pos=vector(0, 0, 0), radius=0.065)
velocity = vector(0.01, 0, 0)
color_list = [color.red, color.orange, color.yellow, color.green, color.blue, color.purple]
color_index = 0

while True:
    rate(50)
    bar1.pos.y = amplitude * sin(speed * t)
    bar2.pos.y = amplitude * sin(speed * t)
    t += dt
    
    ball.pos = ball.pos + velocity
    if ball.pos.x > 0.71 or ball.pos.x < -0.71:
        velocity.x = -velocity.x
    k = keysdown()
    if ' ' in k and (ball.pos.x > 0.71 or ball.pos.x < -0.71)  :
        ball.color = color_list[random.randint(0,2)]

