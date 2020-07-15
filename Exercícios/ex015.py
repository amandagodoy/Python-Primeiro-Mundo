d = int(input('Informe os dias de uso: '))
km = float(input('Informe os km utilizados: '))
pg = (d * 60) + (km * 0.15)
print('O total a pagar referente ao aluguel R${:.2f}'.format(pg))
