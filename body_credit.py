#Author: Raunak Bhojwani
#Created: October 21 2014
#Lab2: Gravity
#Class definition for a body

from cs1lib import *

class Body:
    def __init__(self, mass, x, y, vx, vy, pixel_radius, img):      #Initialize all parameters
        self.mass = mass
        
        self.x = x
        self.y = y
        
        self.vx = vx
        self.vy = vy
        
        self.pixel_radius = pixel_radius
        
        self.img = load_image(img)
   
        
        
        
    def update_position(self, timestep):                                # Position depends on x and y velocity
        self.x = self.x + (self.vx * timestep)
        self.y = self.y + (self.vy * timestep)
        
    def update_velocity(self, ax, ay, timestep):                        # Velocity depends on x and y acceleration
        self.vx = self.vx + (ax * timestep)
        self.vy = self.vy + (ay * timestep)
        
    def draw(self, cx, cy, pixels_per_meter):
        draw_image(self.img, cx + (pixels_per_meter * self.x) - self.pixel_radius, cy + (self.y * pixels_per_meter)-self.pixel_radius)
       
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_mass(self):
        return self.mass      
        