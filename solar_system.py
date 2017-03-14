# solar_system.py
# CS 1 Lab Assignment 3.
# Original solution by Raunak Bhojwani, October 2014

from cs1lib import *
from system import System
from body import Body

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

TIME_SCALE = 9000000         # how many real seconds for each second of simulation
PIXELS_PER_METER = 6 / 1e10  # distance scale for the simulation

FRAME_RATE = 30             # frames per second
TIMESTEP = 1.0 / FRAME_RATE # time between drawing each frame

G = 6.67384 * 10**(-11)      # Gravitational Constant

SUN_MASS = 1.98892e30
EARTH_MASS = 5.9736e24
MERCURY_MASS = 3.3022e23
VENUS_MASS = 4.8685e24
MOON_MASS = 7.3477e22
MARS_MASS = 6.4185e23

EARTH_MOON = 3.84403e8
SUN_MERCURY = 5.791e10
SUN_VENUS = 1.082e11
SUN_EARTH = 1.496e11
SUN_MARS = 2.2794e11


def main():
    
    sun = Body(SUN_MASS, 0, 0, 0, 0, 24, 1, 1, 0,)                           # Yellow Sun
    earth = Body(EARTH_MASS, SUN_EARTH, 0, 0, 30000, 8, 0, 0, 1)            # blue earth
    mercury = Body(MERCURY_MASS, SUN_MERCURY, 0, 0, 48000, 3, 1, 0.6, 0)    # Brown Mercury
    venus = Body(VENUS_MASS, SUN_VENUS, 0, 0, 35000, 6.5, 0, 1, 0)          # Green Venus
    mars = Body(MARS_MASS, SUN_MARS, 0, 0, 24000, 5, 1, 0, 0)               # Red Mars
    
    solar = System([sun, mercury, venus, earth, mars])                      # Create the system
    
    set_clear_color(0, 0, 0)    # black background
    enable_smoothing()

    while not window_closed(): 
        clear()
        
        
        # Draw the system in its current state.
        solar.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)
    
        # Update the system for its next state.
        solar.update(TIMESTEP * TIME_SCALE)
    
        # Draw the frame and take a brief nap.
        request_redraw()
        sleep(TIMESTEP)

start_graphics(main, "Solar System Simulation", WINDOW_WIDTH, WINDOW_HEIGHT)
