#!/usr/bin/env python

import resource.Tile
import utility.Path


class CellType:
    
    def __init__(self, name, solid=True, opaque=True, tile_name=None):
        self.name = name
        
        self.solid = solid
        self.opaque = opaque
        
        self.tile = resource.Tile.get(tile_name)    


celltypes = {}
default = CellType('Default', False, False)
path = ''


def init_celltypes(file=None):
    global celltypes, default, path
    
    path = utility.Path.get('celltypes')
    celltypes = {}
    default = CellType('Default', False, False)
    
    if file is not None:
        load_celltypes(file)

def create_celltype(name, solid, opaque, tile_name=None): 
    if not isinstance(name, basestring):
        raise TypeError('name must be a string')
    
    if not isinstance(solid, bool):
        raise TypeError('solid must be a bool')
    
    if not isinstance(opaque, bool):
        raise TypeError('opaque must be a bool')
    
    global celltypes
    cell_type = CellType(name, solid, opaque, tile_name)
    celltypes[name] = cell_type
    return cell_type

def get_celltype(name):
    global celltypes, default
    
    if name in celltypes:
        return celltypes[name]
    else:
        return default

def load_celltypes(name):
    global celltypes, path
    
    file = open(utility.Path.join(path, name), 'r')
        
    line = file.readline().split()
    
    number = int(line[0])
    
    for i in range(number):
        line = file.readline().split()
        
        create_celltype(line[0], line[1] == 'True', line[2] == 'True', line[3])
                
    file.close()

def save_celltypes(name):
    global celltypes, path
    
    file = open(utility.Path.join(path, name), 'w')
        
    file.write('%d\n' % (len(celltypes)))
    
    for cell_type in celltypes.values():
        file.write('%s %s %s %s\n' % (cell_type.name, cell_type.solid, cell_type.opaque, cell_type.tile.name))
                
    file.close()

