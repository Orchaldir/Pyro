#!/usr/bin/env python

from content.actions.Move import can_move

class Patrol:
    
    def __init__(self, points=[], max_priority=0):
        self.points = points
        self.max_priority = max_priority
        self.index = 0
        self.path = None
    
    def execute(self, actor):
        moved = False
        
        while not moved:
            if self.path is None:
                x, y = self.points[self.index]
                self.path = actor.find_path(x, y)
        
            if self.path is not None and self.path.has_next():
                if can_move(actor, self.path.get()):
                    self.path.next()
                    return 'Success'
                else:
                    self.path = None
            else:
                self.index =  (self.index + 1) % len(self.points)
                self.path = None
    
    def get_priority(self):
        return self.max_priority
    
    def load(self, file):
        line = file.readline().split()
        self.max_priority = float(line[0])
        
        line = file.readline().split()
        self.points = []
        
        for i in range(int(line[0])):
            line = file.readline().split()
            
            self.points.append((int(line[0]), int(line[1])))
        
        return True
    
    def prepare(self):
        pass

    def stop(self):
        self.path = None