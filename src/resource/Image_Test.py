#!/usr/bin/env python

import unittest

import resource.Image
import utility.Path

class ImageTest(unittest.TestCase):
    
    def test_init(self):
        resource.Image.init()
        self.assertEqual(resource.Image.path, utility.Path.get())


if __name__ == "__main__":
    unittest.main()   