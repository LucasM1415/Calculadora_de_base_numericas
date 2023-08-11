#Decimal para binário#
def D_B(numero):
    numero = int(numero)
    ListaB = []
    while numero >= 2:
        ListaB.append(numero % 2)
        numero = numero // 2
    ListaB.append(numero)
    ListaB = ListaB[::-1]
    Resposta_binario = int(''.join(map(str, ListaB)))   
    return Resposta_binario

#Decimal para hexadecimal#
def D_H(numero):
    numero = int(numero)
    ListaH = []
    while numero > 0:
        Resto1 = numero % 16
        if Resto1 < 10:
            ListaH.append(Resto1)
        else:
            ListaH.append(chr(65 + (Resto1 - 10)))
        numero = numero // 16
    ListaH = ListaH[::-1]
    Resposta_hexadecimal = ''.join(map(str, ListaH))
    return Resposta_hexadecimal

#Decimal para octal
def D_O(numero):
    numero = int(numero)
    lista_octal = []
    while numero > 0:
        Resto2 = numero % 8
        if Resto2 < 8:
          lista_octal.append(Resto2)
        else:
          Resto2 = Resto2 + 2
          lista_octal.append(Resto2)          
        numero = numero // 8
    lista_octal = lista_octal[::-1]
    Resposta_octal = ''.join(map(str, lista_octal))
    return Resposta_octal

#Binario para decimal#
def B_D(numero):
    numero = str(numero)
    numero = list(numero)
    Resposta_decimal = 0
    for i in range(len(numero)):
        Resposta_decimal += int(numero[i]) * 2 ** (len(numero) - i - 1)
    return Resposta_decimal
    
#Hexadecimal para Decimal)
def H_D(numero):
    numero = str(numero)
    numero = list(numero)
    Resposta_decimal = 0
    for i in range(len(numero)):
        if numero[i].isalpha():
            Resposta_decimal += (ord(numero[i].upper()) - 55) * 16 ** (len(numero) - i - 1)
        else:
            Resposta_decimal += int(numero[i]) * 16 ** (len(numero) - i - 1)
    return Resposta_decimal

#Octal para decimal#
def O_D(numero):
    numero = str(numero)
    numero = list(numero)
    Resposta_decimal = 0
    for i in range(len(numero)):
        Resposta_decimal += int(numero[-i-1]) * 8**i
    return Resposta_decimal
O_D(175)

#Menu#
Numero = input("Informe o número a ser convertido: ")
Base = str(input("Informe a base atual do número: "))
Base = Base.lower()
while Base != "decimal" and Base != "binario" and Base != "hexadecimal" and Base != "octal":
  print("Informação invalida, tente: Decimal, Binario ou Hexadecimal")
  Base = input("Informe a base atual do número: ")
BaseR = str(input("Informe a base no qual deseja transformar o número: "))
BaseR = BaseR.lower()
while BaseR != "decimal" and BaseR != "binario" and BaseR != "hexadecimal" and BaseR != "octal":
  print("Informação invalida, tente: Decimal, Binario ou Hexadecimal")
  BaseR = str(input("Informe a base no qual deseja transformar o número: "))

if Base == BaseR:
  print("A base atal e a base convertida são a mesma, o número é: ", Numero)

elif Base == "decimal" and BaseR == "binario":
  print("O resultado é: ", (D_B(Numero)))
elif Base == "decimal" and BaseR == "hexadecimal":
  print("O resultado é: ", (D_H(Numero)))
elif Base == "decimal" and BaseR == "octal":
  print("O resultado é: ", (D_O(Numero)))
elif Base == "binario" and BaseR == "decimal":
  print("O resultado é: ", (B_D(Numero)))
elif Base == "hexadecimal" and BaseR == "decimal":
  print("O resultado é: ", H_D(Numero))
elif Base == "octal" and BaseR == "decimal":
  print("O resultado é: ", O_D(Numero))
elif Base == "binario" and BaseR == "octal":
  print("O resultado é: ", D_O(B_D(Numero)))
elif Base == "octal" and BaseR == "binario":
  print("O resultado é: ", D_B(O_D(Numero)))
elif Base == "binario" and BaseR == "hexadecimal":
  print("O resultado é: ", D_H(B_D(Numero)))
elif Base == "hexadecimal" and BaseR == "binario":
  print("O resultado é: ", D_B(H_D(Numero)))
elif Base == "octal" and BaseR == "hexadecimal":
  print("O resultado é: ", D_H(O_D(Numero)))
elif Base == "hexadecimal" and BaseR == "octal":
  print("O resultado é: ", D_O(H_D(Numero)))
else:
  print("Error")
