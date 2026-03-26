#Herança hierárquica

class Veiculo:
    def __init__ (self, marca):
        self.marca = marca

    def mover(self):
            return "Esta se movimentando"

class carro(Veiculo):
    def mover(self):
        return "O carro esta se movimentando"

class bicicleta(Veiculo):
    def mover(self):
        return "A bicicleta esta se movimentando"

c = carro("Honda")
b = bicicleta("caloi")

print(c.marca, "→", c.mover())
print(b.marca, "→", b.mover())
#--------------------------------------------------------------------------------------------------------------------------#
print(40*"-")

#Herança simples
class pessoa:
     def __init__(self, nome,idade):
        self.nome = nome
        self.idade = idade

class Estudante(pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

e = Estudante("Michel", 23, "00359624")
print(f"{e.nome} tem {e.idade} anos e possui a matrícula {e.matricula}")
#--------------------------------------------------------------------------------------------------------------------------#
#Herança hierárquica

class Animal:
    def __init__ (self,nome , idade):
        self.nome = nome
        self.idade = idade

    def fazer_som(self):
        return "som generico do animal"
    
    def descrever(self):
        return f"Eu sou {self.nome} e tenho {self.idade} anos"
    
class Cachorro(Animal):
    def __init__ (self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def fazer_som(self):
        return "Au au"

class Gato(Animal):
    pass

rex = Cachorro("Rex", 6, "Labrador")

print(rex.descrever())
print(rex.fazer_som())
print(f"Rex é da raça {rex.raca}")

print("rex é um cachorro?", isinstance(rex, Cachorro))
print("rex é um animal?", isinstance(rex, Animal))
print("rex é um gato?", isinstance(rex, Gato))

help (Gato)

#--------------------------------------------------------------------------------------------------------------------------#
#HERENÇA MÚLTIPLA
class a: pass
class b: pass
class c(a,b): pass
print(c.__mro__)
help(c)
