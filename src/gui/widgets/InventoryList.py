#!/usr/bin/env python

import pygame

from gui.Widget import Widget
from content.object.Object import get_object

class InventoryList(Widget):
    
    def __init__(self, name, object_name, font_name, font_size, font_color=(255, 255, 255), x=0, y=0, size_x=0, size_y=0):
        Widget.__init__(self, name, x, y)
        
        self.object_name = object_name
        obj = get_object(object_name)
        
        if obj is not None and 'Inventory' in obj.components:            
            self.inventory = obj.components['Inventory']
        else:
            self.inventory = None
        
        self.image = None     
        
        self.font_name = font_name 
        self.font_size = font_size
        self.font_color = font_color
        
        self.space_x = 10
        self.space_y = 10
        
        self.size_x = size_x
        self.size_y = size_y
        
        self.active = 0
        self.start = 0
        self.length = 6
        
        self.on_b1_up = None
        self.on_b2_up = None
        
        self.must_update = True
      
    def draw(self, surface):
        if self.must_update:
            self.update_image()
        
        self.image.fill((0,0,0))
        
        if self.inventory is not None:
            y = self.space_y
            for i in range(self.inventory.get_number()):
                if i < self.start:
                    continue
                elif i >= self.start + self.length:
                    break
                
                obj = self.inventory.get_object(i)
                
                if i is self.active:
                    font_color = (255, 0, 0)
                else:
                    font_color = self.font_color
                                
                if 'Description' in obj.components:
                    text = self.font.render(obj.components['Description'].get_name(), True, font_color)
                else:
                    text = self.font.render(obj.id, True, font_color)
                                            
                    
                self.image.blit(text, (self.space_x, y))
                y = y + text.get_height() + self.space_y
        
        surface.blit(self.image, (self.x, self.y))  
    
    def get_active(self):
        if self.inventory is not None:
            return self.inventory.get_object(self.active)
        return None
    
    def on_button_1_up(self, x, y):
        if self.is_inside(x, y):
            relative_y = y - self.y
            
            if self.inventory is not None:
                new_y = self.space_y
                for i in range(self.inventory.get_number()):
                    if i < self.start:
                        continue
                    elif i >= self.start + self.length:
                        break
                    
                    obj = self.inventory.get_object(i)
                
                    if 'Description' in obj.components:
                        text = self.font.render(obj.components['Description'].get_name(), True, self.font_color)
                    else:
                        text = self.font.render(obj.id, True, self.font_color)                                            
                    
                    new_y = new_y + text.get_height() + self.space_y
                    
                    if relative_y < new_y:
                        self.set_active(i)
                        break
            
            return True
        return False
    
    def on_button_2_up(self, x, y):
        return False
    
    def save(self, file):
        pass
    
    def set_active(self, active):
        self.active = active
        
        if self.active < 0:
            self.active = 0
        
        if self.inventory is not None:
            if self.active >= self.inventory.get_number():
                self.active = self.inventory.get_number() - 1
        
        if self.active <= self.start: 
            if self.active - 1 > 0:
                self.start = self.active - 1
            else:
                self.start = 0
        
        if self.active >= self.start + self.length - 1:
            self.start = self.active - 4
            
        
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
    
    return InventoryList(name, object_name, font_name, font_size, (r, g, b), x, y, size_x, size_y)