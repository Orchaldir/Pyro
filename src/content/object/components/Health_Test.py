#!/usr/bin/env python

import unittest

from content.object.components.Health import Health, HealthTemplate

class CharacterTest(unittest.TestCase):
    
    def setUp(self):
        self.template = HealthTemplate(5)
    
    def test_damage(self):
        char = Health(self.template)
        
        self.assertEquals(char.damage(-1), 0)        
        self.assertEquals(char.health, 5)
        
        self.assertEquals(char.damage(1), 1)        
        self.assertEquals(char.health, 4)
        
        self.assertEquals(char.damage(2), 2)        
        self.assertEquals(char.health, 2)
        
        self.assertEquals(char.damage(3), 2)        
        self.assertEquals(char.health, 0)
        
        self.assertEquals(char.damage(4), 0)        
        self.assertEquals(char.health, 0)
        
        self.assertEquals(char.damage(-1), 0)        
        self.assertEquals(char.health, 0)
    
    def test_get_type(self):
        char = Health(self.template)
        self.assertEquals(char.get_type(), 'Health')   
    
    def test_heal(self):
        char = Health(self.template)
        char.health = 1
        
        self.assertEquals(char.heal(-1), 0)        
        self.assertEquals(char.health, 1)
        
        self.assertEquals(char.heal(2), 2)        
        self.assertEquals(char.health, 3)
        
        self.assertEquals(char.heal(3), 2)        
        self.assertEquals(char.health, 5)
        
        self.assertEquals(char.heal(4), 0)        
        self.assertEquals(char.health, 5)
        
        self.assertEquals(char.heal(-1), 0)        
        self.assertEquals(char.health, 5)     
    
    def test_is_alive_death(self):
        char = Health(self.template)
        
        self.assertTrue(char.is_alive())
        self.assertFalse(char.is_death())
        
        char.health = 4     
        self.assertTrue(char.is_alive())
        self.assertFalse(char.is_death())
        
        char.health = 3     
        self.assertTrue(char.is_alive())
        self.assertFalse(char.is_death())
        
        char.health = 2    
        self.assertTrue(char.is_alive()) 
        self.assertFalse(char.is_death())
        
        char.health = 1   
        self.assertTrue(char.is_alive())  
        self.assertFalse(char.is_death())
        
        char.health = 0     
        self.assertFalse(char.is_alive())
        self.assertTrue(char.is_death())