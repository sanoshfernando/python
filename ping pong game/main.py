from turtle import Turtle,Screen
import dashboard
from  dashboard import Dashboard
from paddles import Paddle
from balls import Ball
import time
screen = Screen()
screen.title("Ping Pong Game")
screen.setup(800,500)
screen.bgcolor("black")
sleep_time = 0.1

game_is_on = True

screen.tracer(0)
dashboard.dashed_line()
dashboard = Dashboard()
dashboard.score_board()
r_paddle = Paddle((370,0))
l_paddle = Paddle((-370,0))
ball = Ball()
screen.update()

while game_is_on:
    screen.listen()
    screen.onkey(r_paddle.go_down, "Down")
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(l_paddle.go_down, "s")
    screen.onkey(l_paddle.go_up, "w")
    time.sleep(sleep_time)
    screen.update()
    ball.check_bounce()
    if ball.distance(r_paddle) < 60 and ball.xcor()>350:
        if ball.heading()==45:
            ball.setheading(ball.heading() + 90)
        else:
            ball.setheading(ball.heading() + 270)
    if ball.distance(l_paddle) < 60 and ball.xcor()<-350:
        if ball.heading() == 225:
            ball.setheading(ball.heading() + 90)
        else:
            ball.setheading(ball.heading() + 270)
    ball.move()
    if ball.xcor()>400:
        dashboard.l_win()
        ball.goto(0,0)
        ball.setheading(135)
        sleep_time*=0.5
    elif ball.xcor()<-400:
        dashboard.r_win()
        ball.goto(0, 0)
        ball.setheading(45)
        sleep_time *= 0.9
    dashboard.score_board()








screen.exitonclick()