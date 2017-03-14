# solar_credit.py
# CS 1 Lab Assignment 2.
# Original solution by Raunak Bhojwani, October 2014

from cs1lib import *
from system_credit import System
from body_credit import Body

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

TIME_SCALE = 9000000         # how many real seconds for each second of simulation (change this to speed up or slow down the system)
PIXELS_PER_METER = 6 / 1e10  # distance scale for the simulation

FRAME_RATE = 30             # frames per second
TIMESTEP = 1.0 / FRAME_RATE # time between drawing each frame

G = 6.67384 * 10**(-11)      # Gravitational Constant

#All the relevant masses
SUN_MASS = 1.98892e30
EARTH_MASS = 5.9736e24
MERCURY_MASS = 3.3022e23
VENUS_MASS = 4.8685e24
MOON_MASS = 7.3477e22
MARS_MASS = 6.4185e23

# All the relevant distances
EARTH_MOON = 3.84403e8
SUN_MERCURY = 5.791e10
SUN_VENUS = 1.082e11
SUN_EARTH = 1.496e11
SUN_MARS = 2.2794e11


def main():
    
    sun = Body(SUN_MASS, 0, 0, 0, 0, 24, "SUN.png")                                   # Sun
    earth = Body(EARTH_MASS, SUN_EARTH, 0, 0, 29790, 8, "EARTH FINAL.gif")            # Earth
    mercury = Body(MERCURY_MASS, SUN_MERCURY, 0, 0, 47890, 3, "MERCURY FINAL.jpeg")   # Mercury
    venus = Body(VENUS_MASS, SUN_VENUS, 0, 0, 35040, 5.75, "VENUS FINAL.gif")         # Venus
    mars = Body(MARS_MASS, SUN_MARS, 0, 0, 24140, 5, "MARS FINAL.gif")                # Mars
    
    solar = System([sun, mercury, venus, earth, mars])                                 #Create the solar system
    
    set_clear_color(0, 0, 0)    # black background
    enable_smoothing()

    while not window_closed(): 
        clear()
        background_img = load_image("ss122.gif")                        # Space background image
        draw_image(background_img, 0, 0)
        
       
        
        # Draw the system in its current state.
        solar.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)
    
        # Update the system for its next state.
        solar.update(TIMESTEP * TIME_SCALE)
    
        # Draw the frame and take a brief nap.
        request_redraw()
        sleep(TIMESTEP)

start_graphics(main, "Solar System Simulation", WINDOW_WIDTH, WINDOW_HEIGHT)
