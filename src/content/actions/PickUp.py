#!/usr/bin/env python

class PickUp:
    
    def __init__(self, obj):
        self.obj = obj
    
    def execute(self):
        objects = self.obj.body.get_objects()
    
        if len(objects) > 0:
            inventory = self.obj.components['Inventory']
            
            for obj in objects:
                inventory.add(obj)
                
        return True

def can_pick_up(obj):
    if obj is None and obj.body is None:
        return False
    
    if 'Inventory' not in obj.components: 
        return False
    
    if 'Controller' not in obj.components: 
        return False
            
    obj.components['Controller'].action = PickUp(obj)
        
    return True