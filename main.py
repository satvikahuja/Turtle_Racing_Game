from turtle import Turtle, Screen
import random


is_race_on=False
screen = Screen()

screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet",prompt="Which turtle wins the race? Enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]
p_positions = [-70,-40,-10,20,50,80]

all_turtles = []

for i in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=p_positions[i])
    all_turtles.append(new_turtle)
    

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on = False
            winning_color=turtle.pencolor()
            if winning_color== user_bet:
                print(f"You have won! The {winning_color} turtle is the winner!")
                Screen().bgcolor(f"{winning_color}")
            else:
                print(f"You have Lost! The {winning_color} turtle is the winner! ")
                Screen().bgcolor(f"{winning_color}")


        rand_diatance = random.randint(1,10)
        turtle.forward(rand_diatance)


screen.exitonclick()