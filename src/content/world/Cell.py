#!/usr/bin/env python

import math

from content.world.CellType import get_celltype
from resource.Tile import create_color_tile

class Cell:
    
    water_tiles = None
    
    def __init__(self, x, y, celltype_name=None):
        self.x = x
        self.y = y
        self.celltype = get_celltype(celltype_name)
        self.objects = []
        self.neighbors = None
    
    def draw(self):
        self.celltype.tile.draw(self.x, self.y)    
    
    def get_neighbors(self):
        if self.neighbors is None:
            self.neighbors = []
        
            cell = map.get_cell(self.x + 1, self.y)
        
            if cell is not None:
                self.neighbors.append(cell)
        
            cell = map.get_cell(self.x - 1, self.y)
        
            if cell is not None:
                self.neighbors.append(cell)
        
            cell = map.get_cell(self.x, self.y + 1)
        
            if cell is not None:
                self.neighbors.append(cell)
        
            cell = map.get_cell(self.x, self.y - 1)
        
            if cell is not None:
                self.neighbors.append(cell)
        else:
            return self.neighbors
    
    def get_distance(self, x, y):
        return int(math.fabs(x - self.x) + math.fabs(y - self.y))
    
    def is_walkable(self, obj):
        if self.celltype.solid:
            return False
        
        if 'Character' in obj.components:
            for o in self.objects:
                if 'Character' in o.components and o is not obj:
                    return False
        
        return True
    
