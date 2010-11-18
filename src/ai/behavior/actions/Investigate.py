#!/usr/bin/env python

from content.actions.Move import can_move

class Investigate:
    
    def __init__(self, max_priority=0):
        self.max_priority = max_priority
    
    def execute(self, actor):
        perception = actor.components['Perception']
        
        if perception.sound is None:
            return 'Failed'
        
        print 'Investigate : ' + str(perception.sound.loudness)
        
        path = actor.find_path(perception.sound.x, perception.sound.y)
        
        if path is not None and path.has_next():
            if can_move(actor, path.get()):
                path.next()
                
                return 'Success'
        
        perception.sound = None
        
        return 'Failed'
    
    def get_priority(self):
        return self.max_priority
    
    def load(self, file):
        line = file.readline().split()
        self.max_priority = float(line[0])
        return True
    
    def prepare(self):
        pass
    
    def stop(self):
        pass