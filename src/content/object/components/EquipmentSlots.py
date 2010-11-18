#!/usr/bin/env python

class EquipmentSlotsTemplate:
    
    def __init__(self, slots=[]):
        self.slots = slots
    
    def load(self, file):
        self.slots = []
        
        line = file.readline().split()
    
        for i in range(int(line[0])):
            line = file.readline().split()
            
            self.slots.append(line[0])
    
    def save(self, file):
        pass

class EquipmentSlots:
    
    def __init__(self, template):
        self.template = template
        self.armors = []
        self.weapon = None
        self.slots = {}     
        
        for slot in self.template.slots:
            self.slots[slot] = None   
    
    def equip(self, obj):
        equipment = obj.components['Equipment']
        
        for slot in equipment.template.slots:
            if slot not in self.template.slots:
                return False
        
        for slot in equipment.template.slots:
            if self.slots[slot] is not None:
                self.unequip(self.slots[slot])
            self.slots[slot] = obj
        
        if 'Weapon' in obj.components:
            self.weapon = obj.components['Weapon']
        
        if 'Armor' in obj.components:
            self.armors.append(obj.components['Armor'])
    
    def get_armor(self):
        total_armor = 0
        
        for armor in self.armors:
            total_armor = total_armor + armor.get_armor()
        
        return total_armor
    
    def get_weapon_damage(self):
        if self.weapon is not None:
            return self.weapon.get_damage()
        else:
            return 0
    
    def get_weapon_range(self):
        if self.weapon is not None:
            return self.weapon.get_range()
        else:
            return 0
    
    def get_weapon_loudness(self):
        if self.weapon is not None:
            return self.weapon.get_loudness()
        else:
            return 0.0
    
    def get_type(self):
        return 'EquipmentSlots'
    
    def has_weapon(self):
        return self.weapon is not None
    
    def is_equipped(self, obj):
        for slot in self.template.slots:
            if self.slots[slot] is obj:
                return True
        
        return False
    
    def unequip(self, obj):
        for slot in self.template.slots:
            if self.slots[slot] is obj:
                self.slots[slot] = None
        
        if 'Weapon' in obj.components:
            if self.weapon is obj.components['Weapon']:
                self.weapon = None
        
        if 'Armor' in obj.components:
            self.armors.remove(obj.components['Armor'])