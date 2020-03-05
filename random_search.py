from random import random
def random_list(minmax):
    l=[minmax[0]+((minmax[1]-minmax[0])*random()) for i in range(len(minmax))]
    return l

def objective_function(l):
    return min([(i**2)-(2*i)-1 for i in l])

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


k=[[i,objective_function([i])] for i in range(-10,10)]
k=sorted(k,key=lambda x:x[1])
expected_near=k[0][1]

all=[]

for space in spaces:
    s=search(space,iterations)
    try:
        if(s['cost']<best['cost']):
            best=s
    except:
        best=s
    print(space,best['cost'])
    all.append(abs(best['cost']-expected_near)**2)
print()
print(best)

actual=best['cost']
print()
print(expected_near,actual)
print('Squared Error = ',abs(expected_near-actual)**2)
print('MSE = ',sum(all)/len(all))
