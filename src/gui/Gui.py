#!/usr/bin/env python

import pygame

import gui.widgets.EquipmentSlots
import gui.widgets.InventoryList
import gui.widgets.Label
import gui.widgets.MapViewer
import gui.widgets.TileViewer
import utility.Path

guis = {}
path = None

class Gui:
    
    def __init__(self, name, surface=None):
        self.name = name
        
        if isinstance(surface, pygame.Surface):
            self.surface = surface
        else:
            self.surface = None
        
        self.widgets = {}
    
    def add_widget(self, widget):
        self.widgets[widget.name] = widget
    
    def draw(self):
        if self.surface is not None:
            for widget in self.widgets.values():
                widget.draw(self.surface)
    
    def get_widget(self, name):
        if name in self.widgets:
            return self.widgets[name]
            
    def load(self, filename):
        global path
        
        file = open(utility.Path.join(path, filename), 'r')
        
        line = file.readline().split()
    
        number = int(line[0])
    
        for i in range(number):
            line = file.readline().split()
        
            if line[0] == 'Label':
                widget = gui.widgets.Label.load(line[1], file)
            elif line[0] == 'MapViewer':
                widget = gui.widgets.MapViewer.load(line[1], file)
            elif line[0] == 'TileViewer':
                widget = gui.widgets.TileViewer.load(line[1], file)
            elif line[0] == 'InventoryList':
                widget = gui.widgets.InventoryList.load(line[1], file)
            elif line[0] == 'EquipmentSlots':
                widget = gui.widgets.EquipmentSlots.load(line[1], file)            
            if widget is not None:
                self.add_widget(widget)
                widget = None
                
        file.close()
    
    def on_button_1_down(self, x, y):
        for widget in self.widgets.values():
            if widget.on_button_1_down(x, y):
                return
    
    def on_button_1_up(self, x, y):
        for widget in self.widgets.values():
            if widget.on_button_1_up(x, y):
                return
    
    def on_button_2_down(self, x, y):
        for widget in self.widgets.values():
            if widget.on_button_2_down(x, y):
                return
    
    def on_button_2_up(self, x, y):
        for widget in self.widgets.values():
            if widget.on_button_2_up(x, y):
                return
    
    def save(self, filename):
        global path
        
        file = open(utility.Path.join(path, filename), 'w')
        
        file.write('%d\n' % (len(self.widgets)))
    
        for widget in self.widgets.values():
            widget.save(file)
                
        file.close()


def init():
    global guis, path
    
    guis = {}
    path = utility.Path.get('gui') 

def get_gui(name):
    global guis
    
    if name in guis:
        return guis[name]

def load_gui(name, filename, surface):
    global guis
    
    gui = get_gui(name)
    
    if gui is None:
        gui = Gui(name, surface)
        guis[name] = gui
        
    gui.load(filename)
    
    return gui