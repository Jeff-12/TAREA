def aCadena(n,base):
    Tabla="012345678"
    if n<base:
         return Tabla[n]
    else:
        return aCadena(n//base,base)+Tabla[n%base]
print(aCadena(12,10)) 
def cambio(a,b):
    return cambio_aux(a,b,0,0)
def cambio_aux(a,b,n,m):
    if a>0:
        return cambio_aux(a//10,b,n+1,((a%10)*(b**n))+m)
    else:
        return m
print (cambio(1010001110,2))