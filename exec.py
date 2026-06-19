from produto import Produto, Cliente


cafe = Produto("1234567890124", "Café", 10.0, 100)
acucar = Produto("1234555890123", "Açúcar", 20.0, 50)

resultado_cafe = Produto.validar_codigo_barras(cafe.codigo)
print(f"O código do {cafe.nome} é válido? {resultado_cafe}")

resultado_acucar = Produto.validar_codigo_barras(acucar.codigo)
print(f"O código do {acucar.nome} é válido? {resultado_acucar}")

estoque = cafe.estoque
print(f"O o estoque do {cafe.nome} atualmente é de: {estoque}")

codigo = cafe.codigo
print(f"O código do {cafe.nome} é: {codigo}")

preco = cafe.preco
print(f"O preço do {cafe.nome} é: {preco}")

cafe.estoque = 150
print(f"Estoque de {cafe.nome} após reabastecimento: {cafe.estoque}")


pires = Cliente("João Victor Bernardo Pires", "123.456.789-01", 150.0)
lira = Cliente("Felipe Lira de Oliveira", "123.456.789-00", 150.0)

lira.fazer_compra(acucar, 2)