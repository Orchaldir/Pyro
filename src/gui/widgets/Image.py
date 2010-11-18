#!/usr/bin/env python

import pygame

from gui.Widget import Widget
import resource.Image

class Image(Widget):
    
    def __init__(self, name, image_name, x=0, y=0, size_x=0, size_y=0):
        Widget.__init__(self, name, x, y)
        
        self.raw_image = resource.Image.load(image_name)
        
        self.size_x = size_x
        self.size_y = size_y
        
        self.must_update = True
    
    def save(self, file):
        file.write('Image %s\n' % (self.name))
        
    def update_image(self):
        self.must_update = False
        
        self.image = pygame.transform.scale(self.raw_image, (self.size_x, self.size_y))