# ----------------- Encapsulamento em Python (Uma convenção) ------------------------------------------------
# Encapsulamento é a característica em OOP de poder proteger dados internos da 
# classe a manipulação externa acidental. Tornando atributos e/ou métodos privados a classe.
# Ex.: Na classe ContaCorrente poderíamos definir o atributo 'saldo' como privado
# a classe, só podendo ser manipulado por métodos especializados também internos
# a classe, chamados por exemplo; depositar() e sacar().
# Em classes Python, um atributo ou um método para ser protegido de manipulações
# externas, deve iniciar seu nome com 2 sublinhados '__', ex. __meuAtributo, por convenção
################################

class ContasBancariasForaPadrao:
    def __init__(self, correntista):
        self.__saldo = 0     # Atributo privado a classe
        self.correntista = correntista
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, valor):
        if (self.__saldo+valor)>=0.0: 
            self.__saldo += valor
            return True
        else:
            self.saldo
            return False



# Instanciando a classe ContasBancarias...
minhaCC = ContasBancariasForaPadrao("Guilherme")
# A linha abaixo deve ser evitada. Por convenção, deve-se
# nomear os atributos que sejam privados as classes, iniciando
# com 2 caracteres 'sublinhados'
print(minhaCC.saldo)   # 0
minhaCC.saldo =  1000
minhaCC.saldo =  500
print(minhaCC.saldo) # 1500
minhaCC.saldo =  -1501
print(minhaCC.saldo) # 1000
minhaCC.saldo = -1500
print(minhaCC.saldo) #-1500









# Como fazer para criar uma classe com atributos/métodos privados??!
class ContasBancarias:
    def __init__(self):
        self.__saldo = 0.0    # Atributo privado a classe (por convenção)

    # Criando um método Getter (o que obtem o valor)
    # para poder obter fora da classe o 'saldo'
    # da conta.    
    @property
    def saldo(self):
        '''
        Obtem o saldo da conta
        '''
        return self.__saldo

    # Criando um método Setter (o que atribui o valor)
    # Método para adicionar valor ao 
    # saldo existente.
    @saldo.setter
    def saldo(self, valor):
        '''
            Atribui um valor a crétido ou débito a conta\n
            (respeitando as regras de negócio estabelecidas)
        '''
        if (self.__saldo+valor)>=0.0: 
            self.__saldo += valor
            return True
        else:
            self.saldo
            return False

minhaCP = ContasBancarias()
print(minhaCP.saldo)        # Isso é o Getter, 0
minhaCP.saldo = 1000.0      # Isso é o Setter
print(minhaCP.saldo)        # 1000
minhaCP.saldo = -250.0      # 750
print(minhaCP.saldo)        # 750
# Tentando sacar um valor MAIOR do que o saldo...
minhaCP.saldo = -751.0      # -1, não pode!!!
print(minhaCP.saldo)        # 750
# Tente acessar diretamente o atributo __saldo do objeto 'minhaCP'!!
# tente aqui: ...
print(minhaCP.__dict__)

#exit()

'''
    Uma outra forma de utilizar o decorator 'Property' é através da
    função.
'''
# Como fazer para criar uma classe com atributos/métodos privados??!
class ContasBancariasAplicacao:
    def __init__(self):
        self.__saldo = 0.0    # Atributo privado a classe (por convenção)

    # Getter
    def saldoAtual(self):
        '''
        Obtem o saldo da conta
        '''
        return self.__saldo

    # Setter
    def movimentar(self, valor):
        '''
            Atribui um valor a crétido ou débito a conta\n
            (respeitando as regras de negócio estabelecidas)
        '''
        if (self.__saldo+valor)>=0.0: 
            self.__saldo += valor
            return True
        else:
            self.saldo
            return False
    # Gerando o Objeto 'Property'
    saldo = property(saldoAtual, movimentar)

# Teste de Mesa da Classe ContaBancariasAplicacao
minhaCA = ContasBancariasAplicacao()
print(minhaCA.saldo)        # Isso é o Getter, 0
minhaCA.saldo = 1000.0      # Isso é o Setter
print(minhaCA.saldo)        # 1000
minhaCA.saldo = -250.0      # 750
print(minhaCA.saldo)        # 750
# Tentando sacar um valor MAIOR do que o saldo...
minhaCA.saldo = -751.0      # -1, não pode!!!
print(minhaCA.saldo)        # 750
# Tente acessar diretamente o atributo __saldo do objeto 'minhaCP'!!
# tente aqui: ...
print(minhaCA.__dict__)

exit()


# Exercício 3:
# Crie uma classe nomeada como Cinema, que tem um atributo privado
#  chamado 'idade', crie os métodos getter e setter para esse 
#  atributo. O método setter só deve aceitar idade igual ou maior a 18.
from Classe import Cinema

sala1 = Cinema()     
print(sala1.old )   #0
sala1.old=19
print(sala1.old)    # 19
sala1.old = 16
print(sala1.old)    # 19


# Exercício 4: 
# Crie uma classe que modela o objeto NotaFiscal. Esta classe deve ter
#  dentre outros atributos, um privado nomeado de 'codigoNF', que deve ser
#  uma string, composta de 8 caracteres, iniciando com as letras 'NF'.

from Classe import NF

# Teste de Mesa da Classe NF:
objNF = NF(2500)            # Instância o objeto NF na variável objNF
numero = input("Digite o Numero da NF: ")
objNF.numeroNF = numero     # Chama o método Setter

print(f"{objNF.numeroNF} -> R${objNF.valor:.2f}") # Getter