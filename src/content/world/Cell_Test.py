#!/usr/bin/env python

import unittest
import math

from content.world.CellType import create_celltype
import content.world.Cell

class CellTest(unittest.TestCase):
    
    def setUp(self):
        self.celltype1 = create_celltype('Floor', False, False)
        self.celltype2 = create_celltype('Wall', True, False)
    
    def test_init(self):
        cell1 = content.world.Cell.Cell(10, 20, 'Floor') 
        self.assertEqual(cell1.x, 10)
        self.assertEqual(cell1.y, 20)    
        self.assertEqual(cell1.celltype, self.celltype1)  
        
        cell2 = content.world.Cell.Cell(100, 200, 'Wall') 
        self.assertEqual(cell2.x, 100)
        self.assertEqual(cell2.y, 200)    
        self.assertEqual(cell2.celltype, self.celltype2)
    
    def test_get_distance(self):
        cell_a = content.world.Cell.Cell(1, 1)
        
        for x in range(-1, 3):
            for y in range(-1, 3):
                cell_b = content.world.Cell.Cell(1 + x, 1 + y)
                self.assertEqual(cell_a.get_distance(cell_b.x, cell_b.y), int(math.fabs(x) + math.fabs(y)))
                self.assertEqual(cell_b.get_distance(cell_a.x, cell_a.y), int(math.fabs(x) + math.fabs(y)))
    
    def test_is_walkable(self):
        cell_a = content.world.Cell.Cell(10, 20, 'Floor') 
        cell_b = content.world.Cell.Cell(100, 200, 'Wall')
        
        #self.assertTrue(cell_a.is_walkable(None))
        #self.assertFalse(cell_b.is_walkable(None))

if __name__ == "__main__":
    unittest.main()   
