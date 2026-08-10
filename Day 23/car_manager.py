from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
RIGHT_EDGE = 280
UPPER_Y_LIMIT = 250
LOWER_Y_LIMIT = -250
LEFT_EDGE = -310

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.create_car()
        self.car_speed = MOVE_INCREMENT

    def create_car(self):
        if random.randint(1,6) == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(RIGHT_EDGE, random.randint(LOWER_Y_LIMIT, UPPER_Y_LIMIT))
            self.all_cars.append(new_car)

    def move(self):
        self.create_car()
        for car in self.all_cars:
            car.backward(self.car_speed)
            if car.xcor() < LEFT_EDGE:
                self.all_cars.remove(car)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
