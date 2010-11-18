#!/usr/bin/env python

from content.object.Object import Object, add_object
from content.object.components.Armor import Armor, ArmorTemplate
from content.object.components.Character import Character, CharacterTemplate
from content.object.components.Consumable import Consumable, ConsumableTemplate
from content.object.components.Description import Description, DescriptionTemplate
from content.object.components.Equipment import Equipment, EquipmentTemplate
from content.object.components.EquipmentSlots import EquipmentSlots, EquipmentSlotsTemplate
from content.object.components.Health import Health, HealthTemplate
from content.object.components.Inventory import Inventory
from content.object.components.Perception import Perception, PerceptionTemplate
from content.object.components.Weapon import Weapon, WeaponTemplate
from content.object.components.bodies.Big import Big
from content.object.components.bodies.Simple import Simple
from content.object.components.bodies.Snake import  Snake
from content.object.components.controllers.Ai import Ai
import utility.Path

templates = {}
path = None

class Template:
    
    def __init__(self, name):
        self.name = name
        self.components = {}
        self.count = 0
    
    def create_object(self):
        obj = Object(self.name + '_' + str(self.count))
    
        for type, data in self.components.iteritems():
            if type == 'Ai':
                obj.add_component(Ai(data['behavior']))
            elif type == 'Armor':
                obj.add_component(Armor(data))
            elif type == 'Body':
                if data['type'] == 'Big':
                    obj.add_component(Big(int(data['size']), data['tile']))
                elif data['type'] == 'Simple':
                    obj.add_component(Simple(data['tile']))
                elif data['type'] == 'Snake':
                    obj.add_component(Snake(int(data['length']), data['head_tile'], data['tail_tile']))
            elif type == 'Character':
                obj.add_component(Character(data))
            elif type == 'Consumable':
                obj.add_component(Consumable(data))
            elif type == 'Description':
                obj.add_component(Description(data))
            elif type == 'Equipment':
                obj.add_component(Equipment(data))
            elif type == 'EquipmentSlots':
                obj.add_component(EquipmentSlots(data))
            elif type == 'Health':
                obj.add_component(Health(data))
            elif type == 'Perception':
                obj.add_component(Perception(data))
            elif type == 'Weapon':
                obj.add_component(Weapon(data))
            elif type == 'Inventory':
                obj.add_component(Inventory())
            else:
                return  
    
        self.count = self.count + 1
        add_object(obj)
        return obj
    
    def load(self, file):
        line = file.readline().split()
    
        for i in range(int(line[0])):
            line = file.readline().split()
            component = None
            
            if line[0] == 'Armor':
                component = ArmorTemplate()
            elif line[0] == 'Character':
                component = CharacterTemplate()
            elif line[0] == 'Consumable':
                component = ConsumableTemplate()
            elif line[0] == 'Description':
                component = DescriptionTemplate()
            elif line[0] == 'Equipment':
                component = EquipmentTemplate()
            elif line[0] == 'EquipmentSlots':
                component = EquipmentSlotsTemplate()
            elif line[0] == 'Health':
                component = HealthTemplate()
            elif line[0] == 'Perception':
                component = PerceptionTemplate()
            elif line[0] == 'Weapon':
                component = WeaponTemplate()                
            else:            
                dict = {}
                self.components[line[0]] = dict
            
            
                for c in range(int(line[1])):
                    line = file.readline()
                    parts = line.split()
                    if parts[0] == 's':
                        dict[parts[1]] = line[7 + len(parts[1]):-1]
                    else:
                        dict[parts[0]] = parts[1]
                
                continue
            
            if component is not None:
                component.load(file)
                self.components[line[0]] = component
    
    def save(self, file):
        file.write('%s\n' % (self.name))
        file.write('  %d\n' % (len(self.components)))
        
        for type, dict in self.components.iteritems():
            file.write('  %s %d\n' % (type, len(dict)))
            for key, value in dict.iteritems():
                file.write('    %s %s\n' % (key, value))

def init_templates(filename=None):
    global templates, path
    
    templates = {}
    path = utility.Path.get('templates') 
    
    if filename is not None:
        load_templates(filename)

def create_object(template_name):
    template = get_template(template_name)
    
    if template is None:
        return None
    
    return template.create_object()       

def get_template(name):
    global templates
    
    if name in templates:
        return templates[name]
    else:
        return None

def load_templates(filename):
    global templates, path
        
    file = open(utility.Path.join(path, filename), 'r')
    
    line = file.readline().split()
    
    length = int(line[0])
    
    for i in range(length):
        line = file.readline().split()
        template = Template(line[0])
        template.load(file)
        templates[line[0]] = template
    
    file.close()
    
def save_templates(filename):
    global templates, path
        
    file = open(utility.Path.join(path, filename), 'w')
    
    file.write('%d\n' % (len(templates)))
    
    for template in templates.values():
        template.save(file)
    
    file.close()