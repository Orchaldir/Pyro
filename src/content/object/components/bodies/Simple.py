#!/usr/bin/env python

from content.object.components.Body import Body
import resource.Tile

class Simple(Body):
    
    def __init__(self, tile=None):
        Body.__init__(self)
        
        self.tile = resource.Tile.get(tile)
    
    def draw(self):
        self.tile.draw(self.x, self.y)