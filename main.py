Web VPython 3.2
import random

scene = canvas(title = 'Ping Pong!', width = 650, height = 400) #배경 생성(제목,가로,세로)
bar1 = box(pos=vector(-0.8, 0, 0), size=vector(0.1, 1.8, 0.5), color=color.white) #바1 생성(위치,크기,색깔)
bar2 = box(pos=vector(0.8, 0, 0), size=vector(0.1, 1.8, 0.5), color=color.white) #바2생성(위치,크기,색깔)

t = 0 #시간
dt = 0.05 #시간의 간격/정밀도
speed = 0.5 #속도 조절 나사
amplitude = 0.5 #진폭/움직임 범위

ball = sphere(pos=vector(0, 0, 0), radius=0.065) #공 생성(중심(0, 0, 0)에 반지름 (0.065) 크기)
velocity = vector(0.01, 0.01, 0) #속도 설정(x,y축 방향으로 매순간 0.01씩 이동)
color_list = [color.red, color.orange, color.yellow, color.green, color.blue, color.purple] #색깔 리스트(빨,주,노,초,파,보)

while True:     #무한 반복
    rate(50)    #초당 50번 반복
    bar1.pos.y = amplitude * sin(speed * t) #바1이 시간이 흘러도 결과값이 -1과 1사이를 부드럽게 이동(진폭과 곱하여 -0.5와 0.5사이를 부드럽게 이동)
    bar2.pos.y = amplitude * sin(speed * t) #바2가 시간이 흘러도 결과값이 -1과 1사이를 부드럽게 이동(진폭과 곱하여 -0.5와 0.5사이를 부드럽게 이동)
    t += dt     #t = t + dt(매 순간 흘러간 시간 간격(dt = 0.05)만큼 현재 시간(t)을 계속 누적해서 더해주는 것)
    
    ball.pos = ball.pos + velocity  #공의 이동(현재 공의 위치에 속도(velocity)를 더해서 새로운 위치로 바꾸기)
    if ball.pos.x > 0.71 or ball.pos.x < -0.71:  #충돌 감지(벽의 한계점에 닿았을 때)
        velocity.x = -velocity.x    #튕겨 나가기(이동 방향 역전)
        ball.color = random.choice(color_list)  #색상 변경(닿았을 때 색깔 리스트에서 랜덤으로 색을 하나 가져옴)
   
    if ball.pos.y > 1 or ball.pos.y < -1:   #위아래 벽 감지(벽의 한계점에 닿았을 때)
        velocity.y = -velocity.y            #튕겨 나가기(이동 방향 역전)
    
   #if ball.pos.x > 1.0 or ball.pos.x < -1.0:   
      #ball.pos = vector(0, 0, 0)
      #velocity.x = -velocity.x 

    k = keysdown()  
    if ' ' in k and (ball.pos.x > 0.71 or ball.pos.x < -0.71)  :    
        ball.color = color_list[random.randint(0,5)]
