print("Olá mundo!")

#ENTRADA DE DADOS
nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
nota3 = float(input("Insira a terceira nota: "))
nota4 = float(input("Insira a quarta nota: "))

#PROCESSAMENTO DOS DADOS
notaFinal = (nota1 + nota2 + nota3 + nota4) / 4

#SAÍDA
print("A nota final é: ", notaFinal)

if notaFinal < 60:
    print("O aluno está reprovado! ")
elif(notaFinal < 70):
    print("O resultado foi mediano!")
elif(notaFinal < 80):
    print("O resultado foi muito bom!")
elif(notaFinal < 90):
    print("O resultado foi excelente!")
else:
    print("Você vai para Harvard! ")
