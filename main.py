# Case-study #1
# Developers: Fedotova M., Ogorodnikova M., Shepeleva U.
#
import turtle as t

t.speed(500)
screen = t.Screen()
screen.setup(width=600, height=600)


def trn_ssc(x, y, a, b, color):
    '''
    Function, drawing isosceles triangle.
    :param x: x coordinate
    :param y: y coordinate
    :param a: base side isosceles triangle
    :param b: lateral side isosceles triangle
    :param color: colour isosceles triangle
    '''
    t.up()
    t.goto(x, y)
    t.down()
    t.fillcolor(color)
    t.begin_fill()
    t.left(90)
    t.forward(a)
    t.right(135)
    t.forward(b)
    t.right(90)
    t.forward(b)
    t.end_fill()


def rctn(x, y, a, b, color):
    '''
    Function, drawing rectangle.
    :param x: x coordinate
    :param y: y coordinate
    :param a: one side of the rectangle
    :param b: second side of the rectangle
    :param color: colour rectangle
    '''
    t.up()
    t.goto(x, y)
    t.down()
    t.fillcolor(color)
    t.begin_fill()
    t.left(90)
    for i in range(2):
        t.forward(a)
        t.right(90)
        t.forward(b)
        t.right(90)
    t.right(90)
    t.end_fill()


def sqr(x, y, a, color):
    '''
    Function, drawing square.
    :param x: x coordinate
    :param y: y coordinate
    :param a: side of the square
    :param color: colour square
    '''
    t.up()
    t.goto(x, y)
    t.down()
    t.fillcolor(color)
    t.begin_fill()
    for i in range(4):
      t.forward(a)
      t.right(90)
    t.end_fill()


def trpz(x, y, a, b, c, d, color):
    '''
    Function, drawing trapezoid.
    :param x: x coordinate
    :param y: y coordinate
    :param a: lateral side of the trapezoid
    :param b: first base of the trapezoid
    :param c: trapezoid height
    :param d: second base of the trapezoid
    :param color: colour trapezoid
    '''
    t.up()
    t.goto(x, y)
    t.down()
    t.fillcolor(color)
    t.begin_fill()
    t.left(45)
    t.forward(a)
    t.right(45)
    t.forward(b)
    t.right(90)
    t.forward(c)
    t.right(90)
    t.forward(d)
    t.right(180)
    t.end_fill()


def prl_1(x, y, a, color):
    '''
    Function, drawing parallelogram.
    :param x: x coordinate
    :param y: y coordinate
    :param a: one side of the parallelogram
    :param color: colour parallelogram
    '''
    t.up()
    t.goto(x, y)
    t.down()
    t.fillcolor(color)
    t.begin_fill()
    for i in range(2):
        t.forward(a)
        t.right(60)
        t.forward(a)
        t.right(120)
    t.end_fill()


def prl_2(x, y, a, b, color):
    '''
    Function, drawing parallelogram.
    :param x: x coordinate
    :param y: y coordinate
    :param a: one side of the parallelogram
    :param b: second side of the parallelogram
    :param color: colour parallelogram
    '''
    t.up()
    t.goto(x, y)
    t.down()
    t.fillcolor(color)
    t.begin_fill()
    for i in range(2):
        t.forward(a)
        t.right(23)
        t.forward(b)
        t.right(157)
    t.seth(0)
    t.end_fill()


def prl_3(x, y, a, b, color):
    '''
    Function, drawing parallelogram.
    :param x: x coordinate
    :param y: y coordinate
    :param a: one side of the parallelogram
    :param b: second side of the parallelogram
    :param color: colour parallelogram
    '''
    t.up()
    t.goto(x, y)
    t.down()
    t.fillcolor(color)
    t.begin_fill()
    for i in range(2):
        t.forward(a)
        t.right(45)
        t.forward(b)
        t.right(135)
    t.end_fill()


