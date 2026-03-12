def taxaCalculator(tx, price):
    total = (1 + (tx / 100)) * price
    return total


# função pura, argumento posicional
value = taxaCalculator(20, 100)
print(value)

# erro no argumento posicional
value = taxaCalculator(100, 20)
print(value)

# argumento keyword
value = taxaCalculator(price=100, tx=20)
print(value)


# função com propriedade default
def taxaCalculatorDefault(price, tx=20):
    total = (1 + (tx / 100)) * price
    return f"O valor {price} adicionado de {tx}% é {total:.2f}"


response1 = taxaCalculatorDefault(100)
print(response1)

response2 = taxaCalculatorDefault(100, 15)
print(response2)


# Exemplo de função impura
def taxaCalculatorImpure(price, tx=20):
    total = (1 + (tx / 100)) * price
    print(total)
    return f"O valor {price} adicionado de {tx}% é {total:.2f}"


response3 = taxaCalculatorImpure(100)
print(response3)


# Exemplo de função impura - efeito colateral
import random


def randomic(number):
    result = number + random.randint(0, 10)
    return result


print(randomic(10))


def definePar(number):
    if number % 2 == 0:
        return f"{number} é par"
    else:
        return f"{number} é ímpar"


print(definePar(10))
print(definePar(11))


def areaTriangulo(b, h):
    area = (b * h) / 2
    return area


base = float(input("Digite o valor da base: "))
altura = float(input("Digite o valor da altura: "))
print(f"A área do triangulo é: {areaTriangulo(base, altura)} u.a.")