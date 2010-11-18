#!/usr/bin/env python

class ArmorTemplate:
    
    def __init__(self, armor=0):
        self.armor = armor
    
    def load(self, file):
        line = file.readline().split()
    
        for i in range(int(line[0])):
            line = file.readline().split()
            
            if line[0] == 'armor':
                self.armor = int(line[1])
    
    def save(self, file):
        pass

class Armor:
    
    def __init__(self, template):
        self.template = template  
    
    def get_armor(self):
        return self.template.armor
    
    def get_type(self):
        return 'Armor'