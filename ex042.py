print('-=-'*20)
print('Analisador de triângulos')
print('-=-'*20)
r1 = float(input('Primeiro segmento :'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos informados podem formar um triângulo ',end='')

    if r1 == r2 == r3:
        print('Equilátero !')
    elif r1 != r2 != r3 != r1:
        print('Escaleno !')
    else:
        print('Isósceles !')

else:
    print('Os segmentos informados NÃO FORMAM TRIÂNGULO !')

