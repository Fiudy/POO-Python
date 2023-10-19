class Mamiferos:
    def __init__(self, temp):
        self.temp = temp
    
    def medirTemperatura(self):
        print(f"Sua temperatura: {self.temp}")

class Pessoa:
    contadorMatricula = 0
    def __init__(self, nome:str, endereco:str, telefone:int, idade:int):
        # Definindo atributos para pessoa:
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.idade = idade
        self.matricula = 0

    def matricular(self):
        Pessoa.contadorMatricula +=1
        self.matricula = Pessoa.contadorMatricula

    def estudar(self):
        if (self.idade>6):
            print("Creche")
        elif (self.idade<=10) and (self.idade>=6):
            print("Fundamental I")
        elif (self.idade<=14) and (self.idade>=11):
            print("Fundamental II")
        else:
            print("Ensino Médio")

    def pagar(self):
        match (self.idade):
            case [0,1,2,3,4,5]:
                print("Valor R$ 1.000,00")
            case [6,7,8,9, 10]:
                print("Valor R$ 1.800,00")
            case [11,12,13, 14]:
                print("Valor R$ 2.100,00")
            case list (range(15, 151)):
                print("Valor R$ 2.100,00")
   
