class Produto:
    def __init__(self, codigo_barras, nome, preco, estoque):
        # Atributos privados (com __) conforme pedido no enunciado
        self.__codigo = codigo_barras
        self.__nome = nome
        self.__preco = preco
        self.__estoque = estoque

    # 1. MÉTODO ESTÁTICO (Utilitário: valida se o código de barras tem o tamanho correto)
    @staticmethod
    def validar_codigo_barras(codigo):
        # Apenas um exemplo simples de validação que não depende de nenhuma instância
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
    
    # Setter para permitir atualizar o estoque de forma segura
    @estoque.setter
    def estoque(self, nova_quantidade):
        if nova_quantidade >= 0:
            self.__estoque = nova_quantidade

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
        
        if self.__saldo < valor_total:
            print(f'Não foi possível realizar a compra. Saldo insuficiente (Saldo atual: R${self.__saldo})')
        else: 
            
            if produto.diminuir_estoque(quantidade):
                self.__saldo -= valor_total  
                print(f'A compra foi realizada com sucesso! Novo saldo de {self.__nome}: R${self.__saldo}')
            else:
                print(f'Não foi possível realizar a compra. Estoque insuficiente de {produto.nome}.')