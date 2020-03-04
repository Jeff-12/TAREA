def cambio(a,b):
    return cambio_aux(a,b,0,0)
def cambio_aux(a,b,p,c):
    if a>0:
        return cambio_aux(a//10,b,p+1,((a%10)*(b**p))+c)
    else:
        return c
print (cambio(1010001110,2))