#!/usr/bin/env python

from content.actions.Attack import can_attack
from content.actions.Move import can_move

class Attack:
    
    def __init__(self, max_priority=0):
        self.max_priority = max_priority
    
    def execute(self, actor):
        enemies = actor.components['Perception'].get_enemies()
        
        #print 'Attack: ', actor.name, ' ', len(enemies)
        
        if len(enemies) is 0:
            return 'Failed'
        
        enemy = enemies[0]
        
        if can_attack(actor, enemy):
            #actor.attack(enemy)
            return 'Success'
        
        path = actor.find_path(enemy.body.x, enemy.body.y)
        
        if path is not None and path.has_next():
            if can_move(actor, path.get()):
                path.next()
                return 'Success'
        
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