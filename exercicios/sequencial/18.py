import math
name = 'alifer'
# Faça um Programa para uma loja de tintas. O programa deverá pedir
# o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada
# 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
# que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# 1. comprar apenas latas de 18 litros;
# 2. comprar apenas galões de 3,6 litros;
# 3. misturar latas e galões, de forma que o preço seja o menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
# considere latas cheias.


LITRO_TINTA_POR_METRO_QUADRADO = 6
LATA_TINTA = 18
LATA_PRECO = 80
GALAO_TINTA = 3.6
GALAO_PRECO = 25

area = float(input("Quantos metros² de deseja pintar?\n"))
litros_a_serem_usados = (area / LITRO_TINTA_POR_METRO_QUADRADO) * 1.1
print('litros a serem usados:', litros_a_serem_usados)

latas = math.floor(litros_a_serem_usados / LATA_TINTA)
galoes = math.ceil(
    (litros_a_serem_usados - (LATA_TINTA * latas)) / GALAO_TINTA)
print("Latas a serem usadas:", latas)
print("Galoes a serem usados:", galoes)
print("usando:", galoes, "galões, você vai gastar", (galoes * GALAO_PRECO))
print("usando:", latas, "latas, você vai gastar", (latas * LATA_PRECO))

print(" Comprando apenas latas você vai gastar: R$",
      (math.ceil(litros_a_serem_usados / LATA_TINTA) * LATA_PRECO))
print(" Comprando apenas galões você vai gastar: R$",
      (math.ceil((area / LITRO_TINTA_POR_METRO_QUADRADO) / GALAO_TINTA) * GALAO_PRECO))
