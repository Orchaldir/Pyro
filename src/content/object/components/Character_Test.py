#!/usr/bin/env python

import unittest

from content.object.components.Character import Character, CharacterTemplate

class CharacterTest(unittest.TestCase):
    
    def setUp(self):
        self.good = CharacterTemplate('Good')
        self.bad = CharacterTemplate('Bad')
    
    def test_get_type(self):
        char = Character(self.good)
        self.assertEquals(char.get_type(), 'Character')
    
    def test_is_enemy(self):
        char0 = Character(self.good)
        char1 = Character(self.good)
        char2 = Character(self.bad)
        char3 = Character(self.bad)
        
        self.assertFalse(char0.is_enemy(char1))
        self.assertTrue(char0.is_enemy(char2))
        self.assertTrue(char2.is_enemy(char0))
        self.assertFalse(char2.is_enemy(char3))
        
        