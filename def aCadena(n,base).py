def aCadena(n,base)
    if n<base:
        return n
    else:
        return aCadena(n//base,base)+(n%base]
print(aCadena(12,2)) 