#Papa Kojo Oseku-Afful

import random

class Deque:
    def __init__(self):
        self.data = []
        
    
    def InsertFront(self, other):
        self.data.insert(0, other)
        
    
    def RemoveFront(self):
        if self.data == []:
            return ("Array is empty")
        else:
            self.data.pop(0)
            
    def Insertback(self, other):
         self.data.append(other)
         
     
    def RemoveBack(self):
         if self.data == []:
             return (" Array is empty")
         else:
            self.data.pop()
            
            
    def displaydata (self):
        return self.data
    
    def length(self):
        if self.data == []:
            return ("Array is null")
        else:
            return len(self.data)
     
    def isfull(self):
        return len(self.data) == 20    
    
   
   
    def isempty(self):
        return self.data == []
    
    
    
    def top_front(self):
        return self.data[0]
    
    
    def top_back(self):
        return self.data[-1]

de= Deque()
    


N = 20
for i in range(N//2):
    array1= random.randint(1,100)
    de.Insertback(array1)
    
number = random.uniform(0,1)
print(number)
if number > 0 and number <= 0.1:
    x= random.randint(1,100)
    print(x)
    d.InsertFront(x)
    
if number >0.1 and number <= 0.3:
    x = random.randint(1,100)
    print(x)
    d.RemoveFront()
    
if number > 0.3 and number <= 0.4:
    x= random.randint(1,100)
    print(x)
    d.AInsertback(method)
    
if number > 0.4 and number <= 1:
    x = random.randint(1,100)
    print(x)
    de.RemoveBack()
    

if number >0 and number <= 0.1:
    x = random.randint(1,100)
    print(x)
    de.InsertFront(x)
    
if number >0.1 and number <= 0.7:
    x= random.randint(1,100)
    print(x)
    de.RemoveFront()
    
if number >0.7 and number <= 0.8:
    x= random.randint(1,100)
    print(x)
    de.Insertback(x)
    

if number >0.8 and number <= 1:
    x= random.randint(1,100)
    print(x)
    de.RemoveBack()
    
print(de.displaydata())
print(de.length())
print(de.isempty())
print(de.isfull())

