import turtle
from turtle import Turtle,Screen
import random

is_race_on = False
screen=Screen()
screen.setup(width=500,height=400)
#racer_number = screen.textinput("Racer number","Choose a number")
user_bet= screen.textinput("Make your bet", "which turtle will win the race? Enter a color")
colors= ["red","orange","yellow","green","blue","purple"]
all_turtles=[]
i=30
for _ in range(0 , len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[_])
    new_turtle.goto(-230, -100 + i)
    i=i+30
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color==user_bet:
                print(f"You win!. The {winning_color} wins!")
            else:
                print(f"You lose! The {winning_color} wins!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)






screen.exitonclick()