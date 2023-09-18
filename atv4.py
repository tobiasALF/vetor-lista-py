list = []
continua = ""

while continua != "nao":
    compra = input("oque você precisa comprar? ")
    list.append(compra)
    continua = input("gostaria ne continuar a sua magnífica lista?(digite nao para parar)")
    if continua == "nao":
        break
print(list)     
