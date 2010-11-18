#!/usr/bin/env python

class Widget:
    
    def __init__(self, name, x, y):
        self.name = name
        
        self.x = x
        self.y = y
        
        self.size_x = 0
        self.size_y = 0
        
        self.must_update = False
    
    def draw(self, surface):
        if self.must_update:
            self.update_image()
            
        surface.blit(self.image, (self.x, self.y))
    
    def is_inside(self, x, y):
        if x >= self.x and y >= self.y and x < (self.x + self.size_x) and y < (self.y + self.size_y):
            return True
        else:
            return False
    
    def on_button_1_down(self, x, y):
        return False
    
    def on_button_1_up(self, x, y):
        return False
    
    def on_button_2_down(self, x, y):
        return False
    
    def on_button_2_up(self, x, y):
        return False
    
    def save(self, file):
        file.write('Widget %s\n' % (self.name))
    
    def update_image(self):
        pass