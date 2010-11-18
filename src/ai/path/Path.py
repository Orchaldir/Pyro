#!/usr/bin/env python

from heapq import heappush, heappop

class PathNode:
    
    def __init__(self):
        pass
    
    def get_neighbors(self):
        return []
    
    def get_total_cost(self):
        return 0
    
    def is_walkable(self, agent):
        return False
    
    def is_equal(self, node):
        return False


class Path:
    
    def __init__(self):
        pass
    
    def get(self):
        return None
    
    def has_next(self):
        return False
    
    def next(self):
        return False


def find_path(agent, start, goal, create):
    open = []
    closed = []
    
    if not goal.is_walkable(agent):
        neighbors = goal.get_neighbors()
        
        walkable = False
        
        for neighbor in neighbors:
            if neighbor.is_walkable(agent):
                walkable = True
        
        if not walkable:
            return None
        
    
    open.append(start)
    
    def compare(a, b):
        return cmp(a.get_total_cost(), b.get_total_cost())
    
    while len(open) > 0:
        open.sort(compare)
        
        node = open.pop(0)
        
        if node.is_equal(goal):
            return create(node)
        
        neighbors = node.get_neighbors()
        
        for neighbor in neighbors:
            if not neighbor.is_walkable(agent) and not neighbor.is_equal(goal): # if goal is an enemy, it isn't walkable
                continue
            
            new_node = None
            in_open = False
            
            for open_node in open:
                if neighbor.is_equal(open_node):
                    new_node = open_node
                    in_open = True
                    break
            
            if new_node is None:
                for closed_node in closed:
                    if neighbor.is_equal(closed_node):
                        new_node = closed_node
                        break
                    
            if new_node is not None:
                if new_node.cost_from_start < neighbor.cost_from_start:
                    continue
                
                new_node.parent = node
                new_node.cost_from_start = neighbor.cost_from_start
                
                if in_open:
                    open.remove(new_node)
                else:
                    closed.remove(new_node)
            else:
                new_node = neighbor
            
            open.append(new_node)
            
        closed.append(node)