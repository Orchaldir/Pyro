#!/usr/bin/env python

from content.effects.Heal import Heal

class ConsumableTemplate:
    
    def __init__(self):
        self.effects = []
    
    def load(self, file):
        line = file.readline().split()
    
        for i in range(int(line[0])):
            line = file.readline().split()
            
            if line[0] == 'heal':
                self.effects.append(Heal(int(line[1])))
    
    def save(self, file):
        pass

class Consumable:
    
    def __init__(self, template):
        self.template = template      
    
    def get_type(self):
        return 'Consumable'
    
    def use(self, obj):
        for effect in self.template.effects:
            effect.apply(obj)
        
        