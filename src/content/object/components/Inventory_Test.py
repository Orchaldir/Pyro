#!/usr/bin/env python

import unittest

from content.object.Object import Object
from content.object.components.Inventory import Inventory
from content.world.CellType import create_celltype, get_celltype
from content.world.Map import create_map

class InventoryTest(unittest.TestCase):
    
    def test_add(self):
        create_celltype('Floor', False, False)
        map = create_map('Test', 10, 20, 'Floor')
        inventory = Inventory()
        obj1 = Object('Test1')
        obj2 = Object('Test2')
        obj3 = Object('Test3')
        map.add_object(obj1, 1, 0)
        map.add_object(obj2, 2, 0)
        map.add_object(obj3, 3, 0)
        
        inventory.add(obj1)
        
        self.assertEquals(len(inventory.objects), 1)
        self.assertTrue(obj1 in inventory.objects)
        self.assertFalse(obj2 in inventory.objects)
        self.assertFalse(obj3 in inventory.objects)
        
        self.assertFalse(obj1.id in map.objects)
        self.assertFalse(obj1.id in map.get_cell(1, 0).objects)
        body = obj1.body
        self.assertEquals(body.map, None)
        self.assertEquals(body.x, None)
        self.assertEquals(body.y, None)        
        
        inventory.add(obj2)
        
        self.assertEquals(len(inventory.objects), 2)
        self.assertTrue(obj1 in inventory.objects)
        self.assertTrue(obj2 in inventory.objects)
        self.assertFalse(obj3 in inventory.objects)
        
        self.assertFalse(obj2.id in map.objects)
        self.assertFalse(obj2.id in map.get_cell(1, 0).objects)
        body = obj2.body
        self.assertEquals(body.map, None)
        self.assertEquals(body.x, None)
        self.assertEquals(body.y, None)
        
        inventory.add(obj3)
        
        self.assertEquals(len(inventory.objects), 3)
        self.assertTrue(obj1 in inventory.objects)
        self.assertTrue(obj2 in inventory.objects)
        self.assertTrue(obj3 in inventory.objects)
        
        self.assertFalse(obj3.id in map.objects)
        self.assertFalse(obj3.id in map.get_cell(1, 0).objects)
        body = obj3.body
        self.assertEquals(body.map, None)
        self.assertEquals(body.x, None)
        self.assertEquals(body.y, None)
        
        inventory.add(obj1)
        
        self.assertEquals(len(inventory.objects), 3)
        self.assertTrue(obj1 in inventory.objects)
        self.assertTrue(obj2 in inventory.objects)
        self.assertTrue(obj3 in inventory.objects)
    
    def test_get_number(self):
        inventory = Inventory()
        obj1 = Object('Test1')
        obj2 = Object('Test2')
        obj3 = Object('Test3')
        
        self.assertEquals(inventory.get_number(), 0) 
        
        inventory.add(obj1)
        
        self.assertEquals(inventory.get_number(), 1)
        
        inventory.add(obj2)
        
        self.assertEquals(inventory.get_number(), 2)
        
        inventory.add(obj3)
        
        self.assertEquals(inventory.get_number(), 3) 
    
    def test_get_object(self):
        inventory = Inventory()
        obj1 = Object('Test1')
        obj2 = Object('Test2')
        obj3 = Object('Test3')
        list = [obj1, obj2, obj3]
        
        inventory.add(obj1)
        inventory.add(obj2)
        inventory.add(obj3)
        
        self.assertEquals(inventory.get_object(-1), None) 
        
        for i in range(3):
            self.assertTrue(inventory.get_object(i) in list)
        
        self.assertEquals(inventory.get_object(3), None) 
    
    def test_get_type(self):
        inventory = Inventory()
        
        self.assertEquals(inventory.get_type(), 'Inventory')
    
    def test_remove(self):
        inventory = Inventory()
        obj1 = Object('Test1')
        obj2 = Object('Test2')
        obj3 = Object('Test3')
        
        inventory.add(obj1)
        inventory.add(obj2)
        inventory.add(obj3)
        
        inventory.remove_object(obj1)
        
        self.assertEquals(len(inventory.objects), 2)
        self.assertFalse(obj1 in inventory.objects)
        self.assertTrue(obj2 in inventory.objects)
        self.assertTrue(obj3 in inventory.objects)
        
        inventory.remove_object(obj2)
        
        self.assertEquals(len(inventory.objects), 1)
        self.assertFalse(obj1 in inventory.objects)
        self.assertFalse(obj2 in inventory.objects)
        self.assertTrue(obj3 in inventory.objects)
        
        inventory.remove_object(obj3)
        
        self.assertEquals(len(inventory.objects), 0)
        self.assertFalse(obj1 in inventory.objects)
        self.assertFalse(obj2 in inventory.objects)
        self.assertFalse(obj3 in inventory.objects)
        
        inventory.remove_object(obj3)
        
        self.assertEquals(len(inventory.objects), 0)
        self.assertFalse(obj1 in inventory.objects)
        self.assertFalse(obj2 in inventory.objects)
        self.assertFalse(obj3 in inventory.objects)