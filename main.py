# import libs
import numpy
import matplotlib.pyplot as plotter

# create parameters

theta_start = numpy.radians(float(input("Enter the theta you wish to start from in degrees: ")))
length = float(input('Enter the length of the string in meters: '))
grav_acc = 9.81
time_stop = (2 * numpy.pi * numpy.sqrt(length / grav_acc))
time_step = 0.01

# create lists to store the theta, time and w values

angles = [theta_start]
time_list = numpy.arange(0, time_stop, time_step)
w_list = [0]

# fill list with values using Euler's method

with open(f'database_for_{theta_start}_rad.txt', 'x') as data_base:
    for t in time_list[1:]:
        curr_theta = angles[-1]
        curr_w = w_list[-1]
        new_w = curr_w - (grav_acc * numpy.sin(curr_theta) * time_step) / length
        new_theta = curr_theta + new_w * time_step
        angles.append(new_theta)
        w_list.append(new_w)
        data_base.write(f'\n({t}, {curr_theta})')

# make the graph

plotter.plot(time_list, angles, marker='*')
plotter.title("Simple Pendulum ODE Simulation")
plotter.xlabel("Time (s)")
plotter.ylabel("Angle (radians)")
plotter.show()
