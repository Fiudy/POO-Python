from classes import Pessoa

Maria = Pessoa("Maria Cabecex", "Rua de Trás","71994336602", 14)


Pedro = Pessoa("Pedro Álvares", "Rua da Frente", "71993773306", 6)

Maria.matricular()
print("Matrícula de Maria = ", Maria.matricula)
Pedro.matricular()
print("Matrícula de Pedro = ", Pedro.matricula)
print (Maria.pagar())
print (Pedro.pagar())


