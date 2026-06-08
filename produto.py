class Produto:
    def __init__(self, codigo_barras, nome, preco, estoque):
        self.__codigo = codigo_barras
        self.__nome = nome
        self.__preco = preco
        self.__estoque = estoque

    @property
    def retornar_codigo(self):
        return self.__codigo
    
    @property
    def retornar_nome(self):
        return self.__nome
    
    @property
    def retornar_preco(self):
        return self.__preco
    
    @property
    def retornar_estoque(self):
        return self.__estoque
    
class Cliente:
    def __init__(self, nome, cpf, saldo):
        self.__nome = nome
        self.__cpf = cpf
        self.__saldo = saldo
        self.__carrinho = []

    @property
    def retornar_nome(self):
        return self.__nome

    @property
    def retornar_cpf(self):
        return self.__cpf
    
    @property
    def retornar_saldo(self):
        return self.__saldo
    
    @property
    def carrinho(self):
        return self.__carrinho
    
    def adicionar_ao_carrinho(self, produto, quantidade):
        if quantidade > produto.retornar_estoque:
            print(f"Erro Não há estoque suficiente de {produto.nome} para essa quantidade.")
            return
            
        item = {
            "produto": produto.nome,
            "quantidade": quantidade,
            "preco": produto.preco * quantidade
        }

        self.__carrinho.append(item)
        print(f"Sucesso: {quantidade}x '{produto.nome}' adicionado ao carrinho!")
