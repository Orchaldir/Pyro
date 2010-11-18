#!/usr/bin/env python

from ai.behavior.Selector import Selector
from ai.behavior.actions.Attack import Attack
from ai.behavior.actions.Investigate import Investigate
from ai.behavior.actions.Patrol import Patrol
import utility.Path

behaviors = {}
path = None

def init_behaviors(filename=None):
    global behaviors, path
    
    behaviors = {}
    path = utility.Path.get('behaviors') 
    
    if filename is not None:
        load_behaviors(filename)    

def get_behavior(id):
    global behaviors
    
    if id in behaviors:
        return behaviors[id]
    else:
        return None

def load_behaviors(filename):
    global behaviors, path
    
    behaviors = {}
        
    file = open(utility.Path.join(path, filename), 'r')
    
    line = file.readline().split()
    
    for i in range(int(line[0])):
        line = file.readline().split()
        id = line[0]
        
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
            return 
        
        if not behavior.load(file):
            behaviors = {}
            return        
        
        behaviors[id] = behavior
    
    file.close()