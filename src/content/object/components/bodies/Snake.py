#!/usr/bin/env python

from content.object.components.Body import Body
import resource.Tile

class Snake(Body):
    
    def __init__(self, length, head_tile=None, tail_tile=None):
        Body.__init__(self)
        
        self.length = length
        self.head_tile = resource.Tile.get(head_tile)
        self.tail_tile = resource.Tile.get(tail_tile)
        
        self.occupied_cells = {}
    
    def add_to_map(self, map, x, y):
        cell = map.get_cell(x, y)
        
        if cell is None:
            return False
        elif cell.cell_type.solid:
            return False
        
        self.occupied_cells = {}
        self.occupied_cells[0] = cell
        
        self.x = x
        self.y = y
        self.map = map
        
        return True
    
    def draw(self, surface):
        for i, cell in self.occupied_cells.items():
            if i is 0:
                self.head_tile.draw(surface, cell.x, cell.y)
            else:
                self.tail_tile.draw(surface, cell.x, cell.y)
    
    def get_occupied_cells(self):
        return self.occupied_cells.values()
    
    def move(self, x, y):
        cell = self.map.get_cell(self.x + x, self.y + y)
        
        if cell is None:
            return False
        elif cell.cell_type.solid:
            return False
        
        old = self.occupied_cells[0]
        for i in range(1, self.length):
            if i in self.occupied_cells:
                self.occupied_cells[i], old = old, self.occupied_cells[i]
            elif old is not None:
                self.occupied_cells[i] = old
                old = None
            
        self.occupied_cells[0] = cell
        
        self.x = self.x + x
        self.y = self.y + y
        
        return True