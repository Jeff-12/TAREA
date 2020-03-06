def aCadena(n,base):
    Tabla="012345678"
    if n<base:
         return Tabla[n]
    else:
        return aCadena(n//base,base)+Tabla[n%base]
def test_aCadena():
    assert aCadena(10,5)==20
    assert aCadena(20,7)==26
print(aCadena(23,10))
print(aCadena(14,6))


def cambio(a,b):
    return cambio_aux(a,b,0,0)
def cambio_aux(a,b,n,m):
    if a>0:
        return cambio_aux(a//10,b,n+1,((a%10)*(b**n))+m)
    else:
        return m
def test_cambio():
    assert cambio(13,8)==11
    assert cambio(20,6)==12
print (cambio(1010001110,2))
print (cambio(3201,4))