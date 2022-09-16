#Escribir un programa que pida 2 nC:meros y muestre paso a paso el cC!lculo de la raC-z cuadrada de la suma del cuadrado de ambos.
import math
num1=int(input('ingrese primer número: '))
num2=int(input('ingrese segundo número: '))
#Luego procedemos a esperar la multiplicacion de los numeros al cuadrado
print ('√','(',(num1),')^2','+','(',(num2),')^2','=')
pot1 = (num1**2)
pot2 = (num2**2)
#luego se suman ambos numeros a su respectiva potencia
sumapot = (num1**2) + (num2**2)
#luego se imprime el resultado de la suma de estos numeros
print ('√','(',(pot1),'+',(pot2),')','=')
print ('√',(sumapot),'=')
#para acabar se ve el resultado y la raiz de este
resutado = ((num1**2)+(num2**2))
raíz = math.sqrt(resutado)
print ((raíz))
#finally
