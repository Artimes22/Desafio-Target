# Define o faturamento de cada estado
faturamento_SP = 67836.43
faturamento_RJ = 36678.66
faturamento_MG = 29229.88
faturamento_ES = 27165.48
faturamento_outros = 19849.53

# Calcula o faturamento total
faturamento_total = faturamento_SP + faturamento_RJ + faturamento_MG + faturamento_ES + faturamento_outros

# Calcula o percentual de representação de cada estado no faturamento total
percentual_SP = (faturamento_SP / faturamento_total) * 100
percentual_RJ = (faturamento_RJ / faturamento_total) * 100
percentual_MG = (faturamento_MG / faturamento_total) * 100
percentual_ES = (faturamento_ES / faturamento_total) * 100
percentual_outros = (faturamento_outros / faturamento_total) * 100

# Exibe o percentual de representação de cada estado no faturamento total
print("Percentual de representação de cada estado no faturamento total:")
print(f"SP: {percentual_SP:.2f}%")
print(f"RJ: {percentual_RJ:.2f}%")
print(f"MG: {percentual_MG:.2f}%")
print(f"ES: {percentual_ES:.2f}%")
print(f"Outros: {percentual_outros:.2f}%")
