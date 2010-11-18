#!/usr/bin/env python

from ai.behavior.actions.Attack import Attack
from ai.behavior.actions.Investigate import Investigate
from ai.behavior.actions.Patrol import Patrol

class Selector:
    
    def __init__(self, behaviors=[]):
        self.behaviors = behaviors
        self.priority = 0
        self.active = None
    
    def execute(self, actor):
        def compare(a, b):
            return cmp(b.get_priority(), a.get_priority())
        
        self.behaviors.sort(compare)
        
        for behavior in self.behaviors:
            status = behavior.execute(actor)
            
            if status == 'Success':
                if behavior is not self.active:
                    if self.active is not None:
                        self.active.stop()
                    self.active =  behavior
                    
                return 'Success'
        
        if self.active is not None:
            self.active.stop()
            self.active =  None
        
        return 'Failed'
    
    def load(self, file):
        line = file.readline().split()
    
        length = int(line[0])
        
        self.behaviors = []
    
        for i in range(length):
            line = file.readline().split()
        
            if line[0] == 'Selector':
                behavior = Selector()
            elif line[0] == 'Attack':
                behavior = Attack()
            elif line[0] == 'Investigate':
                behavior = Investigate()
            elif line[0] == 'Patrol':
                behavior = Patrol()
            else:
                return False
        
            behavior.load(file)        
        
            self.behaviors.append(behavior)
        
        return True
    
    def prepare(self):
        self.priority = 0
        
        for behavior in self.behaviors:
            behavior.prepare()
            
            priority = behavior.get_priority()
            
            if priority > self.priority:
                self.priority = priority
    
    def stop(self):
        if self.active is not None:
            self.active.stop()
            self.active =  None