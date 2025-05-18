from turtle import Turtle, Screen
import random

screen = Screen()
new_turtles = Turtle()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

race_is_on = True

screen.setup(width=500, height=400)
y_positions = [-100, -50, 0, 50, 100, 150]

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?")
all_turtles = []

for i in range(0,6):
    new_turtles = Turtle(shape="turtle")
    new_turtles.color(colors[i])
    new_turtles.penup()
    new_turtles.goto(x=-200, y=y_positions[i])
    new_turtles.speed(random.randrange(1,100,1))
    all_turtles.append(new_turtles)

while race_is_on:
    for turtle in all_turtles:
        turtle.forward(random.randint(0,10))
        if turtle.xcor() > 230 :
            race_is_on = False
            if turtle.pencolor() == user_bet:
                print(f"You've won! The {user_bet} turtle wins!")
            else:
                print(f"You've lost! The {turtle.pencolor()} turtle wins!")

screen.exitonclick()