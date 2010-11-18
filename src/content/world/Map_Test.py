import unittest

from content.object.Object import Object
from content.world.Cell import Cell
from content.world.CellType import create_celltype
import content.world.Map

class MapTest(unittest.TestCase):
    
    def setUp(self):
        self.cell_type1 = create_celltype('Floor', False, False)
        self.cell_type2 = create_celltype('Wall', True, False)

    def test_init(self):
        map = content.world.Map.Map('test')
        
        self.assertTrue(isinstance(map, content.world.Map.Map))  
        self.assertEqual(map.name, 'test')
        self.assertEqual(map.width, 0)
        self.assertEqual(map.height, 0)
        self.assertEqual(len(map.cells), 0)
        self.assertEqual(len(map.objects), 0)
    
    def test_add_object(self):
        map = content.world.Map.create_map('test', 10, 20, 'Floor')
        obj1 = Object('Test1')
        obj2 = Object('Test2')
        
        map.add_object(obj1, 1, 2)
        
        self.assertEqual(len(map.objects), 1)
        self.assertEqual(map.objects['Test1'], obj1)
        self.assertEqual(obj1.body.map, map)
        self.assertEqual(obj1.body.x, 1)
        self.assertEqual(obj1.body.y, 2)
        
        map.add_object(obj2, 5, 5)
        
        self.assertEqual(len(map.objects), 2)
        self.assertEqual(map.objects['Test1'], obj1)
        self.assertEqual(map.objects['Test2'], obj2)
        self.assertEqual(obj2.body.map, map)
        self.assertEqual(obj2.body.x, 5)
        self.assertEqual(obj2.body.y, 5)
    
    def test_create(self):       
        map = content.world.Map.Map('test')
        map.create(10, 20, 'Floor') 
        
        self.assertEqual(map.width, 10)
        self.assertEqual(map.height, 20)
        
        for x in range(0, 10):
            for y in range(0, 20):
                cell_ = map.cells[(x,y)]
                self.assertTrue(isinstance(cell_, Cell))  
                self.assertEqual(cell_.x, x)
                self.assertEqual(cell_.y, y)
                self.assertEqual(cell_.celltype, self.cell_type1)
    
    def test_get_cell(self):
        map = content.world.Map.Map('test')
        map.create(10, 20, 'Floor')
        
        self.assertEqual(map.get_cell(-1,0), None)
        self.assertEqual(map.get_cell(10,0), None)
        
        self.assertEqual(map.get_cell(0,-1), None)
        self.assertEqual(map.get_cell(0,20), None)
        
        for x in range(0, 10):
            for y in range(0, 20):
                self.assertEqual(map.get_cell(x, y), map.cells[(x,y)])
    
    def test_remove_object(self):
        map = content.world.Map.create_map('test', 10, 20, 'Floor')
        obj1 = Object('Test1')
        obj2 = Object('Test2')
        
        map.add_object(obj1, 1, 2)
        map.add_object(obj2, 5, 5)
        
        map.remove_object(obj1)
        
        self.assertEqual(len(map.objects), 1)
        self.assertFalse(obj1 in map.objects)
        self.assertEqual(map.objects['Test2'], obj2)
        
        self.assertEqual(obj1.body.map, None)
        self.assertEqual(obj1.body.x, None)
        self.assertEqual(obj1.body.y, None)
        
        map.remove_object(obj2)
        
        self.assertEqual(len(map.objects), 0)
        self.assertFalse(obj1 in map.objects)
        self.assertFalse(obj2 in map.objects)
        
        self.assertEqual(obj2.body.map, None)
        self.assertEqual(obj2.body.x, None)
        self.assertEqual(obj2.body.y, None)
        

class GloablMapTest(unittest.TestCase):
    
    def setUp(self):
        self.cell_type1 = create_celltype('Floor', True, False)
        self.cell_type2 = create_celltype('Second', False, True)

    def test_create(self):       
        map = content.world.Map.create_map('test', 10, 20, 'Floor') 
        
        self.assertTrue(isinstance(map, content.world.Map.Map))  
        self.assertEqual(map.name, 'test')
        
        self.assertEqual(map.width, 10)
        self.assertEqual(map.height, 20)
        for x in range(0, 10):
            for y in range(0, 20):
                cell_ = map.cells[(x,y)]
                self.assertTrue(isinstance(cell_, content.world.Cell.Cell))  
                self.assertEqual(cell_.x, x)
                self.assertEqual(cell_.y, y)
                self.assertEqual(cell_.celltype, self.cell_type1)
    
    def test_get(self): 
        content.world.Map.init_maps()
        
        self.assertEqual(content.world.Map.get_map('test'), None)
              
        map = content.world.Map.create_map('test', 10, 20, 'Floor')
        
        self.assertEqual(content.world.Map.get_map('test'), map)        
        

if __name__ == "__main__":
    unittest.main()   
