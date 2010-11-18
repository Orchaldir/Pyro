#!/usr/bin/env python

import pygame.font

from gui.Widget import Widget

class Label(Widget):
    
    def __init__(self, name, text, font_name, font_size, font_color=(255, 255, 255), x=0, y=0, update=None):
        Widget.__init__(self, name, x, y)
        
        self.text = text
        
        self.font_name = font_name 
        self.font_size = font_size
        self.font_color = font_color
        
        self.update = update
        
        self.update_image()
    
    def draw(self, surface):
        if self.must_update:
            self.update_image()
            
        surface.blit(self.image, (self.x, self.y))
    
    def save(self, file):
        file.write('Label %s\n' % (self.name))
        file.write('  %d %d\n' % (self.x, self.y))   
        file.write('  %s\n' % (self.text))   
        file.write('  %s %d\n' % (self.font_name, self.font_size))  
        file.write('  %d %d %d\n' % (self.font_color))  
    
    def set_text(self, text):
        self.text = text
        self.must_update = True
    
    def update_image(self):
        self.must_update = False
            
        self.font = pygame.font.SysFont(self.font_name, self.font_size)
        self.image = self.font.render(self.text, True, self.font_color)
        
        self.size_x = self.image.get_width()
        self.size_y = self.image.get_height()


def load(name, file):
    line = file.readline().split()    
    x = int(line[0])
    y = int(line[1])
    
    line = file.readline()
    text = line[2:]
    
    line = file.readline().split()    
    font_name = line[0]
    font_size = int(line[1])
    
    line = file.readline().split()    
    r = int(line[0])
    g = int(line[1]) 
    b = int(line[2])
    
    return Label(name, text, font_name, font_size, (r, g, b), x, y)