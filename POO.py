

class Pet:
    def __init__(self, nome, idade, cor):
        self.nome = nome
        self.idade = idade
        self.cor = cor

    def mostrar(self):
        print(f"Eu sou {self.nome} e tenho {self.idade} anos e sou {self.cor}")

class Gato(Pet):
    def Fala(self):
        print("Meow")

class Cachorro(Pet):
    def Fala(self):
        print("Auau")

class Cavalo(Pet):
    print("Ihuuuuuu")
    def comer(self):
        print("Comendo capim...")




p = Pet("RuffleS", 19, "rosa")
p.mostrar()

g = Gato("Kitty", 15, "branco")
g.mostrar()
g.Fala()

c = Cachorro("Caramelo", 20, "preto")
c.mostrar()
c.Fala()

ca = Cavalo("Henrico", 12, "Marrom")
ca.mostrar()
ca.comer()