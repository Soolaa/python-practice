import turtle
from turtle import Turtle, Screen
import random
# import colorgram
# colors = colorgram.extract('images.jpg', 10)
# print(colors)
#
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     print(new_color)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

color_list = [(29, 35, 44), (44, 106, 153), (237, 231, 73), (40, 32, 23), (63, 179, 225), (26, 37, 31), (42, 28, 37), (214, 151, 100), (247, 240, 206), (16, 176, 223)]
screen = Screen()
screen.colormode(255)
tim = Turtle()
tim.hideturtle()
tim.penup()
tim.shape("turtle")
tim.pensize(2)
tim.speed("fastest")
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

number_of_dot = 100


for dot_count in range(1, number_of_dot+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen.exitonclick()


