a=[1,2,2]
b=[1]

def array_diff(a, b):
   b = [x for x in a if x not in b]
   return b
    
    

print(array_diff(a,b))