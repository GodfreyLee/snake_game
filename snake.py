import turtle

distance = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.tims = []
        self.create_snake()
        self.head = self.tims[0]
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self,position):
        tim = turtle.Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.tims.append(tim)

    def reset(self):
        for num in self.tims:
            num.goto(1000,1000)
        self.tims.clear()
        self.create_snake()
        self.head = self.tims[0]
    def extend(self):
        self.add_segment(self.tims[-1].position())

    def move(self):
        for tim_num in range(len(self.tims) - 1, 0, -1):
            new_x = self.tims[tim_num - 1].xcor()
            new_y = self.tims[tim_num - 1].ycor()
            self.tims[tim_num].goto(new_x, new_y)
        self.head.forward(distance)

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


