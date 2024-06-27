# Importando classes criadas
from Heroi import Heroi
from Inimigo import Inimigo

class Jogo:
    def __init__(self):
        self.heroi = Heroi(nome="Heroi", vida=100, nivel=5,habilidade="Super Forca")
        self.inimigo = Inimigo(nome="Morcego", vida=80, nivel=5, tipo="Voador")
        

    def iniciar_batalha(self):
        """Gestão da batalha em turnos"""
        print("Iniciando batalha!")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("Detalhes dos personagens")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            print("Escolha a ação do heroi:")
            print("1 - Ataque normal 2- Ataque especial")
            escolha = int(input("Escolha: "))
            print("\n\n\n")

            if escolha == 1:
                self.heroi.atacar(self.inimigo)
            elif escolha == 2:
                self.heroi.ataque_especial(self.inimigo)
            else:
                print("Escolha invalida")

            if self.inimigo.get_vida() > 0:
                self.inimigo.atacar(self.heroi)

        if self.heroi.get_vida() > 0:
            print("Heroi venceu!")
        else:
            print("Inimigo venceu!\n Você foi derrotado!!")
        
