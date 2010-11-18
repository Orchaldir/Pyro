#!/usr/bin/env python

from content.object.Template import create_object
from content.object.components.Body import Body
from content.world.Cell import Cell
import utility.Path

maps = {}
path = None

class Map:
    
    def __init__(self, name):
        self.name = name
        self.width = 0
        self.height = 0
        self.cells = {}
        self.objects = {}
        self.updates = []
        self.objects_to_remove = []
        self.sound_listener = []
    
    def add_object(self, obj, x, y):
        if obj.body is None:
            obj.add_component(Body())
        
        if obj.body.add_to_map(self, x, y):
            self.objects[obj.id] = obj
            self.updates.append(obj)
            obj.owner = self
            
            if 'Perception' in obj.components:
                self.sound_listener.append(obj.components['Perception'])
            
            return True
        
        return False
    
    def add_sound(self, x, y, loudness, generators=[]):
        if loudness > 0.0:
            print 'new Sound : %d %d %f' % (x, y, loudness)
            for listener in self.sound_listener:
                listener.add_sound(x, y, loudness, generators)
    
    def create(self, width, height, cell_type_name):
        self.width = width
        self.height = height
        self.cells = {}
        for x in range(0, width):
            for y in range(0, height):
                self.cells[(x,y)] = Cell(x, y, cell_type_name)
    
    def get_cell(self, x, y):
        if (x,y) in self.cells:
            return self.cells[(x,y)]
        else: 
            return None
        
    def draw(self):
        for cell in self.cells.values():
            cell.draw()
        
        for obj in self.objects.values():
            obj.draw()
    
    def load(self, filename):
        global path
    
        file = open(utility.Path.join(path, filename), 'r')
        
        line = file.readline().split()
        
        self.width = int(line[0])
        self.height = int(line[1])
        
        for x in range(0, self.width):
            for y in range(0, self.height):
                line = file.readline().split()
                self.cells[(x,y)] = Cell(x, y, line[0])
        
        line = file.readline().split()
        
        for i in range(int(line[0])):
            line = file.readline().split()
            
            self.add_object(create_object(line[0]), int(line[1]), int(line[2]))
            
                
        file.close()
        
        return True
    
    def remove_object(self, obj):
        if obj.id in self.objects:
            if obj is self.objects[obj.id]:
                del self.objects[obj.id]
                obj.body.remove_from_map()
                
                if obj in self.updates:
                    self.updates.remove(obj)
                else:
                    self.objects_to_remove.append(obj)
                
                if 'Perception' in obj.components:
                    self.sound_listener.remove(obj.components['Perception'])
    
    def save(self, filename):
        global path
        
        file = open(utility.Path.join(path, filename), 'w')
        
        file.write('%d %d\n' % (self.width, self.height))
        
        for x in range(0, self.width):
            for y in range(0, self.height):
                cell = self.cells[(x, y)]
                file.write('%s\n' % (cell.cell_type.name))
                
        file.close()
    
    def update(self):
        updates = []
        
        for i in range(len(self.updates)):
            if len(self.updates) is 0:
                break
            
            obj = self.updates[0]
            
            if obj.update():
                self.updates.remove(obj)
                updates.append(obj)
            else:
                break
        
        for obj in updates:
            if not obj in self.objects_to_remove:
                self.updates.append(obj)
        
        self.objects_to_remove = []                


def init_maps():
    global maps, path
    
    maps = {}
    path = utility.Path.get('maps')    

def create_map(name, width, height, cell_type_name):
    global maps
    
    map = get_map(name)
    
    if map is None:
        map = Map(name)
        maps[name] = map
        
    map.create(width, height, cell_type_name)
    
    return map

def get_map(name):
    global maps
    
    if name in maps:
        return maps[name]
    else:
        return None

def load_map(name, filename):
    global maps
    
    map = get_map(name)
    
    if map is None:
        map = Map(name)
        maps[name] = map
        
    map.load(filename)
    
    return map

def save_map(name, filename):
    map = get_map(name)
    
    if map is not None:
        map.save(filename)
