# lista=[10, 11, 12, 13, 14, 15]
# for valor in lista:
#    print(valor)

# for valor in range (5):
#     print (valor)

# for valor in range (4, 8):
#     print (valor)

# texto = "Python"
# for caracter in texto:
#     print (caracter)

# frase = "A ligeira raposa marrom ataca o cão preguiçoso"
# qtdeLetras = 0
# for letra in frase:
#     qtdeLetras += 1
# print ("A frase possui " + str(qtdeLetras) + " letras.")

#dados = [1, 3, 5, 8, 10, 2]
#soma = 0
#qtde = 0
#for valor in dados:
#    soma += valor
#    qtde += 1
#
#print(soma)
#print(qtde)
#
#media = soma/qtde
#
#print(media)

#soma=0
#for numero in range(10):
#    if (numero % 2)==0:
#        soma += numero
#print(soma)

#noVerificados=0
#noMultiplos=0
#for numero in range(20):
#    noVerificados+=1
#    if (numero % 3)==0:
#        noMultiplos+=1
#
#print(noVerificados)
#print(noMultiplos)


#numero=int(input("Digite o número que se deseja determinar o fatorial:"))
#fatorial=1
#for termo in range (1, (numero+1)):
#    fatorial *= termo
#
#print("O fatorial de "+ str(numero) + "! é igual a " + str(fatorial))


#A = [2, 3, 4]
#B = [7, -3, 2]
#C=[]
#
#for indice in range (3):
#    C.append(A[indice] + B[indice])
#
#print(C)


# numPrimos = []
# for numero in range(20):
#     div=0
#     for divisor in range (1, numero+1):
#         if (numero %divisor)==0:
#             div += 1
#     if div == 2:
#         numPrimos.append(numero)
#
# print(numPrimos)

# a=10.50
# b=a%4
# print(b)

# varA=3
# varB=0
# for num in range (varA):
#     varB += num ** 2
#
# print (varB)

#
# dados = [[1,2,3],[4,5,6],[7,8,9]]
# for linha in dados:
#     for coluna in linha:
#         print(coluna)

#
# tabela=[]
# contador=1
# for linha in range(3):
#     linha=[]
#     for coluna in range(3):
#         linha.append(contador)
#         contador+=1
#     tabela.append(linha)
# print(tabela)

#
# for numerador in range (10):
#     print("Tabuada do número", numerador + 1)
#     for multiplicador in range (10):
#         print ((numerador + 1)*(multiplicador + 1))

tabela=[]
contador = 0
for linha in range(3):
    linha = []
    for coluna in range (3):
        coluna = []
        for z in range (3):
            contador += 1
            coluna.append(contador)
        linha.append(coluna)
    tabela.append(linha)

print(tabela)
for linha in tabela:
    for coluna in linha:
        print(coluna)