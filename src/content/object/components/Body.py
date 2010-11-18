#!/usr/bin/env python

class Body:
    
    direction_x = [0, 1, 0, -1]
    direction_y = [1, 0, -1, 0]
    
    def __init__(self):
        self.object = None
        self.x = None
        self.y = None
        self.map = None
    
    def add_to_map(self, map, x, y):
        cell = map.get_cell(x, y)
        
        if cell is None or not cell.is_walkable(self.object):
            return False
        
        if self.object is not None:
            occupied_cell = map.get_cell(self.x, self.y)
            if occupied_cell is not None:
                occupied_cell.objects.remove(self.object)        
        
            cell.objects.append(self.object)
        
        self.x = x
        self.y = y
        self.map = map
        
        return True
    
    def can_move(self, direction):
        if self.is_moveable():
            cell = self.map.get_cell(self.x + Body.direction_x[direction], self.y + Body.direction_y[direction])
        
            if cell is not None and cell.is_walkable(self.object):
                return True
        
        return False
        
    def draw(self):
        pass
    
    def get_distance(self, x, y):
        cells = self.get_occupied_cells()      
        min = None
        
        for cell in cells:
            distance = cell.get_distance(x, y)
                
            if min is None or distance < min:
                min = distance
        
        return min
    
    def get_distance_to_body(self, body):
        cells_a = self.get_occupied_cells()
        cells_b = body.get_occupied_cells()        
        min = None
        
        for a in cells_a:
            for b in cells_b:
                distance = a.get_distance(b.x, b.y)
                
                if min is None or distance < min:
                    min = distance
        
        return min      
    
    def get_objects(self):
        cells = self.get_occupied_cells()
        objects = []
            
        for cell in cells:
            for obj in cell.objects:
                if obj is not self.object and obj not in objects and 'Character' not in obj.components:
                    objects.append(obj)
            
        return objects
    
    def get_occupied_cells(self):
        return [self.map.get_cell(self.x, self.y)]
    
    def get_size(self):
        return 1
    
    def get_type(self):
        return 'Body'
    
    def is_moveable(self):
        return self.map is not None and self.x is not None and self.y is not None
    
    def move(self, direction):
        if self.is_moveable():
            return self.add_to_map(self.map, self.x + Body.direction_x[direction], self.y + Body.direction_y[direction])                   
        
        return False
    
    def remove_from_map(self):
        if self.object is not None:
            self.map.get_cell(self.x, self.y).objects.remove(self.object)
        
        self.x = None
        self.y = None
        self.map = None
    