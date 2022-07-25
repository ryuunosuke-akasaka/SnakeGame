import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
TIME = 0.1
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Move Snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(TIME)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        # if scoreboard.score > 25 and TIME > 0.04:
        #     TIME = TIME - 0.01
        # if scoreboard.score % 5 == 0 and TIME > 0.99:
        #     TIME = TIME - 0.1

    # Detect collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()

screen.exitonclick()
