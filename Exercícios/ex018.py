import math
ângulo = float(input('Digite o ângulo que deseja saber:'))
seno = math.sin(math.radians(ângulo))
print('O ângulo de {:.2f} tem seno de {:.2f}'.format(ângulo, seno))
cos = math.cos(math.radians(ângulo))
print('O ângulo de {:.2f} tem cosseno de {:.2f} '.format(ângulo, cos))
tan = math.tan(math.radians(ângulo))
print('O ângulo de {:.2f} tem tângente de {:.2f}'.format(ângulo, tan))
