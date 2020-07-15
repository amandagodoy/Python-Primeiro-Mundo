vp = float(input('Informar preço do produto: R$'))
vf = vp - (vp * 5 / 100)
print('O valor antigo do produto era R${:.2f}, tendo a promoção de 5% sendo agora R${:.2f}'.format(vp,vf))
