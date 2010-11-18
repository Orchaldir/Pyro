#!/usr/bin/env python

from ai.behavior.Behavior import get_behavior

class Ai:
    
    def __init__(self, behavior):
        self.behavior = get_behavior(behavior) 
        self.action = None
    
    def get_type(self):
        return 'Controller'
    
    def update(self, obj):
        if self.action is None and self.behavior is not None:
            self.behavior.execute(obj)
            
        if self.action is not None:
            self.action.execute()
            self.action = None
        
        return True
        