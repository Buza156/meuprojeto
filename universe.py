try:
    idade = int(input("Digite a sua idade:"))
except ValueError as error:
    print("Erro:",error)
except Exception as error:
   print("Aconteceu um erro", error)
   
else:
    print(f"Voce tem {idade} anos")    