def main():
    '''
    Main function.
    :return: None
    '''
    # cat
    t.left(90)
    t.pencolor('sandybrown')
    trn_ssc(-207, 130, 62, 45, 'sandybrown')
    t.left(135)
    t.pencolor('chocolate')
    trn_ssc(-145, 130, 62, 45, 'chocolate')
    t.right(90)
    t.pencolor('darksalmon')
    rctn(-233, 220, 82, 44,'darksalmon')
    t.pencolor('lightcoral')
    sqr(-233, 220, 44,'lightcoral')
    t.right(45)
    t.pencolor('indianred')
    trn_ssc(-233, 282, 61, 43, 'indianred')
    t.right(45)
    t.pencolor('firebrick')
    trn_ssc(-295, 220, 61, 43, 'firebrick')
    t.left(90)
    t.pencolor('coral3')
    trpz(-233, 220, 55, 88, 39, 120,'coral3')
    t.right(0)
    t.pencolor('coral4')
    prl_1(-135, 229, 42,'coral4')
    t.seth(0)
    # swan
    t.left(135)
    t.pencolor('darkblue')
    trn_ssc(95, 175, 62, 45, 'darkblue')
    t.left(225)
    t.pencolor('blueviolet')
    trn_ssc(52, 220, 62, 45, 'blueviolet')
    t.pencolor('slateblue')
    rctn(50, 131,90,45, 'slateblue')
    t.right(45)
    t.pencolor('darkorchid')
    trn_ssc(-41, 131, 63, 45, 'darkorchid')
    t.left(113)
    t.pencolor('orchid')
    prl_2(-85, 177, 52, 45, 'orchid')
    t.left(225)
    t.pencolor('pink')
    trn_ssc(-39, 245, 67, 48, 'pink')
    t.left(225)
    t.pencolor('deeppink3')
    trn_ssc(-87, 199, 67, 48, 'deeppink3')
    t.seth(0)
    # scalaria
    t.pencolor('dodgerblue')
    rctn(158, 150, 80, 38, 'dodgerblue')
    t.right(315)
    t.pencolor('mediumblue')
    trn_ssc(196, 112, 53, 37, 'mediumblue')
    t.right(90)
    t.pencolor('cornflowerblue')
    trn_ssc(158, 230, 80, 57, 'cornflowerblue')
    t.right(90)
    t.pencolor('blue4')
    trn_ssc(159, 231, 53, 37, 'blue4')
    t.right(180)
    t.pencolor('skyblue')
    trn_ssc(197, 150, 80, 57, 'skyblue')
    t.right(180)
    t.pencolor('royalblue')
    trn_ssc(275, 152, 53, 37, 'royalblue')
    t.left(45)
    t.pencolor('blue3')
    trn_ssc(238, 190, 53, 37, 'blue3')
    t.seth(0)
    # square
    t.pencolor('pink')
    trn_ssc(-250, -50, 90, 64, 'pink')
    t.left(45)
    t.pencolor('blue')
    trn_ssc(-250, 41, 91, 64, 'blue')
    t.left(45)
    t.pencolor('green')
    trn_ssc(-159, 40, 44, 31, 'green')
    t.left(45)
    t.pencolor('purple')
    trn_ssc(-180, -27, 46, 32, 'purple')
    t.left(90)
    t.pencolor('red')
    sqr(-203, -4, 31, 'red')
    t.right(90)
    t.pencolor('orange')
    trn_ssc(-204, -50, 63, 47, 'orange')
    t.right(315)
    t.pencolor('yellow')
    prl_3(-184, -28, 34, 42, 'yellow')
    t.seth(0)
    #helicopter
    t.right(180)
    t.pencolor('orange')
    trn_ssc(30, 40, 100, 70.7, 'orange')
    t.right(45)
    t.pencolor('purple')
    trn_ssc(30, -60, 100, 70.7, 'purple')
    t.right(135)
    t.pencolor('yellow')
    trn_ssc(30, 40, 70, 49.5, 'yellow')
    t.left(90)
    t.pencolor('green')
    prl_3(30, 40, 40, 40, 'green')
    t.left(45)
    t.pencolor('blue')
    trn_ssc(5, -36, 50, 36, 'blue')
    t.right(45)
    t.pencolor('pink')
    trn_ssc(-70, -10, 50, 36, 'pink')
    t.pencolor('red')
    sqr(-73, -11, 35, 'red')
    t.seth(0)
    # gold_fish
    t.pencolor('red')
    trn_ssc(250, -50, 80, 56.57, 'red')
    t.left(180)
    t.pencolor('pink')
    trn_ssc(250, -0, 100, 70.7, 'pink')
    t.right(315)
    t.pencolor('blue')
    trn_ssc(179.3, -70.7, 100, 70.7, 'blue')
    t.left(45)
    t.pencolor('purple')
    sqr(250, -00, 50, 'purple')
    t.right(90)
    t.pencolor('yellow')
    trn_ssc(179.29, -0, 50, 35.36, 'yellow')
    t.right(45)
    t.pencolor('green')
    trn_ssc(108.65, -34.82, 50, 35.36, 'green')
    t.pencolor('orange')
    prl_3(179.29, -0.1, 35.36, 45, 'orange')
    t.seth(0)
    # rocket
    t.left(90)
    t.pencolor('pink')
    trn_ssc(-184, -142, 30, 21, 'pink')
    t.left(90)
    t.pencolor('yellow')
    trn_ssc(-188, -168, 35, 26, 'yellow')
    t.left(90)
    t.pencolor('orange')
    trn_ssc(-212, -190, 45, 34, 'orange')
    t.right(45)
    t.pencolor('red')
    trn_ssc(-187, -172, 45, 34, 'red')
    t.right(180)
    t.pencolor('blue')
    sqr(-194, -211, 25, 'blue')
    t.left(135)
    t.pencolor('purple')
    trn_ssc(-229, -246, 34, 24, 'purple')
    t.right(90)
    t.pencolor('green')
    prl_3(-168, -236, 25, 30, 'green')
    # human
    t.left(90)
    t.pencolor('blue')
    sqr(25, -132, 28, 'blue')
    t.right(90)
    t.pencolor('pink')
    trn_ssc(42, -155, 51, 37, 'pink')
    t.left(45)
    t.pencolor('yellow')
    trn_ssc(5, -190, 51, 37, 'yellow')
    t.right(45)
    t.pencolor('red')
    trn_ssc(10, -194, 45, 35, 'red')
    t.right(45)
    t.pencolor('purple')
    trn_ssc(55, -251, 35, 25, 'purple')
    t.pencolor('green')
    prl_3(6, -193, 20, 29, 'green')
    t.left(45)
    t.pencolor('orange')
    trn_ssc(-35, -255, 35, 25, 'orange')
    # rooster
    t.right(90)
    t.pencolor('pink')
    trn_ssc(252, -162, 35, 24, 'pink')
    t.left(45)
    t.pencolor('orange')
    sqr(217, -163, 20, 'orange')
    t.left(135)
    t.pencolor('yellow')
    trn_ssc(233, -187, 65, 48, 'yellow')
    t.left(45)
    t.pencolor('red')
    trn_ssc(182, -209, 65, 50, 'red')
    t.left(180)
    t.pencolor('blue')
    trn_ssc(184, -163, 48, 36, 'blue')
    t.right(180)
    t.pencolor('green')
    prl_3(157, -220, 30, 35, 'green')
    t.left(45)
    t.pencolor('purple')
    trn_ssc(214, -210, 30, 23, 'purple')
    t.seth(0)
    t.done()


if __name__ == '__main__':
    main()
