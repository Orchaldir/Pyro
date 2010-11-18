#!/usr/bin/env python

import os.path
import sys

path = ''

def create():
    global path
    #print 'sys.argv[0] =', sys.argv[0]             
    pathname = os.path.dirname(sys.argv[0])        
    #print 'path =', pathname
    abs_path =  os.path.abspath(pathname)
    #print 'full path =',abs_path
    parts =  abs_path.rsplit(os.path.sep, 1)
    #print 'parts =',parts
    path =  os.path.join(parts[0], 'data')
    print 'path =',path
    
def get(sub_path=None):
    global path
    
    if sub_path is None:
        return path
    else:
        return os.path.join(path, sub_path)

def join(path, sub_path):
    return os.path.join(path, sub_path)