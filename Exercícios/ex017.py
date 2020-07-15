import math
co = float(input('Digite um valor para cateto opoto: '))
ca = float(input('Digite outro valor para cateto adjacente: '))
hi = math.hypot(co, ca)
print('O valor da hipotenusa é {:.2f}'.format(hi))