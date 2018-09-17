larg = float(input('Qual é a largura da parede?'))
alt = float(input('Qual a altura da parede?'))
area = larg * alt
print('A sua parede tem as dimensões de {} x {} e sua área total é de {}m²'.format(larg,alt,area))
tinta = area / 2
print('Para pintar essa parede você precisará de {}litros de tinta '.format(tinta))
