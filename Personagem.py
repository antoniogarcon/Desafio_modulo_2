import random

class Personagem:
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel
    
    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()}\n Vida: {self.get_vida()}\n Nivel: {self.get_nivel()}"
    
    def atacar(self, alvo):
        dano = random.randint(self.get_nivel() * 2, self.get_nivel() * 4)
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano")

    def receber_ataque(self, dano):
        self.__vida -= dano
        #print(f"{self.get_nome()} recebeu {dano} de dano e tem {self.__vida} de vida restante")
        if self.__vida <= 0:
            self.__vida = 0
            #print(f"{self.get_nome()} morreu!")