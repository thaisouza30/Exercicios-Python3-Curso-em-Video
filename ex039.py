from datetime import date
ano_nascimento = int(input('Digite o ano de nascimento:'))
ano_atual = date.today().year
idade = abs(ano_nascimento - ano_atual)
falta1 = (18 - idade)
falta2 = (idade - 18)
if idade < 18:
    print('Ainda vai se alistar , faltam {} anos'.format(abs(falta1)))
    ano = falta1 + ano_atual
    print('Seu alistamento será em {}'.format(ano))
elif idade == 18:
    print('Esta na hora de você se alistar')
elif idade > 18:
    print('Já passou {} anos do tempo de alistamento'.format(abs(falta2)))
    ano = ano_atual - falta2
    print('Seu alistamento foi em {}'.format(ano))



