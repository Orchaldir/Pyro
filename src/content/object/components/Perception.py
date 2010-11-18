#!/usr/bin/env python

class Sound:
    
    def __init__(self, x, y, loudness=1.0):        
        self.x = x
        self.y = y 
        self.loudness = loudness  


class PerceptionTemplate:
    
    def __init__(self, vision_radius=0, min_loudness=0.0):
        self.vision_radius = vision_radius
        self.min_loudness = min_loudness
    
    def load(self, file):
        line = file.readline().split()
    
        for i in range(int(line[0])):
            line = file.readline().split()
            
            if line[0] == 'vision_radius':
                self.vision_radius = int(line[1])
            elif line[0] == 'min_loudness':
                self.min_loudness = float(line[1])
    
    def save(self, file):
        pass


class Perception:
    
    def __init__(self, template):
        self.object = None
        self.sound = None
        self.template = template         
    
    def add_sound(self, x, y, loudness, generators):
        #if self.object in generators:
        #    return
        
        distance = self.object.body.get_distance(x, y)
        new_loudness = loudness - distance * 0.02
        
        if new_loudness > self.get_min_loudness():
            print ' ' + self.object.id + ' heard sound : ' + str(new_loudness)
            
            if self.sound is None or new_loudness > self.sound.loudness:
                self.sound = Sound(x, y, new_loudness)
    
    def get_enemies(self):
        if self.object.body is not None and 'Character' in self.object.components:
            body = self.object.body
            
            if body.map is not None:
                character = self.object.components['Character']
                enemies = []                        
                
                for obj in body.map.objects.values():
                    
                    if 'Character' in obj.components and obj.body is not None and obj is not self.object:
                        
                        if character.is_enemy(obj.components['Character']):                            
                            distance = body.get_distance_to_body(obj.body)
                            
                            if distance < self.get_vision_radius():
                                enemies.append((distance, obj))
                
                def compare(a, b):
                    return cmp(a[0], b[0])
                
                enemies.sort(compare)
                
                return map(lambda x: x[1], enemies)
        
        return []
    
    def get_min_loudness(self):
        return self.template.min_loudness
    
    def get_type(self):
        return 'Perception'
    
    def get_vision_radius(self):
        return self.template.vision_radius
    
    def update(self, obj):
        if self.sound is not None:
            self.sound.loudness = self.sound.loudness - 0.001
            #print ' v : ' + str(self.loudness)
            if self.sound.loudness <= self.get_min_loudness() + 0.001:
                self.sound = None
            