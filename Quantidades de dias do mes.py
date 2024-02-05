mes_entrada = input()

dias_por_mes = {
    "1": 31,
    "2": 28,
    "3": 31,
    "4": 30,
    "5": 31,
    "6": 30,
    "7": 31,
    "8": 31,
    "9": 30,
    "10": 31,
    "11": 30,
    "12": 31,
}

quantidade_dias = dias_por_mes.get(mes_entrada.capitalize(), 0)

if dias_por_mes == 0:
    print("Mês inválido")
else:
    print(f"{quantidade_dias}")
    