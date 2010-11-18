#!/usr/bin/env python

class EquipmentTemplate:
    
    def __init__(self, slots=[]):
        self.slots = []
    
    def load(self, file):
        line = file.readline().split()
    
        for i in range(int(line[0])):
            line = file.readline().split()
            
            self.slots.append(line[0])
    
    def save(self, file):
        pass

class Equipment:
    
    def __init__(self, template):
        self.template = template
    
    def get_type(self):
        return 'Equipment'