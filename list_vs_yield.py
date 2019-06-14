#create python functions which will Generate cube volumes of size (1-10) in a list using
#1. generator, 2.generator with yield for lazy evaluation

def cube(n):
    return n**3

def simpleGenerator(n):
    resultslist=[]
    i=1
    while i<=n:
        resultslist.append(cube(i))
        i+=1
    return resultslist


#Lazy Evaluation using Yield
#This will not return a list, rather single Generator objects

def lazyGenerator(n):
    i=1
    while i<=n:
        yield cube(i)
        i+=1

#Using the simple generator, we start with 1-10 and we generate x^3 resulting list using simple generator
print ("List of 1-10 volume:")
print (simpleGenerator(10))

#Using lazyGenerator using yield. Only the generator object will be returned
lazyResultList = lazyGenerator(10)

#We compute and display the values from the generator object
print ("List")
print ([i for i in lazyResultList])
