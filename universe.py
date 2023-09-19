try:
    num_mes = int(input("Digite o numero do mes"))
    meses = ["janeiro","fevereiro"]
    mes = meses[num_mes-1]
    print("o mes é ",mes)
except:
    print("Erro: voce precisa digitar um numero")