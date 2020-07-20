nome = str(input('Digite seu nome por exetenso: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maísculo é {}'.format(nome.upper()))
print('Seu nome em minísculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
print('O seu primeiro nome tem {} letras'.format(nome.find(' ')))






#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maísculas; - upper()
#O nome com todas minúsculas; - lower()
#Quantas letras ao todo(sem considerar os espaços);
#Quantas letras tem o primeiro nome.

#separa = nome.split()
#print(separa)
#print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

