#!/usr/bin/env python

functions = {}

def init():
    global functions
    
    functions = {}

def add_function(id, function):
    global functions
    
    functions[id] = function
    
def get_function(id):
    global functions
    
    if id in functions:
        return functions[id]
    else:
        return None