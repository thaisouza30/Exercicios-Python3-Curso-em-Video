from time import sleep
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [1]Somar
    [2]Multiplicar
    [3]Maior
    [4]Novos Números
    [5]Sair ''')
    opcao = int(input('Digite a opção escolhida: '))
    if opcao == 1:
        soma = valor1 + valor2
        print('A soma dos valores é {}'.format(soma))
    elif opcao == 2:
        multiplicacao = valor1 * valor2
        print('A multiplicação dos valores é {}'.format(multiplicacao))
    elif opcao == 3:
            if valor1 > valor2:
                print('O valor {} é maior'.format(valor1))
            elif valor1 == valor2:
                print('Os valores {} e {} são iguais'.format(valor1, valor2))
            else:
                print('O valor {} é maior'.format(valor2))
    elif opcao == 4:
        print('Informe os números novamente:')
        valor1 = int(input('Primeiro valor: '))
        valor2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida ,tente novamente')
    print('=-='*10)
    sleep(2)
print('Fim do programa! Volte sempre!')

