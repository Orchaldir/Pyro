#!/usr/bin/env python

import unittest

import resource.Tile
import utility.Path

class TileTest(unittest.TestCase):
    
    def test_init(self):
        resource.Tile.init()
        
        self.assertEqual(resource.Tile.path, utility.Path.get('tiles'))
        self.assertEqual(resource.Tile.default.name, 'Default')
        self.assertEqual(resource.Tile.default.r, 255)
        self.assertEqual(resource.Tile.default.g, 0)
        self.assertEqual(resource.Tile.default.b, 255)
    
    def test_get(self):
        resource.Tile.init()
        
        self.assertEqual(resource.Tile.default, resource.Tile.get('Color'))
        self.assertEqual(resource.Tile.default, resource.Tile.get('Image'))
        
        color_tile = resource.Tile.create_color_tile('Color', 10, 20, 30, 40)
        image_tile = resource.Tile.create_image_tile('Image', 'test.png')
        
        self.assertEqual(color_tile, resource.Tile.get('Color'))
        self.assertEqual(image_tile, resource.Tile.get('Image'))
        
        self.assertEqual(resource.Tile.default, resource.Tile.get('Test'))
        self.assertEqual(resource.Tile.default, resource.Tile.get(None))
        

class CreateColorTileTest(unittest.TestCase):  
    
    def test_success(self):
        resource.Tile.init()
        color_tile = resource.Tile.create_color_tile('Color', 10, 20, 30, 40)
        
        self.assertTrue(isinstance(color_tile, resource.Tile.ColorTile))
        self.assertEqual(color_tile.name, 'Color')
        self.assertEqual(color_tile.r, 10)
        self.assertEqual(color_tile.g, 20)
        self.assertEqual(color_tile.b, 30)
        self.assertEqual(color_tile.a, 40)
        
        is_in = 'Color' in resource.Tile.tiles
        self.assertTrue(is_in)
        if is_in:
            self.assertEqual(color_tile, resource.Tile.tiles['Color'])

class CreateImageTileTest(unittest.TestCase):  
    
    def test_success(self):
        resource.Tile.init()
        image_tile = resource.Tile.create_image_tile('Image', 'test.png')
        
        self.assertTrue(isinstance(image_tile, resource.Tile.ImageTile))
        self.assertEqual(image_tile.name, 'Image')
        
        is_in = 'Image' in resource.Tile.tiles
        self.assertTrue(is_in)
        if is_in:
            self.assertEqual(image_tile, resource.Tile.tiles['Image'])


if __name__ == "__main__":
    unittest.main()   