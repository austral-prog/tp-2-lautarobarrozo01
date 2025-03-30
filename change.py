def change():
    expense = 23.75
    money = 100
    vueltop = int(money-expense)
    vueltoc = int(round((money - expense - vueltop)*100))
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print()
    print("Vuelto")
    print()
    print("Pesos:")
    print(vueltop)
    print("Centavos:")
    print(vueltoc)
