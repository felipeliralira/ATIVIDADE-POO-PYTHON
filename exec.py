from produto import Produto
from produto import Cliente


cafe = Produto("123456789", "Café", 10.0, 100)
acucar = Produto("987654321", "Açúcar", 20.0, 50)

cliente1 = Cliente("João", "123.456.789-00", 100.0)

print(cafe.retornar_estoque)
print(cafe.retornar_codigo)

cliente1.adicionar_ao_carrinho(cafe, 2)
print(cliente1.carrinho)