# input

pre_art = int(input("Ingrese el precio del articulo: "))

# processing
if pre_art<3000:
    ganancia = pre_art*0.15
    pre_ven = pre_art + ganancia 
else: 
    if pre_art<6000:
        ganancia = 500
        pre_vent = pre_art + ganancia
    else:
        ganancia = pre_art*0.25
        pre_vent = pre_art + ganancia

print ("El precio de venta es :" + str (pre_vent))