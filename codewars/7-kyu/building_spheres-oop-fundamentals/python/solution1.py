from math import pi 

class Sphere:
    def __init__(self, radius, mass):  
        self._r = radius  
        self._m = mass  
    
    def get_radius(self): 
        return self._r
    
    def get_mass(self):
        return self._m
    
    def get_volume(self):
        x = ((4 * pi * (self._r**3)) / 3)
        return round(x, 5)
    
    def get_surface_area(self):
        x = 4 * pi * (self._r**2)
        return round(x, 5)
    
    def get_density(self):
        return round(self.get_mass() / self.get_volume(), 5)
