#!/usr/bin/env python3

import sys
import csv
from multiprocessing import Process, Queue

q1= Queue()
q2= Queue()

class Args():
    
    def __init__(self):
        l = sys.argv[1:]
        self.c = l[l.index('-c')+1]
        self.d = l[l.index('-d')+1]
        self.o = l[l.index('-o')+1]



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


'''
class UserData(object):
    
    def __init__(self):
        self.userdata = self._read_users_data()

    def _read_users_data(self):
        with open(args.d) as f:
            data = list(csv.reader(f))
        return data
'''

def read_users_data(q):    
    with open(args.d) as f:
        data = list(csv.reader(f))
    q.put(data)

def get_all(q1, q2):
    userdata =  q1.get()
    users_data = []
    
    for id, salary in userdata:
         
        salary = int(salary)
        shebao = salary * config['s']
        if salary < config['JiShuL']:
            shebao = config['JiShuL'] * config['s']
        if salary > config['JiShuH']:
            shebao = config['JiShuH'] * config['s']
        money = salary - shebao - 3500
        if money <= 0:
            m = 0
        elif money <= 1500:
            m = money * 0.03
        elif money <= 4500:
            m = money * 0.1 - 105
        elif money <= 9000:
            m = money * 0.2 - 555
        elif money <= 35000:
            m = money * 0.25 - 1005
        elif money <= 55000:
            m = money * 0.3 - 2755
        elif money <= 80000:
        	m = money * 0.35 - 5505
        else:
        	m = money * 0.45 - 13505

        users_data.append([id, salary, format(shebao, '.2f'),
            format(m, '.2f'), format(salary-shebao-m, '.2f')]) 

    q2.put(users_data)



def write_datas(q2):
    userdata = q2.get()
    with open(args.o, 'w') as f:
        for line in userdata:
            csv.writer(f).writerow(line)



if __name__ == '__main__':

    args = Args()

    config = Config().config
    
    Process(target=read_users_data, args=(q1,)).start() 
    Process(target=get_all, args=(q1,q2)).start() 
    Process(target=write_datas, args=(q2,)).start() 

