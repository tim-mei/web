import random
from pprint import pprint

f = open('mones.csv')
f2 = f.read()
f2 = f2.strip()

def listing(a):
    vals = []
    z = a.find('\n')
    sec = a[z+1:].split('\n') 
    for x in sec:
        g = []
        g.append(x)
        vals.append(g)
    return vals

f2a = listing(f2)

def prep(a):
    prepping = []
    a1 = random.choice(a)
    a2 = random.choice(a)
    while a2 == a1:
        a2 = random.choice(a)
    for x in a1:
        prepping.append(x)
    for y in a2:
        prepping.append(y)
    return prepping

val2 = prep(listing(f2))

def final_lists(a):
    listt = []
    for x in a:
        g = x.split(',')
        z = []
        y = 0
        while y < 20:
            z.append( (1 * ((1 + (float(g[1]) / int(g[2]) )) ** (y * int(g[2])))) * int(g[0]) )
            y += 1
        listt.append(z)
        y = 0
    return listt

pprint(val2)
print(final_lists(val2))

            
        
            
            



