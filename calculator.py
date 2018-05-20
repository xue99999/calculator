#!/usr/bin/env python3

import sys
import csv

class Args():
    
    def __init__(self):
        l = sys.argv[1:]
        self.c = l[l.index('-c')+1]
        self.d = l[l.index('-d')+1]
        self.o = l[l.index('-o')+1]

args = Args()


class Config(object):
    
    def __init__(self):
        self.config = self._read_config()

    def _read_config(self):
        config = {'s': 0}
        with open(args.c) as f:
            for line in f.readlines():
                key,value = line.split('=')
                key = key.strip()
                value = float(value.strip())
                if value > 1:
                    config[key] = value
                else:
                    config['s'] += value
        return config

config = Config().config

print(config)


