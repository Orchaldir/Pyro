#!/usr/bin/env python

import pygame

from gui.Widget import Widget
import resource.Tile
from content.world.Map import get_map

class MapViewer(Widget):
    
    def __init__(self, name, map_name, x=0, y=0, size_x=0, size_y=0, tile_size_x=10, tile_size_y=10):
        Widget.__init__(self, name, x, y)
        
        self.image = None
        self.map = None
        self.map_name = map_name        
        
        self.size_x = size_x
        self.size_y = size_y
        
        self.tile_size_x = tile_size_x
        self.tile_size_y = tile_size_y
        
        self.on_b1_up = None
        self.on_b2_up = None
        
        self.must_update = True
      
    def draw(self, surface):
        if self.must_update:
            self.update_image()
        
        self.image.fill((255,255,255))
        
        if self.map is not None:                   
            resource.Tile.set_size(self.tile_size_x, self.tile_size_y)
            resource.Tile.actual_surface = self.image
            self.map.draw()   
            
            #self.image = pygame.transform.flip(self.image, False, True) 
        
            surface.blit(self.image, (self.x, self.y))  
    
    def on_button_1_up(self, x, y):
        if self.is_inside(x, y):
            if self.on_b1_up is not None:
                cell = self.map.get_cell((x - self.x) / self.tile_size_x, (y - self.y) / self.tile_size_y)
                if cell is not None:
                    self.on_b1_up(cell)
            return True
        return False
    
    def on_button_2_up(self, x, y):
        if self.is_inside(x, y):
            if self.on_b2_up is not None:
                cell = self.map.get_cell((x - self.x) / self.tile_size_x, (y - self.y) / self.tile_size_y)
                if cell is not None:
                    self.on_b2_up(cell)
            return True
        return False
    
    def save(self, file):
        file.write('MapViewer %s\n' % (self.name))
        file.write('  %s\n' % (self.map_name))
        file.write('  %d %d\n' % (self.x, self.y))   
        file.write('  %d %d\n' % (self.size_x, self.size_y))   
        file.write('  %d %d\n' % (self.tile_size_x, self.tile_size_y)) 
        
    def update_image(self):
        self.must_update = False
        
        self.map = get_map(self.map_name)
        self.image = pygame.Surface((self.size_x, self.size_y))

def load(name, file):
    line = file.readline().split()
    map_name = line[0]
    
    line = file.readline().split()    
    x = int(line[0])
    y = int(line[1])       
    
    line = file.readline().split()    
    size_x = int(line[0])
    size_y = int(line[1]) 
    
    line = file.readline().split()    
    tile_size_x = int(line[0])
    tile_size_y = int(line[1]) 
    
    return MapViewer(name, map_name, x, y, size_x, size_y, tile_size_x, tile_size_y)