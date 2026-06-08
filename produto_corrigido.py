class Produto:
    def __init__(self, codigo_barras, nome, preco, estoque):
        self.__codigo = codigo_barras
        self.__nome = nome
        self.__preco = preco
        self.__estoque = estoque

    # Usando nomes mais comuns para propriedades (só o nome do atributo)
    @property
    def nome(self):
        return self.__nome
    
    @property
    def estoque(self):
        return self.__estoque
    
class Cliente:
    def __init__(self, nome, cpf, saldo):
        self.__nome = nome
        self.__cpf = cpf
        self.__saldo = saldo
        self.__carrinho = [] # Sua lista de carrinho

    @property
    def carrinho(self):
        return self.__carrinho

    # O método precisa ficar DENTRO da classe Cliente (identado para a direita)
    def adicionar_ao_carrinho(self, produto, quantidade):
        # Usando a propriedade .estoque do produto
        if quantidade > produto.estoque:
            print(f"Erro: Não há estoque suficiente de {produto.nome} para essa quantidade.")
            return
        
        # Criando um dicionário para representar o item no carrinho
        item = {
            "produto": produto.nome,
            "quantidade": quantidade,
            "preco_unitario": produto._Produto__preco # Acessando o preço para registro
        }
        
        # Adicionando o item à lista self.__carrinho
        self.__carrinho.append(item)
        print(f"Sucesso: {quantidade}x '{produto.nome}' adicionado ao carrinho!")

# --- Testando o funcionamento ---

# 1. Criamos um produto e um cliente
notebook = Produto("12345", "Notebook", 3500.00, 5)
cliente1 = Cliente("Lucas", "111.222.333-44", 5000.00)

# 2. Tentamos adicionar mais do que o estoque (Deve dar erro)
cliente1.adicionar_ao_carrinho(notebook, 10)

# 3. Adicionamos a quantidade correta (Deve dar sucesso)
cliente1.adicionar_ao_carrinho(notebook, 2)

# 4. Verificando o que tem dentro do carrinho do cliente
print("\nConteúdo do Carrinho:", cliente1.carrinho)