#Author: Raunak Bhojwani
#Created: October 21 2014
#Lab2 Gravity
#Class definition for a system of bodies


from cs1lib import *
from body import Body
from math import *

G = 6.67384 * 10**(-11)

class System:
    def __init__(self, body_list):
        self.body_list = body_list                  # Initialize list
            
    def distance(self, x1, y1, x2, y2):             #Figure out the distance between two bodies
        dx = x2 - x1
        dy = y2 - y1
        return (sqrt(dx * dx + dy * dy), dx, dy)
    
    def compute_acceleration(self, n):              # Computing the acceleration of one body influenced by all the other bodies in the system
        ax = 0
        ay = 0
        for body in self.body_list:
            if body != self.body_list[n]:
                (d, dx, dy) = self.distance(self.body_list[n].get_x(), self.body_list[n].get_y(), body.get_x(), body.get_y())
                a = (G * body.get_mass())/(d*d)
                ax = ax + a * (dx/d)
                ay = ay + a * (dy/d)
    
        return (ax, ay)
            
    def update(self, timestep):                 # Update function for the system
         
        for n in range(len(self.body_list)):
            
            (ax, ay) = self.compute_acceleration(n)
            self.body_list[n].update_velocity(ax, ay, timestep)
            self.body_list[n].update_position(timestep)    
            
    def draw(self, cx, cy, pixels_per_meter):
        for body in self.body_list:                 # For each body, draw the body with the parameters provided 
            body.draw(cx, cy, pixels_per_meter)