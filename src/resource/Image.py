#!/usr/bin/env python

import pygame

import utility.Path

path = ''

def init():
    global path
    
    path = utility.Path.get()

def load(name):
    global path
    
    return pygame.image.load(utility.Path.join(path, name))
    