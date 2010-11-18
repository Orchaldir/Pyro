#!/usr/bin/env python

import unittest

from content.object.Object import Object
from content.object.components.bodies.Big import Big
from content.world.CellType import create_celltype, get_celltype
from content.world.Map import create_map

class SimpleTest(unittest.TestCase):
    
    def setUp(self):
        self.obj = Object('Test')
        self.body = Big(2)
        self.obj.add_component(self.body)
        create_celltype('Floor', False, False)
        create_celltype('Wall', True, False)
        self.map = create_map('Test', 10, 10, 'Floor')
    
    def check(self, x, y):
        self.assertEqual(self.body.x, x)
        self.assertEqual(self.body.y, y)
                
        self.assertEquals(len(self.body.occupied_cells), 4)
        
        for j in range(0, 9):
            for k in range(0, 9):
                cell = self.map.get_cell(j, k)
                if (j is x or j is x + 1) and (k is y or k is y + 1):
                    self.assertTrue(cell in self.body.occupied_cells)
                    self.assertTrue(self.obj in cell.objects)
                else:
                    self.assertFalse(cell in self.body.occupied_cells)
                    self.assertFalse(self.obj in cell.objects)
    
    def test_get_occupied_cells(self):
        self.map = create_map('Test', 10, 10, 'Floor')
        
        for x in range(0, 9):
            for y in range(0, 9):
                self.body.add_to_map(self.map, x, y)
                cells = self.body.get_occupied_cells()
                
                self.assertEquals(len(cells), 4)
                self.assertTrue(self.map.get_cell(x, y) in cells)
                self.assertTrue(self.map.get_cell(x, y + 1) in cells)
                self.assertTrue(self.map.get_cell(x + 1, y) in cells)
                self.assertTrue(self.map.get_cell(x + 1, y + 1) in cells)
    
    # add
    
    def test_add_to_map(self):
        self.map = create_map('Test', 10, 10, 'Floor')
        
        # inside
        
        for x in range(0, 9):
            for y in range(0, 9):
                self.assertTrue(self.body.add_to_map(self.map, x, y))
                
                self.check(x, y)
                
        
        # outside
        
        self.assertFalse(self.body.add_to_map(self.map, -1, -1))
        self.assertFalse(self.body.add_to_map(self.map, 9, -1))
        self.assertFalse(self.body.add_to_map(self.map, -1, 9))
        self.assertFalse(self.body.add_to_map(self.map, 9, 9))
        
        self.check(8, 8)
        
        # solid
        
        self.map.get_cell(5, 5).celltype = get_celltype('Wall')
        
        self.assertFalse(self.body.add_to_map(self.map, 5, 5))
        self.assertFalse(self.body.add_to_map(self.map, 4, 5))
        self.assertFalse(self.body.add_to_map(self.map, 5, 4))
        self.assertFalse(self.body.add_to_map(self.map, 4, 4))
        
        self.check(8, 8)
    
    def test_map_add_object(self):
        self.map = create_map('Test', 10, 10, 'Floor') 
        
        # inside
        
        for x in range(0, 9):
            for y in range(0, 9):
                self.assertTrue(self.map.add_object(self.obj, x, y))
                
                self.check(x, y)
        
        # outside
        
        self.assertFalse(self.map.add_object(self.obj, -1, 0))
        self.assertFalse(self.map.add_object(self.obj, 0, -1))
        self.assertFalse(self.map.add_object(self.obj, 10, 9))
        self.assertFalse(self.map.add_object(self.obj, 9, 10))
        
        self.check(8, 8)
        
        # solid
        
        self.map.get_cell(5, 5).celltype = get_celltype('Wall')
        
        self.assertFalse(self.map.add_object(self.obj, 5, 5))
        self.assertFalse(self.map.add_object(self.obj, 4, 5))
        self.assertFalse(self.map.add_object(self.obj, 5, 4))
        self.assertFalse(self.map.add_object(self.obj, 4, 4))
        
        self.check(8, 8)
    
    # move
    
    def test_move(self):
        self.map = create_map('Test', 10, 10, 'Floor')
        self.map.add_object(self.obj, 0, 0)
        
        # inside
        
        self.assertTrue(self.body.move(1))
        self.check(1, 0)
                
        self.assertTrue(self.body.move(0))
        self.check(1, 1)
        
        self.assertTrue(self.body.move(3))
        self.check(0, 1)
        
        self.assertTrue(self.body.move(2))
        self.check(0, 0)
        
        # outside
        
        self.assertFalse(self.body.move(3))     
        self.check(0, 0)           
        self.assertFalse(self.body.move(2))
        self.check(0, 0)
        
        self.map.add_object(self.obj, 8, 8)
        
        self.assertFalse(self.body.move(1))
        self.check(8, 8)
        self.assertFalse(self.body.move(0))
        self.check(8, 8)
        
        # solid
        
        self.map.get_cell(5, 5).celltype = get_celltype('Wall')
        
        self.map.add_object(self.obj, 3, 5)        
        self.assertFalse(self.body.move(1))
        self.check(3, 5)
        
        self.map.add_object(self.obj, 3, 4)        
        self.assertFalse(self.body.move(1))
        self.check(3, 4)
        
        self.map.add_object(self.obj, 6, 5)        
        self.assertFalse(self.body.move(3))
        self.check(6, 5)
        
        self.map.add_object(self.obj, 6, 4)        
        self.assertFalse(self.body.move(3))
        self.check(6, 4)
        
        self.map.add_object(self.obj, 5, 3)        
        self.assertFalse(self.body.move(0))
        self.check(5, 3)
        
        self.map.add_object(self.obj, 4, 3)        
        self.assertFalse(self.body.move(0))
        self.check(4, 3)
        
        self.map.add_object(self.obj, 5, 6)        
        self.assertFalse(self.body.move(2))
        self.check(5, 6)
        
        self.map.add_object(self.obj, 4, 6)        
        self.assertFalse(self.body.move(2))
        self.check(4, 6)
    
    """def test_objects_move(self):
        self.map = create_map('Test', 10, 10, 'Floor')
        self.map.add_object(self.obj, 0, 0)
        
        # inside
        
        self.assertTrue(self.obj.move(1))
        self.check(1, 0)
                
        self.assertTrue(self.obj.move(0))
        self.check(1, 1)
        
        self.assertTrue(self.obj.move(3))
        self.check(0, 1)
        
        self.assertTrue(self.obj.move(2))
        self.check(0, 0)
        
        # outside
        
        self.assertFalse(self.obj.move(3))     
        self.check(0, 0)           
        self.assertFalse(self.obj.move(2))
        self.check(0, 0)
        
        self.map.add_object(self.obj, 8, 8)
        
        self.assertFalse(self.obj.move(1))
        self.check(8, 8)
        self.assertFalse(self.obj.move(0))
        self.check(8, 8)
        
        # solid
        
        self.map.get_cell(5, 5).celltype = get_celltype('Wall')
        
        self.map.add_object(self.obj, 3, 5)        
        self.assertFalse(self.obj.move(1))
        self.check(3, 5)
        
        self.map.add_object(self.obj, 3, 4)        
        self.assertFalse(self.obj.move(1))
        self.check(3, 4)
        
        self.map.add_object(self.obj, 6, 5)        
        self.assertFalse(self.obj.move(3))
        self.check(6, 5)
        
        self.map.add_object(self.obj, 6, 4)        
        self.assertFalse(self.obj.move(3))
        self.check(6, 4)
        
        self.map.add_object(self.obj, 5, 3)        
        self.assertFalse(self.obj.move(0))
        self.check(5, 3)
        
        self.map.add_object(self.obj, 4, 3)        
        self.assertFalse(self.obj.move(0))
        self.check(4, 3)
        
        self.map.add_object(self.obj, 5, 6)        
        self.assertFalse(self.obj.move(2))
        self.check(5, 6)
        
        self.map.add_object(self.obj, 4, 6)        
        self.assertFalse(self.obj.move(2))
        self.check(4, 6)"""
    
    # remove
    
    def test_remove_from_map(self):
        self.map = create_map('Test', 10, 10, 'Floor')
        
        for x in range(0, 9):
            for y in range(0, 9):
                self.body.add_to_map(self.map, x, y)        
                self.body.remove_from_map()
                
                self.assertEqual(self.body.map, None)
                self.assertEqual(self.body.x, None)
                self.assertEqual(self.body.y, None)
                self.assertEquals(len(self.body.occupied_cells), 0)
                
                self.assertFalse(self.obj in self.map.get_cell(x, y).objects)
                self.assertFalse(self.obj in self.map.get_cell(x, y + 1).objects)
                self.assertFalse(self.obj in self.map.get_cell(x + 1, y).objects)
                self.assertFalse(self.obj in self.map.get_cell(x + 1, y + 1).objects)
        
        for x in range(0, 10):
            for y in range(0, 10):
                self.assertFalse(self.obj in self.map.get_cell(x, y).objects)