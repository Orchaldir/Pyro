#!/usr/bin/env python

class Heal:
    
    def __init__(self, amount):
        self.amount = amount
    
    def apply(self, obj):
        if 'Health' in obj.components:
            health = obj.components['Health']
            health.heal(self.amount)
            
            return True                
        
        return False