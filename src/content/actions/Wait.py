#!/usr/bin/env python

class Wait:
    
    def __init__(self):
        pass
    
    def execute(self):
        return True

def can_wait(obj):
    if 'Controller' in obj.components:
        obj.components['Controller'].action = Wait()        
        return True
    
    return False