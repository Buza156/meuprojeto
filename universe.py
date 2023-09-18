resposta = 0
contador = 0

while resposta != 42:
    try:
        contador += b
        if contador >= 10:
            break
        resposta = int(input("Qual o numero do universo ? E tudo mais: "))
    except:
        print("Erro")
    