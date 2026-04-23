# ## polimorfismo parametrico
from typing import TypeVar, Generic

T = TypeVar("T")

class Caixa (Generic[T]):
     def __init__(self, item: T):
        self.item = item
    
     def pegar_item(self) -> T:
         return self.item

if __name__ == "__main__":
     caixa_int = Caixa[int](42)
     caixa_str = Caixa[str]("Python")
     caixa_lista = Caixa[list]([1 ,2 ,3])

     print(caixa_int.pegar_item())
     print(caixa_str.pegar_item())
     print(caixa_lista.pegar_item())

    ##---------------------------------------------------------------------------------------##

##correção de tipos(type coercion)
print(5 + 3.14)  ##int é convertido para float automaticamnete

print("idade: " + str(25))

 ##outro exemplo comun
def repitir(texto, vezes):
     return texto * vezes
print(repitir("Python ", 3 ))
# ##---------------------------------------------------------------------------------------##
class Animal:
    def fazer_som(self):
         print("o animal faz um som...")

class cachorro(Animal):
     def fazer_som(self):
         print("au au au au au")  ##sobescrita(overriding)

class gato(Animal):
     def fazer_som(self):
         print("miau miau miau miau") ##sobrescrita

class vaca(Animal):
     def fazer_som(self):
         print("muuuuuuuuu!!")

 ###polimorfismo de inclusão

def fazer_barulho(animal: Animal):
     animal.fazer_som() ##Chamar o metodo correto de cada subclass

##testando
animais =[cachorro(),gato(),vaca(),Animal()]

for animal in animais:
     fazer_barulho(animal)

##---------------------------------------------------------------------------------------##

##polimorfismo de sobrecarga
class Calculadora:
    def somar(self, a, b=None):
        if b is None:
            return a+a
        return a + b
if __name__ == "__main__":
    calc = Calculadora()
    print(calc.somar(5))
    print(calc.somar(5, 3))

