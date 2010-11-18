#!/usr/bin/env python

from content.effects.Damage import Damage

class Attack:
    
    def __init__(self, attacker, target):
        self.attacker = attacker
        self.target = target
    
    def execute(self):
        character = self.attacker.components['Character']
        damage = Damage(character.get_weapon_damage())
        damage.apply(self.target)
        self.attacker.body.map.add_sound(self.attacker.body.x, self.attacker.body.y, character.get_weapon_loudness(), [self.attacker, self.target])
        return True

def can_attack(attacker, target):
    if attacker is None or attacker.body is None:
        return False
    
    if target is None or target.body is None or attacker is target:
        return False
    
    if 'Character' not in attacker.components: 
        return False
    
    if 'Controller' not in attacker.components: 
        return False
    
    if 'Character' not in target.components: 
        return False
        
    character = attacker.components['Character']
            
    if attacker.body.get_distance_to_body(target.body) <= character.get_weapon_range():
        attacker.components['Controller'].action = Attack(attacker, target)
        return True
        
    return False