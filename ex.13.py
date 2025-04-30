def calcular_idade_em_dias(anos, meses, dias):
    dias_por_ano = 365
    dias_por_mes = 30
    total_dias = (anos * dias_por_ano) + (meses * dias_por_mes) + dias
    
    return total_dias
anos = int(input("Digite a idade em anos: "))
meses = int(input("Digite a idade em meses: "))
dias = int(input("Digite a idade em dias: "))
idade_em_dias = calcular_idade_em_dias(anos, meses, dias)
print(f"A idade total em dias é: {idade_em_dias} dias.")
