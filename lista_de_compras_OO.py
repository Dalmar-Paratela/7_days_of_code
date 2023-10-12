class Produto:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

class ListaDeCompras:
    def __init__(self):
        self.produtos = []

    def mostrar_lista(self):
        if not self.produtos:
            print("A lista de compras está vazia.")
        else:
            for produto in self.produtos:
                print(f'Item: {produto.nome}, Quantidade: {produto.quantidade}')

    def inserir_produto(self, nome, quantidade):
        produto = Produto(nome, quantidade)
        self.produtos.append(produto)
        print(f'Item {nome} adicionado à lista.')

    def retirar_produto(self, nome):
        for produto in self.produtos:
            if produto.nome == nome:
                self.produtos.remove(produto)
                print(f'Item {nome} retirado da lista.')
                break
        else:
            print(f'Item {nome} não está na lista.')

    def alterar_quantidade(self, nome, nova_quantidade):
        for produto in self.produtos:
            if produto.nome == nome:
                produto.quantidade = nova_quantidade
                print(f'Quantidade de {nome} alterada para {nova_quantidade}.')
                break
        else:
            print(f'Item {nome} não está na lista.')

if __name__ == "__main__":
    lista = ListaDeCompras()

    while True:
        print('\nSAIR-(0)  MOSTRAR LISTA-(1)  INSERIR PRODUTO-(2)  RETIRAR PRODUTO-(3)  ALTERAR QUANTIDADE DE PRODUTO-(4)')
        decisao = input('O que fazer? ===> ').strip()

        if decisao == '0':
            break
        elif decisao == '1':
            lista.mostrar_lista()
        elif decisao == '2':
            nome_produto = input('Insira o novo item: ').strip().upper()
            quantidade_produto = int(input('Digite a quantidade: '))
            lista.inserir_produto(nome_produto, quantidade_produto)
        elif decisao == '3':
            nome_produto = input('Digite o nome do item a ser retirado da lista: ').strip().upper()
            lista.retirar_produto(nome_produto)
        elif decisao == '4':
            nome_produto = input('Qual item deseja alterar a quantidade? ').strip().upper()
            nova_quantidade = int(input('Insira a nova quantidade desejada: '))
            lista.alterar_quantidade(nome_produto, nova_quantidade)
