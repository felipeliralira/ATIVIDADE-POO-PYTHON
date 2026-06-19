class Produto:
    def __init__(self, codigo_barras, nome, preco, estoque):
        
        self.__codigo = codigo_barras
        self.__nome = nome
        self.__preco = preco
        self.__estoque = estoque

    #staticmethod serve para criar uma função comum dentro de uma classe 
    # valida se o código de barras tem o tamanho correto
    @staticmethod
    def validar_codigo_barras(codigo):
        # vendo se o codigo tem 13 caracter
        return len(str(codigo)) == 13

    # Decoradores Python (@property) para expor os atributos privados
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def nome(self):
        return self.__nome
    
    @property
    def preco(self):
        return self.__preco
    
    @property
    def estoque(self):
        return self.__estoque
    
    # Setter pra atualizar o estoque de forma segura
    @estoque.setter
    def estoque(self, nova_quantidade):
        if nova_quantidade >= 0:
            self.__estoque = nova_quantidade
        else:
            print("Quantidade de estoque não pode ser negativa.")

class Cliente: 
    def __init__(self, nome, CPF, saldo):
        self.__nome = nome
        self.__CPF = CPF
        self.__saldo = saldo 
    
    @property
    def nome(self): return self.__nome

    @property
    def saldo(self): return self.__saldo

    @property
    def CPF(self): return self.__CPF

    def fazer_compra(self, produto, quantidade):
        valor_total = produto.preco * quantidade
        print(f'\n{self.__nome} está tentando comprar {quantidade} unidade(s) de {produto.nome}. Valor total: R${valor_total}')

        print("Se deseja continuar (1) | Cancelar Compra(0)")
        valDigitado = int(input("Digite um número: "))

        # pra se a pessoa digitar outro valor que não seja 1 ou 0,
        # ele vai pedir pra digitar novamente
        while valDigitado not in [1, 0]:
            print("Valor Inválido! Tente novamente")
            valDigitado = int(input("Digite um número: "))

        if valDigitado == 1:
            if self.__saldo < valor_total:
                print(f'Não foi possível realizar a compra. Saldo insuficiente (Saldo atual: R${self.__saldo})')
            else:
                self.__saldo -= valor_total
                produto.estoque -= quantidade
                print(f'Compra realizada com sucesso! Novo saldo: R${self.__saldo}. Estoque restante de {produto.nome}: {produto.estoque}')
        else: print("Volte sempre!")