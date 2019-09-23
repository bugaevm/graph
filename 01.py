from graph import *
from time import sleep

c = canvas()

width = 794
height = 1123

windowSize(width, height)
canvasSize(width, height)

fps = 1 / 60

class UFO:
    def __init__(self, *args):
        self.content = list(args)

class Ray:
    def __init__(self, down, horizon, top):
        self.top = top
        self.horizon = horizon
        self.down = down

class Eye:
    def __init__(self, obj, pos2, size):
        self.obj = obj
        self.pos1 = (xCoord(obj) + 1, yCoord(obj) + 1)
        self.pos2 = pos2
        self.size = size

        self.looking = None

    def move(self, v, i, length):
        # beg = self.pos1 if v == 1 else self.pos2
        # moveObjectTo(self.obj,
        #     beg[0] + int(v * i * (self.pos2[0] - self.pos1[0]) / length + 0.5),
        #     beg[1] + int(v * i * (self.pos2[1] - self.pos1[1]) / length + 0.5),
        # )

        moveObjectBy(self.obj,
            v * (self.pos2[0] - self.pos1[0]) / length,
            v * (self.pos2[1] - self.pos1[1]) / length,
        )

    def take_pos1(self):
        moveObjectTo(self.obj, *self.pos1)

    def take_pos2(self):
        moveObjectTo(self.obj, *self.pos2)

    def look(self, i, length):
        size_x = (1 + i / length * 0.0) * self.size
        size_y = (1 + i / length * 0.9) * self.size

        x = self.pos2[0] - (size_x - self.size) / 2 + 0.5
        y = self.pos2[1] - (size_y - self.size) / 2 + 0.5

        self.not_look()
        self.looking = c.create_oval(
            x, y, x + size_x + 0.5, y + size_y + 0.5, fill='white', outline='white'
        )

    def not_look(self):
        if self.looking is not None:
            deleteObject(self.looking)
            self.looking = None


def html_col(col):
    r, g, b = col

    r = ('0' + hex(r)[2:])[-2:]
    g = ('0' + hex(g)[2:])[-2:]
    b = ('0' + hex(b)[2:])[-2:]

    return '#' + r + g + b

def create_background():
    penColor(horizon_col)
    brushColor(sky_col)
    penSize(1)

    rectangle(-1, -1, width + 1, 576)

    brushColor(ground_col)
    rectangle(-1, 576 + 1, width + 1, height + 1)


