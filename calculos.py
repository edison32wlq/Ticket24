def determinarResultadosIMC(imc):
    if imc >= 0 and imc < 16:
        res = "Delgades severa"
    elif imc >= 16 and imc < 17:
        res = "Delgadez moderada"
    elif imc >=17 and imc < 18.5:
        res = "Delgadez leve"
    elif imc >= 18.5 and imc < 25:
        res = "Peso normal"
    elif imc >= 25 and imc < 30:
        res = "Sobrepeso"
    elif imc >= 30 and imc < 35:
        res = "Obesidad Grado 1"
    elif imc >= 35 and imc < 40:
        res = "Obesidad Grado 2"
    elif imc >= 40:
        res  = "Obesidad Grado 3"
    else:
        res = "IMC fuera del rango"
    
    return res

