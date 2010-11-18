#!/usr/bin/env python

from ai.path.Path import find_path
from content.world.MapPath import MapPath, MapPathNode

objects = {}

class Object:
    
    def __init__(self, id):
        self.id = id
        self.components = {}
        self.body = None
        self.owner = None
    
    def add_component(self, component):
        if component.get_type() is 'Body':
            self.body = component
            self.body.object = self       
        else:
            self.components[component.get_type()] = component   
        
        if component.get_type() is 'Perception' or component.get_type() is 'Health' or component.get_type() is 'Character':   
            component.object = self  
    
    def draw(self):
        if self.body is not None:
            self.body.draw()
    
    def get_component(self, type):
        if type in self.components:
            return self.components[type]
        else:
            return None
    
    def find_path(self, goal_x, goal_y):
        if self.body is not None and self.body.is_moveable():
                goal = MapPathNode(goal_x, goal_y, goal=0, size=self.body.get_size())
                start = MapPathNode(self.body.x, self.body.y, None, 0, goal, self.body.map)
                return find_path(self, start, goal, lambda x: MapPath(x))
        
        return None
    
    def remove(self):
        if self.owner is not None:
            self.owner.remove_object(self)
            self.owner = None
    
    def update(self):
        if 'Perception' in self.components:
            self.components['Perception'].update(self)
        
        if 'Controller' in self.components:
            controller = self.components['Controller']
            return controller.update(self)
        
        return True


def add_object(obj):
    global objects
    
    objects[obj.id] = obj

def get_object(id):
    global objects
    
    if id in objects:
        return objects[id]
    else:
        return None
    