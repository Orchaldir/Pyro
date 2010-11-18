#!/usr/bin/env python

class WeaponTemplate:
    
    def __init__(self, damage=0, range=0, loudness=0.0):
        self.damage = damage
        self.range = range
        self.loudness = loudness
    
    def load(self, file):
        line = file.readline().split()
    
        for i in range(int(line[0])):
            line = file.readline().split()
            
            if line[0] == 'damage':
                self.damage = int(line[1])
            elif line[0] == 'range':
                self.range = int(line[1])  
            elif line[0] == 'loudness':
                self.loudness = float(line[1])                      
    
    def save(self, file):
        pass

class Weapon:
    
    def __init__(self, template):
        self.template = template  
    
    def get_damage(self):
        return self.template.damage
    
    def get_loudness(self):
        return self.template.loudness
    
    def get_range(self):
        return self.template.range
    
    def get_type(self):
        return 'Weapon'