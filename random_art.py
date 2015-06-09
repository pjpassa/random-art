import random
from math import pi, sin, cos, tan, atan, acos, asin
import perlin_noise as pn
# Your job is to create better version of create_expression and
# run_expression to create random art.
# Your expression should have a __str__() function defined for it.


def create_expression():
    """This function takes no arguments and returns an expression that
    generates a number between -1.0 and 1.0, given x and y coordinates."""
    angles1 = generate_angles()
    angles2 = generate_angles()
    angles3 = generate_angles()
    grid_size1 = generate_grid_size()
    grid_size2 = generate_grid_size()
    grid_size3 = generate_grid_size()
    offset_1x = random.random()
    offset_1y = random.random()
    offset_2x = random.random()
    offset_2y = random.random()
    trig1 = trig_func()
    trig2 = trig_func()
    trig3 = trig_func()
    func1 = f()
    func2 = f()
    func3 = f()
    func4 = f()
    func5 = f()

    def expr(x, y):
        value1 = trig2(pi * func5(trig1(func1(pn.perlinNoise((x + offset_1x,
                       y + offset_1y), grid_size1, angles1)) * pi)))
        value2 = trig2(func3(pn.perlinNoise((x + offset_2x, y + offset_2y),
                       grid_size2, angles2) * pi))
        value3 = trig1(func2(pn.perlinNoise((x + offset_2y, y + offset_1x),
                       grid_size3, angles3)) * pi)
        return trig2(pi * func4(trig3(pi * func2(value1 *
                     value2 - (value3 + x * y)))))
    return expr


def run_expression(expr, x, y):
    """This function takes an expression created by create_expression and
    an x and y value. It runs the expression, passing the x and y values
    to it and returns a value between -1.0 and 1.0."""
    return expr(x, y)


def generate_angles():
    return (random.uniform(0, 2*pi), random.uniform(0, 2*pi),
            random.uniform(0, 2*pi), random.uniform(0, 2*pi))


def generate_grid_size():
    return random.randint(2500, 4500)


def trig_func():
        return random.choice([sin, cos])


def f():
        return random.choice([sin, tan, cos, atan])
