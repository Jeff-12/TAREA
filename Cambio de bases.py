def aCadena(n,base):
    Tabla:"012345678"
    if n<base:
        return Tabla[n]
    else:
        return aCadena(n//base,base)+Tabla[n%base]
print(aCadena(12,2)) 