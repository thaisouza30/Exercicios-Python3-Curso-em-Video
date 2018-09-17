nota1 = float(input('Digite a primeira nota :'))
nota2 = float(input('Digite a segunda nota:'))
media = (nota1+nota2) / 2
print('A média é {:.1f}'.format(media))
if media < 5.0:
    print('Reprovado')
elif media == 5.0 or media <= 6.9:
    print('Recuperação')
elif media >= 7.0:
    print('Aprovado')
