#print(randInt())   
import random
def randInt(min= 0  , max= 100  ):
    num = random.random()*100
    return round(num) 
print(randInt())

#print(randInt(max=50)) 

import random
def randInt( max= 50  ):
    num = random.random()*50
    return round(num) 
print(randInt(max=50 ))

#print(randInt(min=50))

def randInt( min= 50, max=100 ):
    num = random.random()*50
    return round(num) 
print(randInt( min=50 ))

#print(randInt(min=50, max=500))
def randInt(min=10, max=30):
    num = random.random() * (max - min) + min 
    return round(num)

print(randInt(min=10, max=30))


#print(randInt())             # should print a random integer between 0 to 100
#print(randInt(max=50))         # should print a random integer between 0 to 50
#print(randInt(min=50))         # should print a random integer between 50 to 100
#print(randInt(min=50, max=500))    # should print a random integer between 50 and 500