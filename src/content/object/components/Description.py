#!/usr/bin/env python

class DescriptionTemplate:
    
    def __init__(self):
        self.Name = 'Name'
    
    def load(self, file):
        line = file.readline().split()
    
        for i in range(int(line[0])):
            line = file.readline()
            parts = line.split()
            
            if parts[0] == 'name':
                self.name = line[9:-1]
    
    def save(self, file):
        pass

class Description:
    
    def __init__(self, template):
        self.template = template
    
    def get_name(self):
        return self.template.name
    
    def get_type(self):
        return 'Description'