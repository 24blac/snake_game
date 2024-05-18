from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Noga Game")
screen.tracer(0)


s = Snake()
food = Food()
score = Scoreboard()


screen.listen()
screen.onkey(s.up, "Up")
screen.onkey(s.down, "Down")
screen.onkey(s.left, "Left")
screen.onkey(s.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    s.move()

    #detect collision with food

    if s.head.distance(food) < 13:
        food.refresh()
        s.extend()
        score.inc_score()

    #detect collision with wall
    if s.head.xcor() > 280 or s.head.xcor() < -280 or s.head.ycor() > 280 or s.head.ycor() < -280:
        score.reset()
        s.reset()
    

    #detecting collision with tail
    for sq in s.snake[1:]:
        if s.head.distance(sq) < 10:
            score.reset()
            s.reset()
        


screen.exitonclick()