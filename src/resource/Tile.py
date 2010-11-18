#!/usr/bin/env python

#import os.path
import pygame

import resource.Image
import utility.Path

path = ''
size_x = 10
size_y = 10
tiles = {}
default = None
actual_surface = None

class Tile:
    
    def __init__(self, name):
        self.name = name
        self.images = {}
    
    def add_size(self, size):
        return False
    
    def draw(self, x, y, size=1):
        global size_x, size_y, actual_surface
        
        if size in self.images:
            actual_surface.blit(self.images[size], (x * size_x, y * size_y))
        else:
            if self.add_size(size):
                actual_surface.blit(self.images[size], (x * size_x, y * size_y))
        

class ColorTile(Tile):
    
    def __init__(self, name, r, g, b, a=255):
        Tile.__init__(self, name)
        
        self.r = r
        self.g = g 
        self.b = b 
        self.a = a    
        
    def add_size(self, size):
        global size_x, size_y
        
        self.images[size] = self.get_image(size_x * size, size_y * size)
        return True
    
    def get_image(self, size_x, size_y):
        surface = pygame.Surface((size_x, size_y))
        surface.fill((self.r, self.g, self.b))    
        if self.a < 255:
            surface.set_alpha(self.a)
        return surface
    
    def save(self, file):
        file.write('C %s %d %d %d %d\n' % (self.name, self.r, self.g, self.b, self.a))
    
    
class ImageTile(Tile):
    
    def __init__(self, name, image_name):
        Tile.__init__(self, name)
        
        self.image_name = image_name    
        self.image = None           
        
    def add_size(self, size):
        global size_x, size_y
        
        self.images[size] = self.get_image(size_x * size, size_y * size)#pygame.transform.flip(, False, True)
        return True
    
    def get_image(self, size_x, size_y):
        if self.image is None:
            self.image = resource.Image.load(utility.Path.join('tiles', self.image_name))
            
        return pygame.transform.scale(self.image, (size_x, size_y))
    
    def save(self, file):
        file.write('I %s %s\n' % (self.name, self.image_name))


def init(file=None):
    global tiles, default, path
    
    path = utility.Path.get('tiles')
    tiles = {}
    default = ColorTile('Default', 255, 0, 255)
    
    if file is not None:
        load(file)

def set_size(new_size_x, new_size_y):
    global size_x, size_y
    
    size_x = new_size_x
    size_y = new_size_y

def create_color_tile(name, r, g, b, a=255):
    global tiles
    
    tile = ColorTile(name, r, g, b, a)
    tiles[name] = tile
    return tile

def create_image_tile(name, image_name):
    global tiles
    
    tile = ImageTile(name, image_name)
    tiles[name] = tile
    return tile

def get(name):
    global tiles, default
    
    if name in tiles:
        return tiles[name]
    else:
        return default

def load(name):
    global tiles, path
    
    file = open(utility.Path.join(path, name), 'r')
        
    line = file.readline().split()
    
    number = int(line[0])
    
    for i in range(number):
        line = file.readline().split()
        
        if line[0] is 'C':
            create_color_tile(line[1], int(line[2]), int(line[3]), int(line[4]), int(line[5]))
        elif line[0] is 'I':
            create_image_tile(line[1], line[2])
                
    file.close()

def save(name):
    global tiles, path
    
    file = open(utility.Path.join(path, name), 'w')
        
    file.write('%d\n' % (len(tiles)))
    
    for tile in tiles.values():
        tile.save(file)
                
    file.close()

