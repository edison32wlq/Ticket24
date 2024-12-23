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

def encontrarMayor(num1,num2,num3):
    mayorActual = num1
    if mayorActual < num2:
        mayorActual = num2
    if mayorActual < num3:
        mayorActual = num3
    return mayorActual

def encontrarMenor(num1,num2,num3,num4):
    menorActual = num1
    if menorActual > num2:
        menorActual = num2
    if menorActual > num3:
        menorActual = num3
    if menorActual > num4:
        menorActual = num4
    return menorActual
    
def calcularCuota(monto, interesAnual, numeroMeses):
    interesMensual = (interesAnual/12)/100  
    cuotaMensual = (monto*interesMensual)/(1-(1+interesMensual)**(-numeroMeses))
    return cuotaMensual

def calcularEdad(añonacimiento):
    añoactual = 2024  
    if añonacimiento > añoactual:
        return -1
    elif añonacimiento < 0:
        return -1
    else:
        return añoactual - añonacimiento

resultado1 = calcularEdad(2050)
if resultado1 == -1:
    print("Año nacimiento: 2050 => Usted aun no nace, o nació antes de cristo")

resultado2 = calcularEdad(-10)
if resultado2 == -1:
    print("Año nacimiento: -10 => Usted aun no nace, o nació antes de cristo")

resultado3 = calcularEdad(2024)
print(f"Año nacimiento: 2024 => Este año cumple {resultado3} años")

resultado4 = calcularEdad(2013)
print(f"Año nacimiento: 2013 => Este año cumple {resultado4} años")
