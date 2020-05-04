import math

print('''calculations Available:\n Square \n rectangle \n Triangle \n trapezoid \n Circle \n circum_of_circle \n surfarea_of_cube \n tot_surfarea_of_cylinder \n cylinder \n vol_of_cylinder \n accel \n density \n pressure \n kin_energy \n voltage''')

def calc_square(a_side):
    square_area = a_side ** 2
    return square_area

def calc_rectangle(l, b):
    rect_area = l * b
    return rect_area

def calc_triangle(b, h):
    triangle_area = 1/2 * b * h
    return triangle_area

def calc_trapezoid(b1, b2, h):
    trapezoid_area = (1/2 * (b1 + b2) * h)
    return trapezoid_area

def calc_circle(r):
    circle_area = math.pi * r ** 2
    return circle_area

def calc_circum_of_circle(r):
    circle_circum = 2 * math.pi * r ** 2
    return circle_circum

def calc_surfarea_of_cube(a):
    cube_surfarea = 6 * a ** 2
    return cube_surfarea

def calc_cylinder(r, h):
    cylinder_curve_surfarea = 2 * math.pi * r * h
    return cylinder_curve_surfarea

def calc_tot_surfarea_of_cylinder(r, h):
    tot_surfarea_of_cylinder = 2 * math.pi * r (r + h)
    return tot_surfarea_of_cylinder

def calc_vol_of_cylinder(r, h):
    vol_of_cylinder = math.pi * r ** 2 * h
    return vol_of_cylinder

# program to calculate physical quantities

def calc_accel(v, u, t):
    accel = (v - u) / t
    return accel

def calc_density(m, v):
    density = m / v
    return density

def calc_pressure(f, a):
    pressure = f / a
    return pressure

def calc_kin_energy(m, v):
    kinetic_energy = 1/2 * m * v ** 2
    return kinetic_energy

def calc_voltage(i, r):
    voltage = i * r
    return voltage

## function determining which formula to calculate

def area_calc_logic(user_calc):
    if user_calc == "square":
        a_side = int(input("give length of side: "))
        print(calc_square(a_side))
    elif user_calc == "rectangle":
        l = int(input("give length: "))
        b = int(input("give breath: "))
        print(calc_rectangle(l, b))
    elif user_calc == "triangle":
        b = int(input("what is your base: "))
        h = int(input("what is your height: "))
        print(calc_triangle(b, h))
    elif user_calc == "trapezoid":
        b1 = int(input("what is your short base: "))
        b2 = int(input("what is your long base: "))
        h = int(input("what is your height: "))
        print(calc_trapezoid(b1, b2, h))
    elif user_calc == "circle":
        r = int(input("what is the radius of your circle: "))
        print(calc_circle(r))
    elif user_calc == "circum_of_circle":
        r = int(input("what is the radius of your circle: "))
        print(calc_circum_of_circle(r))
    elif user_calc == "surfarea_of_cube":
        a = int(input("what is the length of the sides of the cube"))
        print(calc_surfarea_of_cube(a))
    elif user_calc == "cylinder":
        r = int(input("what is the radius: "))
        h = int(input("what is the height: "))
        print(calc_cylinder(r, h))
    elif user_calc == "tot_surfarea_of_cylinder":
        r = int(input("what is the radius: "))
        h = int(input("what is the height: "))
        print(calc_tot_surfarea_of_cylinder(r, h))
    elif user_calc == "vol_of_cylinder":
        r = int(input("what is the radius: "))
        h = int(input("what is the height: "))
        print(calc_vol_of_cylinder(r, h))
    elif user_calc == "accel":
        v = int(input("what is the veloity: "))
        u = int(input("what is the initial velocity: "))
        t = int(input("what is your time: "))
        print(calc_accel(v, u, t))
    elif user_calc == "density":
        m = int(input("what is your mass? "))
        v = int(input("what is your volume? "))
        print(calc_density(m, v))
    elif user_calc == "pressure":
        f = int(input("what is the force: "))
        a = int(input("what is the area: "))
        print(calc_pressure(f, a))
    elif user_calc == "kin_energy":
        m = int(input("what is your mass? "))
        v = int(input("what is the veloity: "))
        print(calc_kin_energy(m, v))
    elif user_calc == "voltage":
        i = int(input("what is your current: "))
        r = int(input("what is your resistance: "))
        print(calc_voltage(i, r))
area_calc_logic(input("what would you like to calculate? "))


















