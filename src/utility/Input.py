#!/usr/bin/env python

from utility.Function import get_function

keys_down_action = {}
keys_up_action = {}
mouse_listeners = []

keys_up = []

def init():
    global keys_down_action, keys_up_action, mouse_listeners
    
    keys_down_action = {}
    keys_up_action = {}
    mouse_listeners = []

def update():
    global keys_up
    
    keys_up = []

"""keys"""
    
def bind_key_down(key, action):
    global keys_down_action
    
    keys_down_action[key] = action

def bind_key_up(key, action):
    global keys_up_action
    
    keys_up_action[key] = action

def is_key_up(key):
    global keys_up
    return key in keys_up   

def on_key_down(key):
    global keys_down_action
    
    if key in keys_down_action:
        action_id = keys_down_action[key]
        action = get_function(action_id)
        if action is not None:
            print 'down : ' + str(key) + ' -> ' + action_id
            action()

def on_key_up(key):
    global keys_up_action, keys_up
    
    keys_up.append(key)
    
    if key in keys_up_action:
        action_id = keys_up_action[key]
        action = get_function(action_id)
        if action is not None:
            print 'up : ' + str(key) + ' -> ' + action_id
            action()

"""mouse"""

def add_mouse_listener(listener):
    global mouse_listeners
    
    mouse_listeners.append(listener)

def on_mouse_down(button, x, y):
    global mouse_listeners
    
    if button is 1:
        for listener in mouse_listeners:
            listener.on_button_1_down(x, y)
    elif button is 3:
        for listener in mouse_listeners:
            listener.on_button_2_down(x, y)

def on_mouse_up(button, x, y):
    global mouse_listeners
    
    if button is 1:
        for listener in mouse_listeners:
            listener.on_button_1_up(x, y)
    elif button is 3:
        for listener in mouse_listeners:
            listener.on_button_2_up(x, y)

