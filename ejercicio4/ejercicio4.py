# Programa para calcular imc

print ("-------------------------------------")
print ("----Programa para calcular el IMC----")
print ("-------------------------------------")

# input

peso = int(input("Digite su peso en kg: "))
altura = float(input("Digite su altura en metros: "))

# processing

imc = peso/altura**2

if imc < 16:
    msj = ("Criterio de ingreso en hospital")
else:
    if imc < 17:
        msj = (" Infrapeso")
    else:
        if imc < 18:
            msj = ("Bajo peso")
        else:
            if  imc < 25:
                msj = ("Peso saludable")
            else:
                if imc < 30:
                    msj = ("Sobrepeso (obesidad de grado I)")
                else:
                    if imc < 35:
                        msj = ("Sobrepreso crónico (obesidad de grado II)")
                    else:
                        if imc < 40:
                            msj = ("Obesidad premórbida (obesidad de grado III)")
                        else:
                            if imc > 40:
                                msj = ("Obesidad mórbida (obesidad de grado IV)")
                            else:
                                msj = ("Obesidad mórbida (obesidad de grado IV)")
#output

print ("Su índice de masa corporal es " +  str(imc))
print (msj)