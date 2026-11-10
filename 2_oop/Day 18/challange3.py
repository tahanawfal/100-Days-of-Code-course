from random import choice
import turtle as t


tim = t.Turtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

########### Challenge 3 - Draw Shapes ########
for shape in range(3,11):
    tim.color(choice(colours))
    for shapes_sides in range(shape):
        angle = 360 / shape
        tim.setheading(360 - (angle * shapes_sides))
        tim.forward(100)