def create_sun():
    penColor('#f2f2f2')
    brushColor('#f2f2f2')

    circle((631 + 383) // 2, (127 + 370) // 2, (631 - 383) // 2)

def create_clouds():
    light = list()
    dark = list()

    light.append((502, -22, 502 + 581, -22 + 116))
    light.append((-539, 16, -539 + 1035, 16 + 204))
    light.append((353, 142, 353 + 735, 142 + 125))
    light.append((-423, 245, -423 + 935, 245 + 131))
    light.append((260, 292, 260 + 756, 292 + 130))

    dark.append((137, 83, 137 + 739, 83 + 125))
    dark.append((-301, 214, -301 + 636, 214 + 123))
    dark.append((113, 379, 113 + 748, 379 + 121))

    for cloud in light:
        c.create_oval(*cloud, fill='#666666', outline='#666666')

    for cloud in dark:
        c.create_oval(*cloud, fill='#333333', outline='#333333')


def create_ray():
    global ray

    down = list()
    top = list()

    down.append((20, 734))
    down.append((344, 738))
    down.append((254, 578))
    down.append((93, 578))

    top.append((95, 575))
    top.append((252, 575))
    top.append((214, 508))
    top.append((128, 507))


    penColor(ray_ground_col)
    brushColor(ray_ground_col)
    r_down = polygon(down)

    penColor(ray_sky_col)
    brushColor(ray_sky_col)
    r_top = polygon(top)

    penColor(ray_horizon_col)
    brushColor(ray_horizon_col)
    r_hor = polygon([(94, 576), (253, 576), (254, 577), (93, 577)])

    ray = Ray(r_down, r_hor, r_top)

def create_ufo():
    global ufo

    ufo = UFO()

    windows = list()

    windows.append((24, 443, 24 + 41, 443 + 18))
    windows.append((68, 464, 68 + 41, 464 + 18))
    windows.append((126, 474, 126 + 41, 474 + 18))
    windows.append((190, 476, 190 + 41, 476 + 18))
    windows.append((247, 465, 247 + 41, 465 + 18))
    windows.append((303, 444, 303 + 41, 444 + 18))

    ufo.content.append(c.create_oval(
        6, 393, 6 + 355, 393 + 117, fill='#999999', outline='#999999'
    ))

    ufo.content.append(c.create_oval(
        56, 383, 56 + 256, 383 + 82, fill='#cccccc', outline='#cccccc'
    ))

    for window in windows:
        ufo.content.append(c.create_oval(
            *window, fill='#ffffff', outline='#ffffff'
        ))

def create_dodik():
    global eye1, eye2

    body = (513, 761, 513 + 54, 761 + 117)
    c.create_oval(*body, fill='#dde9af', outline='#dde9af')

    head = list()

    head.append((500, 699))
    head.append((499, 692))
    head.append((499, 686))
    head.append((500, 683))
    head.append((502, 680))
    head.append((507, 676))
    head.append((521, 678))
    head.append((541, 678))
    head.append((569, 675))
    head.append((580, 675))
    head.append((592, 678))
    head.append((605, 684))
    head.append((607, 687))
    head.append((607, 694))
    head.append((605, 704))
    head.append((599, 717))
    head.append((593, 727))
    head.append((584, 739))
    head.append((564, 760))
    head.append((556, 764))
    head.append((546, 764))
    head.append((536, 760))
    head.append((523, 748))
    head.append((518, 740))
    head.append((504, 710))

    head_outline = [(507, 709)] + head + [(496, 692)]


    penColor('#dde9af')
    brushColor('#dde9af')
    polygon(head)

    penColor('#090a06')
    polyline(head_outline)


    ovals = list()

    ovals.append((473, 609, 473 + 27, 609 + 22))
    ovals.append((479, 629, 479 + 21, 629 + 12))
    ovals.append((491, 642, 491 + 17, 642 + 20))
    ovals.append((502, 661, 502 + 10, 661 + 15))

    ovals.append((647, 633, 647 + 23, 633 + 28))
    ovals.append((626, 635, 626 + 15, 635 + 12))
    ovals.append((607, 643, 607 + 15, 643 + 16))
    ovals.append((602, 660, 602 + 8, 660 + 15))
    ovals.append((592, 667, 592 + 18, 667 + 18))

    ovals.append((481, 808, 481 + 11, 808 + 15))
    ovals.append((490, 789, 490 + 23, 789 + 17))
    ovals.append((501, 767, 501 + 28, 767 + 28))

    ovals.append((602, 794, 602 + 32, 794 + 17))
    ovals.append((575, 785, 575 + 27, 785 + 18))
    ovals.append((561, 770, 561 + 29, 770 + 29))

    ovals.append((471, 899, 471 + 28, 899 + 27))
    ovals.append((494, 872, 494 + 23, 872 + 47))
    ovals.append((498, 834, 498 + 29, 834 + 44))

    ovals.append((547, 851, 547 + 29, 851 + 42))
    ovals.append((558, 887, 558 + 21, 887 + 48))
    ovals.append((575, 915, 575 + 28, 915 + 27))


    for oval in ovals:
        c.create_oval(*oval, fill='#dde9af', outline='#dde9af')

    c.create_oval(514, 691, 514 + 35, 691 + 33, fill='black', outline='black')
    c.create_oval(570, 698, 570 + 24, 698 + 26, fill='black', outline='black')

    eye1 = Eye(c.create_oval(
        531, 708, 531 + 9, 708 + 8, fill='white', outline='white'),
        (514 + (35 - 9) // 2, 691 + (33 - 8) // 2), 9.5
    )
    eye2 = Eye(c.create_oval(
        581, 711, 581 + 7, 711 + 7, fill='white', outline='white'),
        (570 + (24 - 7) // 2, 698 + (26 - 7) // 2), 7
    )

def create_apple():
    c.create_oval(620, 751, 620 + 55, 751 + 53, fill='#c83737', outline='#c83737')

    branch = list()

    branch.append((645, 755))
    branch.append((648, 751))
    branch.append((650, 747))
    branch.append((655, 741))
    branch.append((662, 733))

    polyline(branch)

    leave = list()

    leave.append((650, 748))
    leave.append((644, 743))
    leave.append((642, 738))
    leave.append((642, 727))
    leave.append((644, 727))
    leave.append((648, 733))
    leave.append((651, 739))
    leave.append((651, 747))

    brushColor('#88aa00')
    polygon(leave)


def change_col(col1, col2, i, length):
    r1, g1, b1 = col1
    r2, g2, b2 = col2

    r = r1 + int((r2 - r1) * (i + 1) / length + 0.5)
    g = g1 + int((g2 - g1) * (i + 1) / length + 0.5)
    b = b1 + int((b2 - b1) * (i + 1) / length + 0.5)

    return html_col((r, g, b))


sky_col = (0, 34, 43)  #00222b
horizon_col = (46, 69, 68)  #2e4544
ground_col = (34, 43, 0)  #222b00

ray_sky_col = (106, 125, 131)  #6a7d83
ray_horizon_col = (132, 146, 145)  #849291
ray_ground_col = (125, 131, 106)  #7d836a

def turn_off_ray(j):
    changeFillColor(ray.top, change_col(ray_sky_col, sky_col, j, per))
    changePenColor(ray.top, change_col(ray_sky_col, sky_col, j, per))

    changeFillColor(ray.horizon, change_col(ray_horizon_col, horizon_col, j, per))
    changePenColor(ray.horizon, change_col(ray_horizon_col, horizon_col, j, per))

    changeFillColor(ray.down, change_col(ray_ground_col, ground_col, j, per))
    changePenColor(ray.down, change_col(ray_ground_col, ground_col, j, per))

def turn_on_ray(j):
    changeFillColor(ray.top, change_col(sky_col, ray_sky_col, j, per))
    changePenColor(ray.top, change_col(sky_col, ray_sky_col, j, per))

    changeFillColor(ray.horizon, change_col(horizon_col, ray_horizon_col, j, per))
    changePenColor(ray.horizon, change_col(horizon_col, ray_horizon_col, j, per))

    changeFillColor(ray.down, change_col(ground_col, ray_ground_col, j, per))
    changePenColor(ray.down, change_col(ground_col, ray_ground_col, j, per))

i = 0
per = int(1 / fps / 2)

v = 0
a = 0

def animate_ufo(i):
    global v, a

    dy = v + a // 2
    v += a

    for obj in ufo.content:
        moveObjectBy(obj, 0, -dy)

    if i // per == 9:
        a = 3

    elif i == 11 * per:
        v = -v

    elif i == int(13.24 * per):
        a = 0
        v = 0

        for obj in ufo.content:
            deleteObject(obj)

        create_ufo()


def animate_ray(i):
    if i // per == 7:
        j = i - 7 * per
        turn_off_ray(j)

    elif i == 8 * per:
        changeFillColor(ray.top, html_col(sky_col))
        changePenColor(ray.top, html_col(sky_col))

        changeFillColor(ray.horizon, html_col(horizon_col))
        changePenColor(ray.horizon, html_col(horizon_col))

        changeFillColor(ray.down, html_col(ground_col))
        changePenColor(ray.down, html_col(ground_col))

    elif i // per == 14:
        turn_on_ray(i - 14 * per)


def animate_eyes(i):
    if 10 * per <= i < 10.5 * per:
        j = int(i - 10 * per)
        eye1.move(1, j, per // 2)
        eye2.move(1, j, per // 2)

    if 11 * per == i:
        eye1.take_pos2()
        eye2.take_pos2()

    if 11 * per <= i < 11.125 * per:
        eye1.look(i - 11 * per, per / 8)
        eye2.look(i - 11 * per, per / 8)


    if 29 * per == 2 * i:
        eye1.not_look()
        eye2.not_look()

    if 14.5 * per <= i:
        j = int(i - 14.5 * per)

        eye1.move(-1, j, per // 2)
        eye2.move(-1, j, per // 2)
    if i == 0:
        eye1.take_pos1()
        eye2.take_pos1()


def animation():
    global i

    i += 1
    i %= 15 * per

    animate_ufo(i)
    animate_ray(i)
    animate_eyes(i)



create_background()
create_sun()
create_clouds()
create_ray()
create_ufo()
create_dodik()
create_apple()

onTimer(animation, int(fps * 1000))


run()
