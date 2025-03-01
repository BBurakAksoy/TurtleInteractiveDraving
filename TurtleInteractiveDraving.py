import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("black")
drawing_board.title("Python Turtle")

turtle_instance = turtle.Turtle()
turtle_instance.color("white")

def turtle_forward():
    turtle_instance.forward(50)

def rotate_angle_right():
    turtle_instance.right(20)

def rotate_angle_left():
    turtle_instance.left(20)

def clear_screen():
    turtle_instance.clear()

def turtle_return_home():
    turtle_pen_up()
    turtle_instance.home()
    turtle_pen_down()

def turtle_pen_up():
    turtle_instance.penup()

def turtle_pen_down():
    turtle_instance.pendown()

drawing_board.listen()
drawing_board.onkey(fun=turtle_forward,key="space")
drawing_board.onkey(fun=rotate_angle_left,key="Up")
drawing_board.onkey(fun=rotate_angle_right,key="Down")
drawing_board.onkey(fun=clear_screen,key="c")
drawing_board.onkey(fun=turtle_return_home,key="b")
drawing_board.onkey(fun=turtle_pen_up,key="z")
drawing_board.onkey(fun=turtle_pen_down,key="x")

turtle.done()
