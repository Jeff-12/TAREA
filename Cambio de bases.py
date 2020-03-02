def aCadena(n,base):
    Tabla="012345678"
    if n<base:
         return Tabla[n]
    if base==0:
        return 0
    if base==1:
        return 1
    else:
        return aCadena(n//base,base)+Tabla[n%base]
print(aCadena(12,10)) 