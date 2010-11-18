#!/usr/bin/env python

class Player:
    
    def __init__(self):
        self.used = False  
        self.action = None
    
    def get_type(self):
        return 'Controller'
    
    def update(self, obj):
        if self.action is not None:
            if self.action.execute():
                self.action = None
                return True
            self.action = None
            
        return False