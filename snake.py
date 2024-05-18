from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)] 
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class Snake:
    def __init__(self):
        self.snake = []
        self.make_snake()
        self.head = self.snake[0]

    def make_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_square(pos)
            

    def add_square(self, pos):
        square = Turtle(shape="square")
        square.color("green")
        square.penup()
        square.goto(pos)
        self.snake.append(square)

    
    def extend(self):
        self.add_square(self.snake[-1].position())

    def reset(self):
        for sq in self.snake:
            sq.goto(1000, 1000)
        self.snake.clear()
        self.make_snake()
        self.head = self.snake[0]


    def move(self):
        for sq_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[sq_num - 1].xcor()
            new_y = self.snake[sq_num - 1].ycor()
            self.snake[sq_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        