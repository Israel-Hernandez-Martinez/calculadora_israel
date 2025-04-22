
def calcula_salario_semanal(salario, dias):
    salario_semanal = salario * dias
    return(salario_semanal)

def calcula_semanas_restantes(capital, salario_semanal):
    dias_restantes = capital/salario_semanal
    return(dias_restantes)
