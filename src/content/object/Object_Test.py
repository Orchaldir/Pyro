#!/usr/bin/env python

import unittest

from content.object.Object import Object, add_object, get_object
from content.object.components.Body import Body
from content.object.components.Inventory import Inventory
from content.world.CellType import create_celltype
from content.world.Map import create_map

class ObjectTest(unittest.TestCase):
    
    def setUp(self):
        create_celltype('Floor', False, False)
        create_celltype('Wall', True, False)
        self.map = create_map('Test', 10, 20, 'Floor')
    
    def test_init(self):
        obj = Object('Test')
        
        self.assertEqual(obj.id, 'Test')
        self.assertEqual(len(obj.components), 0)
    
    def test_add_component(self):
        obj = Object('Test')        
        component0 = Body()
        component1 = Body()
        component2 = Inventory()
        component3 = Inventory()
        
        obj.add_component(component0)
        
        self.assertEqual(len(obj.components), 0)
        self.assertEqual(obj.body, component0)
        self.assertNotEqual(obj.body, component1)
        
        obj.add_component(component1)
        
        self.assertEqual(len(obj.components), 0)
        self.assertNotEqual(obj.body, component0)
        self.assertEqual(obj.body, component1)
        
        obj.add_component(component2)
        
        self.assertEqual(len(obj.components), 1)
        self.assertEqual(obj.components['Inventory'], component2)
        self.assertNotEqual(obj.components['Inventory'], component3)
        
        obj.add_component(component3)
        
        self.assertEqual(len(obj.components), 1)
        self.assertNotEqual(obj.components['Inventory'], component2)
        self.assertEqual(obj.components['Inventory'], component3)
    
    """def test_get_objects(self):
        obj1 = Object('Test1')
        obj2 = Object('Test2')
        obj3 = Object('Test3')
        
        self.map.add_object(obj1, 5, 5)        
        objects = obj1.get_objects()
        
        self.assertEqual(len(objects), 0)
        
        self.map.add_object(obj2, 5, 5)        
        objects = obj1.get_objects()
        
        self.assertEqual(len(objects), 1)
        self.assertTrue(obj2 in objects)
        
        self.map.add_object(obj3, 5, 5)        
        objects = obj1.get_objects()
        
        self.assertEqual(len(objects), 2)
        self.assertTrue(obj2 in objects)
        self.assertTrue(obj3 in objects)
        
        objects = obj2.get_objects()
        
        self.assertEqual(len(objects), 2)
        self.assertTrue(obj1 in objects)
        self.assertTrue(obj3 in objects)
        
        objects = obj3.get_objects()
        
        self.assertEqual(len(objects), 2)
        self.assertTrue(obj1 in objects)
        self.assertTrue(obj2 in objects)"""
    
    def test_remove(self):
        pass

class GlobalObjectTest(unittest.TestCase):
    
    def test_get(self):
        obj1 = Object('Test1')
        add_object(obj1)
        obj2 = Object('Test2')
        add_object(obj2)
        
        self.assertEqual(obj1, get_object('Test1'))
        self.assertEqual(obj2, get_object('Test2'))
        self.assertEqual(None, get_object('Test3'))
        
        