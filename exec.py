from produto import Produto


cafe = Produto("1234567890123", "Café", 10.0, 100)
acucar = Produto("1234555890123", "Açúcar", 20.0, 50)


resultado_cafe = Produto.validar_codigo_barras(cafe.codigo)
print(f"O código do {cafe.nome} é válido? {resultado_cafe}")

resultado_acucar = Produto.validar_codigo_barras(acucar.codigo)
print(f"O código do {acucar.nome} é válido? {resultado_acucar}")