import random

import time

start = time.time()


Uniform_rn = range(1,32767)

arraydata = random.sample(Uniform_rn, k = 5000)

arraydata.sort()

print(arraydata)

N = len(arraydata)

def Binary_Search(arraydata, low, high, target):
     if high >= low:
        mid = (high + low) // 2
        
        if target == arraydata[mid]:
         return mid
        
        elif arraydata[mid] > target:
         return Binary_Search(arraydata, low, mid -1,target )
        
        else:
         return Binary_Search(arraydata, mid + 1, high,target )
     else:
         return-1
        
def Interpolation_Search(arraydata, low, high, target):
     if high >= low:
       pos =low + ((high-low) * (target- arraydata[low]) //(arraydata[high]-arraydata[low]))
       
       if target == arraydata[pos]:
           return pos
       
       elif arraydata[pos] > target:
           return BinarySearch(arraydata,target, low, pos -1 )
        
       else:
           return Binary_Search(arraydata,target, pos + 1, high)
     
     else:
         return-1
    
length = len(arraydata) - 1

element = Binary_Search(arraydata, 0, length, 1100)

if element != -1:
    
    print("\nElement has been found" , element)
    

else:
    print("\nElement not found.")
    

end = time.time()

print ("\nTime in msec = %.6f seconds" %(end - start))