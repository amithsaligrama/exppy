import turtle
x = 0
screen = turtle.Screen()
screen.bgcolor("black")
white = turtle.Turtle()
white.shape("turtle")
white.color("black")
penguin = turtle.Turtle()
penguin.shape("turtle")
penguin.color("black")
hen = turtle.Turtle()
hen.shape("turtle")
hen.color("black")
dog = turtle.Turtle()
dog.shape("turtle")
dog.color("black")
cat = turtle.Turtle()
cat.shape("turtle")
cat.color("black")
henry = turtle.Turtle()
henry.shape("turtle")
henry.color("black")
white.forward(300)
henry.backward(300)
penguin.forward(600)
hen.backward(600)
dog.left(90)
dog.forward(300)
cat.right(90)
cat.forward(300)
while 0==0:
    henry.right(128)
    henry.forward(100)
    x += 1
    if x % 9 == 2:
        henry.color("green")
    elif x % 9 == 3:
        henry.color("blue")
    elif x % 9 == 4:
        henry.color("brown")
    elif x % 9 == 5:
        henry.color("yellow")
    elif x % 9 == 0:
        henry.color("pink")
    elif x % 9 == 1:
        henry.color("white")
    elif x % 9 == 7:
        henry.color("orange")
    elif x % 9 == 6:
        henry.color("cyan")
    else:
        henry.color("red")
    white.left(64)
    white.forward(100)
    if x % 9 == 1:
        white.color("green")
    elif x % 9 == 2:
        white.color("blue")
    elif x % 9 == 3:
        white.color("brown")
    elif x % 9 == 4:
        white.color("yellow")
    elif x % 9 == 5:
        white.color("pink")
    elif x % 9 == 6:
        white.color("white")
    elif x % 9 == 7:
        white.color("orange")
    elif x % 9 == 0:
        white.color("cyan")
    else:
        white.color("red")
    penguin.left(75)
    penguin.forward(100)
    if x % 9 == 2:
        penguin.color("green")
    elif x % 9 == 3:
        penguin.color("blue")
    elif x % 9 == 4:
        penguin.color("brown")
    elif x % 9 == 5:
        penguin.color("yellow")
    elif x % 9 == 6:
        penguin.color("pink")
    elif x % 9 == 7:
        penguin.color("white")
    elif x % 9 == 8:
        penguin.color("orange")
    elif x % 9 == 0:
        penguin.color("cyan")
    else:
        penguin.color("red")
    hen.left(37.5)
    hen.forward(50)
    if x % 9 == 3:
        hen.color("green")
    elif x % 9 == 4:
        hen.color("blue")
    elif x % 9 == 5:
        hen.color("brown")
    elif x % 9 == 6:
        hen.color("yellow")
    elif x % 9 == 7:
        hen.color("pink")
    elif x % 9 == 8:
        hen.color("white")
    elif x % 9 == 2:
        hen.color("orange")
    elif x % 9 == 1:
        hen.color("cyan")
    else:
        hen.color("red")
    dog.right(104)
    dog.forward(100)
    if x % 9 == 4:
        dog.color("green")
    elif x % 9 == 5:
        dog.color("blue")
    elif x % 9 == 6:
        dog.color("brown")
    elif x % 9 == 7:
        dog.color("yellow")
    elif x % 9 == 8:
        dog.color("pink")
    elif x % 9 == 0:
        dog.color("white")
    elif x % 9 == 1:
        dog.color("orange")
    elif x % 9 == 2:
        dog.color("cyan")
    else:
        dog.color("red")
    cat.right(152)
    cat.forward(100)
    if x % 9 == 5:
        cat.color("green")
    elif x % 9 == 6:
        cat.color("blue")
    elif x % 9 == 7:
        cat.color("brown")
    elif x % 9 == 8:
        cat.color("yellow")
    elif x % 9 == 0:
        cat.color("pink")
    elif x % 9 == 1:
        cat.color("white")
    elif x % 9 == 2:
        cat.color("orange")
    elif x % 9 == 3:
        cat.color("cyan")
    else:
        cat.color("red")
