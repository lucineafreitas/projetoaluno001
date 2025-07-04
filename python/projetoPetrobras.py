alcool = float(input("Insira o valor do alcool: "))
gasolina = float(input("Insira o valor da gasolina: "))

resultado = alcool / gasolina

print(resultado)

if resultado > 0.7:
    print("Abasteça com gasolina! ")
elif resultado < 0.7:
    print("Abasteça com alcool! ")
else:
    print("Tanto faz! ")
