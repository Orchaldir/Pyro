#!/usr/bin/env python

import pygame

from gui.Widget import Widget
from content.object.Object import get_object

class EquipmentSlots(Widget):
    
    def __init__(self, name, object_name, font_name, font_size, font_color=(255, 255, 255), x=0, y=0, size_x=0, size_y=0):
        Widget.__init__(self, name, x, y)
        
        self.object_name = object_name
        obj = get_object(object_name)
        
        if obj is not None and 'EquipmentSlots' in obj.components:            
            self.character = obj.components['EquipmentSlots']
        else:
            self.character = None
        
        self.image = None     
        
        self.font_name = font_name 
        self.font_size = font_size
        self.font_color = font_color
        
        self.space_x = 10
        self.space_y = 10
        
        self.size_x = size_x
        self.size_y = size_y
        
        self.on_b1_up = None
        self.on_b2_up = None
        
        self.must_update = True
      
    def draw(self, surface):
        if self.must_update:
            self.update_image()
        
        self.image.fill((0,0,0))
        
        if self.character is not None:
            y = self.space_y
            for slot in self.character.template.slots:
                if self.character.slots[slot] is not None:
                    obj = self.character.slots[slot]
                    if 'Description' in obj.components:
                        text = self.font.render(slot +  ' - ' + obj.components['Description'].get_name(), True, self.font_color)
                    else:
                        text = self.font.render(slot +  ' - ' + obj.id, True, self.font_color)
                else:
                    text = self.font.render(slot, True, self.font_color)                                            
                    
                self.image.blit(text, (self.space_x, y))
                y = y + text.get_height() + self.space_y
        
        surface.blit(self.image, (self.x, self.y)) 
    
    def on_button_1_up(self, x, y):
        return False
    
    def on_button_2_up(self, x, y):
        return False
    
    def save(self, file):
        pass
        
    def update_image(self):
        self.must_update = False
        
        self.font = pygame.font.SysFont(self.font_name, self.font_size)
        self.image = pygame.Surface((self.size_x, self.size_y))
        self.image.fill((0,0,0))

def load(name, file):
    line = file.readline().split()
    object_name = line[0]
    
    line = file.readline().split()    
    x = int(line[0])
    y = int(line[1])       
    
    line = file.readline().split()    
    size_x = int(line[0])
    size_y = int(line[1]) 
    
    line = file.readline().split()    
    font_name = line[0]
    font_size = int(line[1])
    
    line = file.readline().split()    
    r = int(line[0])
    g = int(line[1]) 
    b = int(line[2])
    
    return EquipmentSlots(name, object_name, font_name, font_size, (r, g, b), x, y, size_x, size_y)