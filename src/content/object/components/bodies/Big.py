#!/usr/bin/env python

from content.object.components.Body import Body
import resource.Tile

class Big(Body):
    
    def __init__(self, size=2, tile=None):
        Body.__init__(self)
        
        self.size = size
        self.tile = resource.Tile.get(tile)
        
        self.occupied_cells = []        
    
    def add_to_map(self, map, x, y):
        occupied_cells = []
        
        for cx in range(0, self.size):
            for cy in range(0, self.size):            
                cell = map.get_cell(x + cx, y + cy)
                
                if cell is None:
                    return False
                elif cell.celltype.solid:
                    return False
                
                for obj in cell.objects:
                    if obj is not self.object and 'Character' in obj.components:
                        return False
                
                occupied_cells.append(cell)
        
        if self.object is not None:
            for cell in self.occupied_cells:
                cell.objects.remove(self.object)
        
        self.occupied_cells = occupied_cells
        
        if self.object is not None:
            for cell in self.occupied_cells:
                cell.objects.append(self.object)
        
        self.x = x
        self.y = y
        self.map = map
        
        return True
        
    def draw(self, surface):
        self.tile.draw(surface, self.x, self.y, self.size)
    
    def get_move_targets(self, direction):
        if self.is_moveable():
            cells = []
            
            x = self.x + Big.direction_x[direction]
            y = self.y + Big.direction_y[direction]
            
            for cx in range(0, self.size):
                for cy in range(0, self.size):            
                    cell = self.map.get_cell(x + cx, y + cy)
                
                    if cell is not None and cell not in self.occupied_cells:
                        cells.append(cell)
            
            return cells
        
        return []
    
    def get_occupied_cells(self):
        return self.occupied_cells
    
    def get_size(self):
        return self.size
    
    def remove_from_map(self):
        for cell in self.occupied_cells:
            cell.objects.remove(self.object)
        
        self.occupied_cells = []
        
        self.x = None
        self.y = None
        self.map = None