import sys

itens = ['PÉ-DE-PATO', 'CHUMBINHO', 'BACAMARTE']
quantidades = [1,2,3]

while True:
    print('\nSAIR-(0)  MOSTRAR LISTA-(1)  INSERIR PRODUTO-(2)  RETIRAR PRODUTO-(3)  ALTERAR QUANTIDADE DE PRODUTO-(4)')
    decisao = str(input('O que fazer? ===> ')).strip()

    if decisao not in ('0', '1', '2', '3', '4'):
        print('OPÇÃO INEXISTENTE\n')
        continue

    elif decisao == '0':
        sys.exit()

    elif decisao == '1':
        lens = len(itens)
        print('')
        for i in range(lens):
            print('Item:', itens[i], 'Quantidade:', quantidades[i])
        continue

    elif decisao == '2':
        print('\nTecle <enter> em uma entrada vazia para voltar ao menu inicial.')
        novo_item = input('Insira o novo item: ').strip().upper()
        if not novo_item:
            continue

        while True:
            nova_quant = input('Digite a quantidade: ').strip()
            if not nova_quant:
                print('ITEM NÃO LANÇADO')
                break

            try:
                nova_quant = int(nova_quant)
            except ValueError:
                print('\nQuantidade inválida')
                continue

            itens.append(novo_item)
            quantidades.append(nova_quant)
            break

    elif decisao == '3':
        while True:
            print('\nTecle <enter> em uma entrada vazia para voltar ao menu inicial.')
            item_fora = input('Digite o nome do item a ser retirado da lista: ').strip().upper()
            if not item_fora:
                break

            if item_fora in itens:
                a_fora = input(f'Confirma a retirada do item <{item_fora}>? (S ou N)').strip().lower()
                if a_fora != 's':
                    continue
                else:
                    index_fora = itens.index(item_fora)
                    del itens[index_fora]
                    del quantidades[index_fora]
                    print(f'O item <{item_fora}> foi retirado da lista.')
            else:
                print(f'O item <{item_fora}> não está na lista.')

    elif decisao == '4':
        while True:
            print('\nTecle <enter> em uma entrada vazia para voltar ao menu inicial.')
            item_muda_quant = str(input('Quer alterar a quantidade de qual item ? ')).strip().upper()
            if not item_muda_quant:
                break
            if item_muda_quant not in itens:
                print('OPÇÃO INEXISTENTE\n')
                continue

            if item_muda_quant in itens:
                index_muda_quant = itens.index(item_muda_quant)
                print(f'A quantidade atual do item <{item_muda_quant}> é', quantidades[index_muda_quant])
                new_quant = int(input('Insira a nova quantidade desejada: '))
                a_new = input(f'Confirma a alteração da quantidade para <{new_quant}>? (S ou N)').strip().lower()
                if a_new != 's':
                    continue
                else:
                    quantidades[index_muda_quant] = new_quant
                    print(f'O item <{item_muda_quant}> teve sua quantidade alterada para', new_quant)

