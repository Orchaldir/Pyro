#!/usr/bin/env python

class Consume:
    
    def __init__(self, consumer, consumable):
        self.consumer = consumer
        self.consumable = consumable
    
    def execute(self):
        self.consumable.components['Consumable'].use(self.consumer)
        self.consumable.remove()
        return True

def can_consume(consumer, consumable):
    if 'Controller' in consumer.components and 'Consumable' in consumable.components:   
        consumer.components['Controller'].action = Consume(consumer, consumable)
        return True
        
    return False