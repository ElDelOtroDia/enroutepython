# var = 'mundo'
# num = 1234
# num2 = 5678
# flotante = 123.5
# flotante2 = 456.3
# caracter = 'c'
# caracter2 = 'd'

# bol = True
# bol2 = False
# bol3 = None

# print(var)
# print(caracter + caracter2)
# print(var + caracter)

# print(num + num2)
# print(flotante + flotante2)

# print(not bol)
# print(not bol2)
# print(bol or bol2)
# print(bol and bol2)

# if 10 > 5:
#     print('10 es mayor que 5')
# elif 10 < 5:
#     print('Eso es imposible')

# if bol:
#     print('Usamos la variable bol')

# if True:
#     print("Es verdadero")

# if not False:
#     print('La negacion de falso')

# var_rapida = 0
# while bol != bol2:
#     if var_rapida > 10:
#         bol = False
#     print(var_rapida)
#     var_rapida += 2

# for x in range(1, 101):
#     if not(x % 2):
#         print(x)

# if type(var_rapida) is int:
#     print('Es un entero')

# if type(var) is str:
#     print('Es una cadena')

# if type(flotante) is float:
#     print('Es flotante')

# if type(flotante) is int:
#     print('Es entero')

# arreglo_num = [0, 1, 2, 3]
# arreglo_car = ['c', 'h', 'a', 'r']

# print(arreglo_car[0])
# print(arreglo_car[1])
# print(arreglo_car[-1])
# print(len(arreglo_car))

# for cualquierNombreDeVariable in arreglo_num:
#     print(cualquierNombreDeVariable)

# for i in range(5):
#     print(var[i])

# for i in var:
#     print(i)

# for i in range(0, 100):
#     if (i & 1):
#         print(i)

for i in range(0, 100): 
  if i>1: 
    for j in range(2,i): 
        if(i % j==0): 
            break
    else: 
        print(i) 