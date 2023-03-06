import statistics

# lista de faturamentos diários
faturamento_diario_lista1 = [
    {"dia": 1, "valor": 22174.1664},
    {"dia": 2, "valor": 24537.6698},
    {"dia": 3, "valor": 26139.6134},
    {"dia": 4, "valor": 0.0},
    {"dia": 5, "valor": 0.0},
    {"dia": 6, "valor": 26742.6612},
    {"dia": 7, "valor": 0.0},
    {"dia": 8, "valor": 42889.2258},
    {"dia": 9, "valor": 46251.174},
    {"dia": 10, "valor": 11191.4722},
    {"dia": 11, "valor": 0.0},
    {"dia": 12, "valor": 0.0},
    {"dia": 13, "valor": 3847.4823},
    {"dia": 14, "valor": 373.7838},
    {"dia": 15, "valor": 2659.7563},
    {"dia": 16, "valor": 48924.2448},
    {"dia": 17, "valor": 18419.2614},
    {"dia": 18, "valor": 0.0},
    {"dia": 19, "valor": 0.0},
    {"dia": 20, "valor": 35240.1826},
    {"dia": 21, "valor": 43829.1667},
    {"dia": 22, "valor": 18235.6852},
    {"dia": 23, "valor": 4355.0662},
    {"dia": 24, "valor": 13327.1025},
    {"dia": 25, "valor": 0.0},
    {"dia": 26, "valor": 0.0},
    {"dia": 27, "valor": 25681.8318},
    {"dia": 28, "valor": 1718.1221},
    {"dia": 29, "valor": 13220.495},
    {"dia": 30, "valor": 8414.61}
]
faturamento_diario_lista2 = [
    {"dia": 1, "valor": 22174.1664},
    {"dia": 2, "valor": 24537.6698},
    {"dia": 3, "valor": 26139.6134},
    {"dia": 4, "valor": 0.0},
    {"dia": 5, "valor": 0.0},
    {"dia": 6, "valor": 26742.6612},
    {"dia": 7, "valor": 0.0},
    {"dia": 8, "valor": 42889.2258 },
    {"dia": 9, "valor": 46251.174},
    {"dia": 10, "valor": 11191.4722},
    {"dia": 11, "valor": 0.0 },
    {"dia": 12, "valor": 0.0},
    {"dia": 13, "valor": 39807.662},
    {"dia": 14, "valor": 27261.6304},
    {"dia": 15, "valor": 39775.6434},
    {"dia": 16, "valor": 29797.6232 },
    {"dia": 17, "valor": 17216.5017 },
    {"dia": 18, "valor": 0.0000 },
    {"dia": 19, "valor": 0.0000 },
    {"dia": 20, "valor": 12974.2000 },
    {"dia": 21, "valor": 28490.9861 },
    {"dia": 22, "valor": 8748.0937 },
    {"dia": 23, "valor": 8889.0023 },
    {"dia": 24, "valor": 17767.5583 },
    {"dia": 25, "valor": 0.0000 },
    {"dia": 26, "valor": 0.0000 },
    {"dia": 27, "valor": 3071.3283 },
    {"dia": 28, "valor": 48275.2994 },
    {"dia": 29, "valor": 10299.6761 },
    {"dia": 30, "valor": 39874.1073 }
    ]


# lista de faturamentos diários em formato de dicionário
faturamento_dict = {f['dia']: f['valor'] for f in faturamento_diario_lista1}

# menor e maior valor de faturamento
min_faturamento_lista1 = min(faturamento_dict.values())
max_faturamento_lista1 = max(faturamento_dict.values())

# lista de faturamentos diários superiores à média mensal
media_mensal_lista1 = statistics.mean([f['valor'] for f in faturamento_diario_lista1 if f['valor'] != 0])
faturamento_superior_media_lista1 = [f for f in faturamento_diario_lista1 if f['valor'] > media_mensal_lista1]

# número de dias no mês em que o faturamento diário foi superior à média mensal
num_dias_faturamento_superior_media = len(faturamento_superior_media_lista1)

print("Menor valor de faturamento: {:.2f}".format(min_faturamento_lista1))
print("Maior valor de faturamento: {:.2f}".format(max_faturamento_lista1))
print("Número de dias com faturamento superior à cima da media")

print("-="*30)

# lista de faturamentos diários em formato de dicionário
faturamento_dict = {f['dia']: f['valor'] for f in faturamento_diario_lista2}

# menor e maior valor de faturamento
min_faturamento_lista2 = min(faturamento_dict.values())
max_faturamento_lista2 = max(faturamento_dict.values())

# lista de faturamentos diários superiores à média mensal
media_mensal_lista2 = statistics.mean([f['valor'] for f in faturamento_diario_lista1 if f['valor'] != 0])
faturamento_superior_media_lista2 = [f for f in faturamento_diario_lista2 if f['valor'] > media_mensal_lista2]

# número de dias no mês em que o faturamento diário foi superior à média mensal
num_dias_faturamento_superior_media = len(faturamento_superior_media_lista2)

print("Menor valor de faturamento: {:.2f}".format(min_faturamento_lista2))
print("Maior valor de faturamento: {:.2f}".format(max_faturamento_lista2))
print("Número de dias com faturamento superior à cima da media")
