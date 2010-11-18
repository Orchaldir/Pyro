#!/usr/bin/env python

import pygame
from pygame.locals import *

from ai.behavior.Behavior import init_behaviors
from content.actions.Attack import can_attack
from content.actions.Consume import can_consume
from content.actions.Move import can_move
from content.actions.PickUp import can_pick_up
from content.actions.Wait import can_wait
from content.object.Object import get_object
from content.object.Template import init_templates
from content.object.components.controllers.Player import Player
from content.world.Map import init_maps, load_map
from content.world.CellType import init_celltypes
import gui.Gui
import resource.Image
import resource.Tile
from utility.Function import add_function
import utility.Input
import utility.Path


running = True
map = None
hero = None

def quit():
    global running
    running = False   

def attack(cell):
    global hero
    
    if hero.components['Health'].is_alive():
        for obj in cell.objects:
            if can_attack(hero, obj):
                return

def move(direction):
    global hero
    
    can_move(hero, direction)

def sound(cell):
    global map
    
    map.add_sound(cell.x, cell.y, 0.5)

def use():
    global hero
    
    active_gui = gui.Gui.get_gui('main')
    inv = active_gui.get_widget('Inventory')
    obj = inv.get_active()
    
    if obj is not None:               
        if 'Equipment' in obj.components:
            slots = hero.components['EquipmentSlots']
            
            if slots.is_equipped(obj):
                slots.unequip(obj)
            else:
                slots.equip(obj)   
        elif 'Consumable' in obj.components:   
            can_consume(hero, obj)


def main():
    global map, hero
    
    pygame.init()
    screen = pygame.display.set_mode((1400, 1100))
    pygame.display.set_caption('Pyro 0.0.07')
    
    utility.Path.create()
    
    add_function('Quit', quit)    
    add_function('Use', use)
    add_function('Wait', lambda: can_wait(hero))
    add_function('PickUp', lambda: can_pick_up(hero))
    add_function('Up', lambda: move(2))
    add_function('Down', lambda: move(0))
    add_function('Left', lambda: move(3))
    add_function('Right', lambda: move(1))
    
    utility.Input.bind_key_up(K_ESCAPE, 'Quit')
    utility.Input.bind_key_up(K_e, 'Use')
    utility.Input.bind_key_up(K_p, 'PickUp')
    utility.Input.bind_key_up(K_SPACE, 'Wait')
    utility.Input.bind_key_up(K_UP, 'Up')
    utility.Input.bind_key_up(K_DOWN, 'Down')
    utility.Input.bind_key_up(K_LEFT, 'Left')
    utility.Input.bind_key_up(K_RIGHT, 'Right')
    utility.Input.bind_key_up(K_w, 'Up')
    utility.Input.bind_key_up(K_s, 'Down')
    utility.Input.bind_key_up(K_a, 'Left')
    utility.Input.bind_key_up(K_d, 'Right')
    
    resource.Image.init()    
    resource.Tile.init('tiles.txt')    
    init_celltypes('cell_types.txt')    
    init_behaviors('behaviors.txt')
    init_templates('templates.txt')      
    
    init_maps()
    map = load_map('test', 'map.txt')
    
    hero = get_object('Hero_0')
    hero.add_component(Player())
    
    gui.Gui.init()
    active_gui = gui.Gui.load_gui('main', 'pyro.txt', screen)
    utility.Input.add_mouse_listener(active_gui) 
    
    active_gui.get_widget('MapViewer').on_b1_up = attack
    active_gui.get_widget('MapViewer').on_b2_up = sound
    label_hp = active_gui.get_widget('HP')
    label_damage = active_gui.get_widget('Damage')
    
    char = hero.components['Character']
    health = hero.components['Health']
    
    clock = pygame.time.Clock()
    
    while running:
        clock.tick(5)
        utility.Input.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == KEYDOWN:
                utility.Input.on_key_down(event.key)
            elif event.type == KEYUP:
                utility.Input.on_key_up(event.key)
            elif event.type == MOUSEBUTTONUP:
                utility.Input.on_mouse_up(event.button, event.pos[0], event.pos[1])
            elif event.type == MOUSEBUTTONDOWN:
                utility.Input.on_mouse_down(event.button, event.pos[0], event.pos[1])
        
        map.update()
        
        label_hp.set_text('%d / %d' % (health.get_health(), health.get_max_health()))
        label_damage.set_text('%d / %d' % (char.get_weapon_damage(), char.get_armor()))
            
        screen.fill((50, 50, 50))
        
        active_gui.draw()
        
        pygame.display.flip()

if __name__ == '__main__': main()