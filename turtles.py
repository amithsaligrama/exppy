import turtle
x = 0
screen = turtle.Screen()
screen.bgcolor("black")
quokka = turtle.Turtle()
quokka.shape("turtle")
quokka.color("black")
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
dingo = turtle.Turtle()
dingo.shape("turtle")
dingo.color("black")
quokka.forward(300)
dingo.backward(300)
penguin.forward(600)
hen.backward(600)
dog.left(90)
dog.forward(300)
cat.right(90)
cat.forward(300)
while 0==0:
    dingo.right(128)
    dingo.forward(100)
    x += 1
    if x % 9 == 2:
        dingo.color("green")
    elif x % 9 == 3:
        dingo.color("blue")
    elif x % 9 == 4:
        dingo.color("brown")
    elif x % 9 == 5:
        dingo.color("yellow")
    elif x % 9 == 0:
        dingo.color("pink")
    elif x % 9 == 1:
        dingo.color("white")
    elif x % 9 == 7:
        dingo.color("orange")
    elif x % 9 == 6:
        dingo.color("cyan")
    else:
        dingo.color("red")
    quokka.left(64)
    quokka.forward(100)
    if x % 9 == 1:
        quokka.color("green")
    elif x % 9 == 2:
        quokka.color("blue")
    elif x % 9 == 3:
        quokka.color("brown")
    elif x % 9 == 4:
        quokka.color("yellow")
    elif x % 9 == 5:
        quokka.color("pink")
    elif x % 9 == 6:
        quokka.color("white")
    elif x % 9 == 7:
        quokka.color("orange")
    elif x % 9 == 0:
        quokka.color("cyan")
    else:
        quokka.color("red")
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
