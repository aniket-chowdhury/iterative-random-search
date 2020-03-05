from random import random
def random_list(minmax):
    l=[minmax[0]+((minmax[1]-minmax[0])*random()) for i in range(len(minmax))]
    return l

def objective_function(l):
    return sum([(i**2)+(2*i) for i in l])

def search(space,iterations):
    best={}
    for i in range(iterations):
        d={}
        d['list']=random_list(space)
        d['cost']=objective_function(d['list'])
        try:
            if(d['cost']<best['cost']):
                best=d
        except:
            best=d
    return best

from random import randint
iterations=100

spaces=[[randint(-10,10) for i in range(2)]for i in range(10)]

for space in spaces:
    s=search(space,iterations)
    try:
        if(s['cost']<best['cost']):
            best=s
    except:
        best=s
    print(space,best['cost'],objective_function([best['cost']]))
print(best)

print([[i,objective_function([i])] for i in range(-10,10)])
