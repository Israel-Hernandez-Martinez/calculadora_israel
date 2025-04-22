import formulas

salario = float(input("Ingresa el salario: "))
dias = float(input("Ingresa los días de trabajo por semana: "))
capital = float(input("Ingresa tu capital: "))

salario_semanal = formulas.calcula_salario_semanal(salario, dias)
semanas_restantes = formulas.calcula_semanas_restantes(capital, salario_semanal)

print(f"Salario semanal: {salario_semanal}")
print(f"Semanas restantes: {semanas_restantes}")