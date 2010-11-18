#!/usr/bin/env python

class CharacterTemplate:
    
    def __init__(self, alignment='Neutral', armor=0, weapon_damage=0, weapon_range=0, weapon_loudness=0.0):
        self.alignment = alignment
        self.armor = armor
        self.weapon_damage = weapon_damage
        self.weapon_range = weapon_range
        self.weapon_loudness = weapon_loudness        
    
    def load(self, file):
        line = file.readline().split()
    
        for i in range(int(line[0])):
            line = file.readline().split()
            
            if line[0] == 'alignment':
                self.alignment = line[1]      
            elif line[0] == 'armor':
                self.armor = int(line[1])      
            elif line[0] == 'weapon_damage':
                self.weapon_damage = int(line[1])
            elif line[0] == 'weapon_range':
                self.weapon_range = int(line[1])
            elif line[0] == 'weapon_loudness':
                self.weapon_loudness = float(line[1])
    
    def save(self, file):
        pass

class Character:
    
    def __init__(self, template):
        self.template = template 
        self.object = None
    
    def get_armor(self):
        total_armor = self.template.armor
        
        if 'EquipmentSlots' in self.object.components:
            total_armor = total_armor + self.object.components['EquipmentSlots'].get_armor()
        
        return total_armor
    
    def get_weapon_damage(self):
        if 'EquipmentSlots' in self.object.components:
            slots = self.object.components['EquipmentSlots']
            
            if slots.has_weapon():
                return slots.get_weapon_damage()
        
        return self.template.weapon_damage
    
    def get_weapon_range(self):
        if 'EquipmentSlots' in self.object.components:
            slots = self.object.components['EquipmentSlots']
            
            if slots.has_weapon():
                return slots.get_weapon_range()
            
        return self.template.weapon_range
    
    def get_weapon_loudness(self):
        if 'EquipmentSlots' in self.object.components:
            slots = self.object.components['EquipmentSlots']
            
            if slots.has_weapon():
                return slots.get_weapon_loudness()
        
        return self.template.weapon_loudness
    
    def get_type(self):
        return 'Character'
    
    def is_enemy(self, character):
        return not self.template.alignment == character.template.alignment
    
    def reduce_damage(self, damage):
        return max(damage - self.get_armor(), 0)