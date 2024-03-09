
def iloczyn(x,y):
   
   
    if y == 1:
        return"Wynikiem jest:", x 
    else:
        k = y//2
        z = x*k
        if y% 2 == 0:
            return "Wynikiem jest", z+z
        else:
            return "wynikiem jest ", x + z + z
        

iks = 10

igrek = 45



szubidubi = iloczyn(iks,igrek)
print(szubidubi)

def iteracja(x,y):
    z = 0 
    while y >= 1:
        if y %2 ==1:
            z+=x
        x += x
        y //= 2
    return z

iteracja(iks,igrek)



