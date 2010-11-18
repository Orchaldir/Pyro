#!/usr/bin/env python

from gui.Widget import Widget
import resource.Tile

class TileViewer(Widget):
    
    def __init__(self, name, tile, x=0, y=0, size_x=0, size_y=0):
        Widget.__init__(self, name, x, y)
        
        if tile is None:
            self.tile = resource.Tile.default
        else:
            self.tile = tile
        
        self.size_x = size_x
        self.size_y = size_y
        
        self.must_update = True
    
    def save(self, file):
        file.write('TileViewer %s\n' % (self.name))
        file.write('  %d %d\n' % (self.x, self.y))   
        file.write('  %d %d\n' % (self.size_x, self.size_y))
        
    def update_image(self):
        self.must_update = False
        
        self.image = self.tile.get_image(self.size_x, self.size_y)

def load(name, file):
    line = file.readline().split()    
    x = int(line[0])
    y = int(line[1])       
    
    line = file.readline().split()    
    size_x = int(line[0])
    size_y = int(line[1]) 
    
    return TileViewer(name, None, x, y, size_x, size_y)