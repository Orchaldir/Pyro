#!/usr/bin/env python

class Inventory:
    
    def __init__(self):
        self.objects = []
    
    def add(self, obj):
        if obj not in self.objects:
            obj.remove()
                    
            self.objects.append(obj)
            obj.owner = self
    
    def get_number(self):
        return len(self.objects)
    
    def get_object(self, index):
        if index >= 0 and index < len(self.objects):
            return self.objects[index]
        return None
    
    def get_type(self):
        return 'Inventory'
    
    def remove_object(self, obj):
        if obj in self.objects:
            self.objects.remove(obj)