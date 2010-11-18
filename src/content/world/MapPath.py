#!/usr/bin/env python

import math

class MapPathNode:
    
    goal = None
    map = None
    size = 1
    
    def __init__(self, x, y, parent=None, cost_from_start=0, goal=None, map=None, size=None):
        if map is not None:            
            MapPathNode.map = map
        
        if size is not None:            
            MapPathNode.size = size
            
        if goal is 0:
            MapPathNode.goal = None
        elif goal is not None:            
            MapPathNode.goal = goal
             
            
        self.x = x
        self.y = y
        self.parent = parent
        
        self.walkable = None
        
        self.cost_from_start = cost_from_start
        if MapPathNode.goal is None:
            self.cost_to_goal = 0
        else:
            self.cost_to_goal = math.fabs(MapPathNode.goal.x - self.x) + math.fabs(MapPathNode.goal.y - self.y)
    
    def get_neighbor(self, x, y, neighbors):
        for cx in range(0, MapPathNode.size):
            for cy in range(0, MapPathNode.size):            
                cell = MapPathNode.map.get_cell(x + cx, y + cy)
                
                if cell is None:
                    return
        
        neighbors.append(MapPathNode(x, y, self, self.cost_from_start + 1))
    
    def get_neighbors(self):
        neighbors = []
        
        self.get_neighbor(self.x + 1, self.y, neighbors)
        self.get_neighbor(self.x - 1, self.y, neighbors)
        self.get_neighbor(self.x, self.y + 1, neighbors)
        self.get_neighbor(self.x, self.y - 1, neighbors)
        
        return neighbors
    
    def get_total_cost(self):
        return self.cost_from_start + self.cost_to_goal
    
    def calculate(self, agent):
        for cx in range(0, MapPathNode.size):
            for cy in range(0, MapPathNode.size):            
                cell = MapPathNode.map.get_cell(self.x + cx, self.y + cy)
                
                if not cell.is_walkable(agent):
                    return False
                
        return True
    
    def is_walkable(self, agent):
        if self.walkable is None:
            self.walkable = self.calculate(agent)
        
        return self.walkable
    
    def is_equal(self, node):
        return self.x is node.x and self.y is node.y


class MapPath:
    
    def __init__(self, node):
        self.points = []
        
        while node is not None and node.parent is not None:
            x = node.x - node.parent.x
            y = node.y - node.parent.y
            
            if x is 0 and y is 1:
                self.points.append(0)
            elif x is 1 and y is 0:
                self.points.append(1)
            elif x is 0 and y is -1:
                self.points.append(2)
            elif x is -1 and y is 0:
                self.points.append(3)
            else:
                print 'Error: MapPath'
                
            node = node.parent
        
        self.points.reverse()
        self.index = 0
    
    def get(self):
        return self.points[self.index]
    
    def has_next(self):
        return self.index < len(self.points)
    
    def next(self):
        if self.index < len(self.points):
            self.index = self.index + 1