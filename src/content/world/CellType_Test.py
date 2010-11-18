#!/usr/bin/env python

import unittest

import content.world.CellType
import resource.Tile
import utility.Path

class CellTypeTest(unittest.TestCase):
    
    def test_init(self):
        cell_type = content.world.CellType.CellType('Test', True, False)
        
        self.assertEqual(cell_type.name, 'Test')
        self.assertEqual(cell_type.solid, True)
        self.assertEqual(cell_type.opaque, False)
        self.assertEqual(cell_type.tile, resource.Tile.default)


class GlobalCellTypeTest(unittest.TestCase):
    
    def test_init(self):
        content.world.CellType.init_celltypes()
        
        self.assertEqual(content.world.CellType.path, utility.Path.get('celltypes'))
        
        self.assertEqual(content.world.CellType.default.name, 'Default')
        self.assertEqual(content.world.CellType.default.solid, False)
        self.assertEqual(content.world.CellType.default.opaque, False)
        self.assertEqual(content.world.CellType.default.tile, resource.Tile.default)
    
    def test_create_celltype(self):
        self.assertRaises(TypeError, content.world.CellType.create_celltype, None, True, True)
        self.assertRaises(TypeError, content.world.CellType.create_celltype, 'Test', None, True)
        self.assertRaises(TypeError, content.world.CellType.create_celltype, 'Test', True, None)
        
        cell_type1 = content.world.CellType.create_celltype('First', True, False)
        
        self.assertTrue(isinstance(cell_type1, content.world.CellType.CellType))
        self.assertEqual(cell_type1.name, 'First')
        self.assertEqual(cell_type1.solid, True)
        self.assertEqual(cell_type1.opaque, False)
        
        is_in = 'First' in content.world.CellType.celltypes
        self.assertTrue(is_in)
        if is_in:
            self.assertEqual(cell_type1, content.world.CellType.celltypes['First'])
    
    def test_get_celltype(self):
        content.world.CellType.init_celltypes()
        
        self.assertEqual(content.world.CellType.default, content.world.CellType.get_celltype('First'))
        self.assertEqual(content.world.CellType.default, content.world.CellType.get_celltype('Second'))
        
        cell_type1 = content.world.CellType.create_celltype('First', True, False)
        cell_type2 = content.world.CellType.create_celltype('Second', False, True)
        
        self.assertEqual(cell_type1, content.world.CellType.get_celltype('First'))
        self.assertEqual(cell_type2, content.world.CellType.get_celltype('Second'))
        
        self.assertEqual(content.world.CellType.default, content.world.CellType.get_celltype('Test'))
        self.assertEqual(content.world.CellType.default, content.world.CellType.get_celltype(None))
          

if __name__ == "__main__":
    unittest.main() 