frase = str(input('Escreva uma frase:')).upper().strip()
print('A letra A aparece em sua frase {} vezes'.format(frase.count('A')))
print('A primeira ocorrência da letra A esta na posição {} '.format(frase.find('A')+1))
print('A última ocorrência da letra A esta na posição {}'.format(frase.rfind('A')+1))




