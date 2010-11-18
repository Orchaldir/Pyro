#!/usr/bin/env python

import content.object.Template

class HealthTemplate:
    
    def __init__(self, health=0, corpse=None):
        self.health = health
        self.corpse = corpse
    
    def load(self, file):
        line = file.readline().split()
    
        for i in range(int(line[0])):
            line = file.readline().split()
            
            if line[0] == 'health':
                self.health = int(line[1])
            elif line[0] == 'corpse':
                self.corpse = line[1]
    
    def save(self, file):
        pass

class Health:
    
    def __init__(self, template):
        self.health = template.health
        self.template = template      
        self.object = None
    
    def damage(self, amount):
        if amount <= 0 or self.is_death():
            return 0
        
        if self.health > amount:
            self.health = self.health - amount       
            return amount                 
        else:
            health = self.health
            self.health = 0
            self.on_death()
            
            return health  
    
    def get_health(self):
        return self.health
    
    def get_max_health(self):
        return self.template.health
    
    def get_type(self):
        return 'Health'
    
    def heal(self, amount):
        if amount <= 0 or self.is_death():
            return 0
        
        delta = self.template.health - self.health
        
        if delta > amount:
            self.health = self.health + amount
            return amount
        else:
            self.health = self.template.health
            return delta
    
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False
    
    def is_death(self):
        if self.health > 0:
            return False
        else:
            return True
    
    def on_death(self):
        if self.object is None or self.is_alive():
            return False
        
        if self.object.body is not None and self.object.body.map is not None:
            map = self.object.body.map
            x = self.object.body.x
            y = self.object.body.y                                                           
            self.object.remove()
            
            if self.template.corpse is not None:
                corpse = content.object.Template.create_object(self.template.corpse)
                map.add_object(corpse, x, y)
        else:
            self.object.remove()
        
        return True