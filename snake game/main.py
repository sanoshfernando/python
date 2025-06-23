from turtle import Screen
import time
from food import Food
from snake import Snake
from scoreboard import Scoreboard
screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()
#detect food collision
    if snake.head.distance(food)<18:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
#detect wall collision
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on=False
        scoreboard.game_over()
#detect tail collision
    for segment in snake.segments[1::]:
        if snake.head.distance(segment)<5:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()
