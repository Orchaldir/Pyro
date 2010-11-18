#!/usr/bin/env python

class Damage:
    
    def __init__(self, amount):
        self.amount = amount
    
    def apply(self, obj):
        character = obj.get_component('Character')
        
        if 'Health' in obj.components:
            health = obj.components['Health']
            
            if character is None:
                health.damage(self.amount)
            else:
                health.damage(character.reduce_damage(self.amount))
                    
            return True                
        
        return False