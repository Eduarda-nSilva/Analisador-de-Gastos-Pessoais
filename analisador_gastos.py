import time

moradia = 0
alimentação = 0
lazer = 0
outros = 0

continuar = True

def nome_usuario(usuario):
    if usuario.strip() == '' or usuario.isdigit():
        return False
    else:
        return True

def valor_valido(gasto):
    try:
        gasto = float(gasto)
        return True
    except ValueError:
        return False

def verificar_categoria(categorias):
    opcoes_validas = ['1', '2', '3', '4','moradia', 'alimentação', 'lazer', 'outros']
    if categorias in opcoes_validas:
        return True
    else:
        return False


print('== == == BEM VINDO! == == ==')
time.sleep(1)

while continuar:
    usuario = str(input('Primeiro, como devo te chamar? '))

    if nome_usuario(usuario):
        print(f'Certo. Vamos começar {usuario}!')
        time.sleep(2)
        break
    else:
        print('Por favor. Digite um nome de usuario válido.')
        
while True:
    gasto = input('Digite o gasto: R$ ')
    if valor_valido(gasto):
        gasto = float(gasto)
        while True:
            print('== == == Categorias == == ==')
            print(f'{"[1] Moradia":^10}')
            print(f'{"[2] Alimentação":^10}')
            print(f'{"[3] Lazer":^10}')
            print(f'{"[4] Outros":^10}')
           
            
            categorias = input('Digite a qual categoria pertence o seu gasto: ').lower()

            if verificar_categoria(categorias):
                if categorias == '1' or categorias =='moradia':
                    moradia += gasto
                    print(f'O gasto de R$ {gasto}, foi adicionado a categoria: MORADIA')
                    break
                elif categorias == '2' or categorias == 'alimentação':
                    alimentação += gasto
                    print(f'O gasto de R$ {gasto}, foi adicionado a categoria: ALIMENTAÇÃO')
                    break
                elif categorias == '3' or categorias == 'lazer':
                    lazer += gasto
                    print(f'O gasto de R$ {gasto}, foi adicionado a categoria: LAZER')
                    break
                else:
                    outros += gasto
                    print(f'O gasto de R$ {gasto}, foi adicionado a categoria: OUTROS')
                    break
            else: 
                print('Erro! Escolha uma das categoria acima.')
                
        while True:
            pergunta = input('Desejar adicionar mais um gasto? ').lower()
            
            if pergunta == "sim" or pergunta == 's':
                break
            elif pergunta == 'não' or pergunta == 'n' or pergunta == 'nao':
                total = float(moradia + alimentação + lazer + outros)

                print ('== == == Extrato == == ==')
                print(f'Usuario: {usuario}\n')
                print(f'Moradia: R${moradia:^10.2f}')
                print(f'Alimentação: R${alimentação:^10.2f}')
                print(f'Lazer: R${lazer:^10.2f}')
                print(f'Outros: R${outros:^10.2f}')
                print(f'Total de gastos até o momento: R${total:^10.2f}\n')
                time.sleep(1)
                print(f'Obrigado por ultilizar o analisador de gastos, {usuario}')
                time.sleep(0.5)


                with open('extrato_gastos.txt', 'w', encoding = 'utf-8') as arquivo:                    
                    arquivo.write(f'EXTRATO DE GASTOS - USUÁRIO: {usuario}\n')
                    arquivo.write(f'Moradia: R$ {moradia:.2f}\n')
                    arquivo.write(f'Alimentação: R$ {alimentação:.2f}\n')
                    arquivo.write(f'Lazer: R$ {lazer:.2f}\n')
                    arquivo.write(f'Outros: R$ {outros:.2f}\n')
                    arquivo.write(f'TOTAL: R$ {total:.2f}\n')

                print('Seu extrato de gastos foi salvo em "extrato_gastos.txt"')

                time.sleep(0.5)
                print('Até á próxima :)')

                continuar = False
                break
            else:
                print('Erro. Digite apenas "sim" ou "não"')

        if not continuar:
            break
    


        
