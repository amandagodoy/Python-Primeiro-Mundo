vp = float(input('Informe qual o salário do funcionário: R$'))
vf = vp + (vp * 15 / 100)
print('O funcionário tinha um salário de R${}, assim houve dissídio c/ aumento de 15% e o salário sendo agora R${:.2f}'.format(vp,vf))
