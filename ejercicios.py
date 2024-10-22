def calculoIVA(precio, porcentaje):
    pFinal =float( ((precio*porcentaje) / 100)+precio )
    return pFinal

def calculoDescuento(precio2,porcentaje2):
    montDesc =float( (precio2*porcentaje2) / 100)
    p_final = float(precio2-montDesc)
    return p_final

def costoTotalCompra(precio,cantProd):
    return float( precio * cantProd  )