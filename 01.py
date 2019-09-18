from graph import *

c = canvas()

width = 794
height = 1123

windowSize(width, height)
canvasSize(width, height)

def create_background():
    penColor('#2e4544')
    brushColor('#00222b')
    penSize(1)

    rectangle(-1, -1, width + 1, 576)

    brushColor('#222b00')
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


    penColor('#7d836a')
    brushColor('#7d836a')
    polygon(down)

    penColor('#6a7d83')
    brushColor('#6a7d83')
    polygon(top)

    penColor('#849291')
    line(94, 576, 253, 576)
    line(93, 577, 254, 577)

def create_ufo():
    windows = list()

    windows.append((24, 443, 24 + 41, 443 + 18))
    windows.append((68, 464, 68 + 41, 464 + 18))
    windows.append((126, 474, 126 + 41, 474 + 18))
    windows.append((190, 476, 190 + 41, 476 + 18))
    windows.append((247, 465, 247 + 41, 465 + 18))
    windows.append((303, 444, 303 + 41, 444 + 18))

    c.create_oval(6, 393, 6 + 355, 393 + 117, fill='#999999', outline='#999999')
    c.create_oval(56, 383, 56 + 256, 383 + 82, fill='#cccccc', outline='#cccccc')

    for window in windows:
        c.create_oval(*window, fill='#ffffff', outline='#ffffff')

def create_dodik():
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

    c.create_oval(531, 708, 531 + 9, 708 + 8, fill='white', outline='white')
    c.create_oval(581, 711, 581 + 7, 711 + 7, fill='white', outline='white')

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









create_background()
create_sun()
create_clouds()
create_ray()
create_ufo()
create_dodik()
create_apple()


run()
