#!/usr/bin/env python

import unittest
import math

from content.object.Object import Object
from content.object.components.bodies.Simple import Simple
from content.object.components.bodies.Big import Big
from content.world.CellType import create_celltype, get_celltype
from content.world.Map import create_map

class SimpleTest(unittest.TestCase):
    
    def setUp(self):
        self.obj = Object('Test')
        self.body = Simple()
        self.obj.add_component(self.body)
        create_celltype('Floor', False, False)
        create_celltype('Wall', True, False)
        
    def check(self, x, y):
        self.assertEqual(self.body.x, x)
        self.assertEqual(self.body.y, y)
        
        self.assertTrue(self.obj in self.map.get_cell(x, y).objects)
        
        for j in range(0, 10):
            for k in range(0, 10):
                cell = self.map.get_cell(j, k)
                if j is not x and k is not y:
                    self.assertFalse(self.obj in cell.objects)     
    
    def test_get_distance_to_body(self):
        map = create_map('Test', 10, 10, 'Floor')
        map.add_object(self.obj, 5, 5)        
        obj = Object('Simple')
        
        # simple
                
        simple = Simple()
        obj.add_component(simple)
        
        for j in range(-2, 5):
            for k in range(-2, 5):
                map.add_object(obj, 5 + j, 5 + k)
                
                self.assertEqual(self.body.get_distance_to_body(simple), int(math.fabs(j) + math.fabs(k)))
                
        # big
        
        big = Big(3)
        obj.add_component(big)
        
        map.add_object(obj, 2, 2)
        self.assertEqual(self.body.get_distance_to_body(big), 2)
        
        map.add_object(obj, 6, 2)
        self.assertEqual(self.body.get_distance_to_body(big), 2)
        
        map.add_object(obj, 2, 6)
        self.assertEqual(self.body.get_distance_to_body(big), 2)
        
        map.add_object(obj, 6, 6)
        self.assertEqual(self.body.get_distance_to_body(big), 2)
        
        map.add_object(obj, 0, 0)
        self.assertEqual(self.body.get_distance_to_body(big), 6)            
    
    def test_get_occupied_cells(self):
        self.map = create_map('Test', 10, 10, 'Floor')
        
        for x in range(0, 10):
            for y in range(0, 10):
                self.body.add_to_map(self.map, x, y)
                cells = self.body.get_occupied_cells()
                
                self.assertEquals(len(cells), 1)
                self.assertEquals(cells[0], self.map.get_cell(x, y))
    
    def test_get_size(self):
        self.assertEqual(self.body.get_size(), 1)
    
    def test_get_type(self):
        self.assertEqual(self.body.get_type(), 'Body')
    
    # add
    
    def test_add_to_map(self):
        self.map = create_map('Test', 10, 10, 'Floor')
        
        # inside
        
        for x in range(0, 10):
            for y in range(0, 10):
                self.assertTrue(self.body.add_to_map(self.map, x, y))
                
                self.check(x, y)
        
        # outside
        
        self.assertFalse(self.body.add_to_map(self.map, -1, 0))
        self.assertFalse(self.body.add_to_map(self.map, 0, -1))
        self.assertFalse(self.body.add_to_map(self.map, 10, 9))        
        self.assertFalse(self.body.add_to_map(self.map, 9, 10))
        
        self.check(9, 9)
        
        # solid
        
        self.map.get_cell(5, 5).celltype = get_celltype('Wall')
        self.assertFalse(self.body.add_to_map(self.map, 5, 5))
        
        self.check(9, 9)
    
    def test_map_add_object(self):
        self.map = create_map('Test', 10, 10, 'Floor') 
        
        # inside
        
        for x in range(0, 10):
            for y in range(0, 10):
                self.assertTrue(self.map.add_object(self.obj, x, y))
                
                self.check(x, y)
        
        # outside
        
        self.assertFalse(self.map.add_object(self.obj, -1, 0))
        self.assertFalse(self.map.add_object(self.obj, 0, -1))
        self.assertFalse(self.map.add_object(self.obj, 10, 9))
        self.assertFalse(self.map.add_object(self.obj, 9, 10))
        
        self.check(9, 9)
        
        # solid
        
        self.map.get_cell(5, 5).celltype = get_celltype('Wall')
        self.assertFalse(self.map.add_object(self.obj, 5, 5))
        
        self.check(9, 9)
    
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
        
        self.map.add_object(self.obj, 9, 9)
        
        self.assertFalse(self.body.move(1))
        self.check(9, 9)        
        self.assertFalse(self.body.move(0))
        self.check(9, 9)
        
        # solid
        
        self.map.get_cell(5, 5).celltype = get_celltype('Wall')
        
        self.map.add_object(self.obj, 4, 5)        
        self.assertFalse(self.body.move(1))
        self.check(4, 5)
        
        self.map.add_object(self.obj, 6, 5)        
        self.assertFalse(self.body.move(3))
        self.check(6, 5)
        
        self.map.add_object(self.obj, 5, 4)        
        self.assertFalse(self.body.move(0))
        self.check(5, 4)
        
        self.map.add_object(self.obj, 5, 6)        
        self.check(5, 6)
    
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
        
        self.map.add_object(self.obj, 9, 9)
        
        self.assertFalse(self.obj.move(1))
        self.check(9, 9)        
        self.assertFalse(self.obj.move(0))
        self.check(9, 9)
        
        # solid
        
        self.map.get_cell(5, 5).celltype = get_celltype('Wall')
        
        self.map.add_object(self.obj, 4, 5)        
        self.assertFalse(self.obj.move(1))
        self.check(4, 5)
        
        self.map.add_object(self.obj, 6, 5)        
        self.assertFalse(self.obj.move(3))
        self.check(6, 5)
        
        self.map.add_object(self.obj, 5, 4)        
        self.assertFalse(self.obj.move(0))
        self.check(5, 4)
        
        self.map.add_object(self.obj, 5, 6)        
        self.check(5, 6)"""
    
    # remove
    
    def test_remove_from_map(self):
        self.map = create_map('Test', 10, 10, 'Floor')
        
        for x in range(0, 10):
            for y in range(0, 10):
                self.body.add_to_map(self.map, x, y)        
                self.body.remove_from_map()
                
                self.assertEqual(self.body.map, None)
                self.assertEqual(self.body.x, None)
                self.assertEqual(self.body.y, None)
                
                cell = self.map.get_cell(x, y)
                
                self.assertFalse(self.obj in cell.objects)
        
        for x in range(0, 10):
            for y in range(0, 10):
                self.assertFalse(self.obj in self.map.get_cell(x, y).objects)
        
        