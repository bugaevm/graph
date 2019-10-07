from graph import *
from tkinter import *
import random as r

c = canvas()

width = 794
height = 1123

windowSize(width, height)
canvasSize(width, height)

cloud_number = None
cloud_list = []  # list of clouds characteristics


def fog_generation():  # func generate cloud_number fog clouds
    global cloud_number, cloud_list
    for i in range(cloud_number):

        # generation of cloud characteristics
        cloud_speed = r.randint(0, 14)
        cloud_length = r.randint(50, 200)
        cloud_x = r.randint(100, 500)
        cloud_y = r.randint(50, 450)

        # cloud color generation
        red = r.randint(200, 255)
        green = r.randint(200, 255)
        blue = r.randint(200, 255)

        # cloud drawing
        penColor(red, green, blue)
        penSize(15)
        cloud = line(cloud_x, cloud_y, cloud_x + cloud_length, cloud_y)
        cloud_list.append([cloud, cloud_speed, cloud_length])


def fog_animation():  # func animate fog
    for i in range(cloud_number):
        pass


def fog():  # main func
    global cloud_number
    cloud_number = r.randint(8, 15)
    fog_generation()
    fog_animation()
    return 0


fog()
run()
