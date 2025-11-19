# recursividade - função que calcula o fatorial de um número.
#  Desafio 1 – Função com múltiplos retornos e escopo 

# Crie uma função analisar_numeros(lista) que: 
# Retorne três valores: quantidade de positivos, negativos e zeros. 
# Teste o comportamento ao usar uma variável global chamada total_elementos e mostre
# como o escopo interfere no resultado. 
# Desafio extra: reescreva sem variável global, usando apenas parâmetros e retornos.

# minhas funções:]

def analisar_numeros(lista):
    positivo = 0
    negativo = 0
    zero = 0
    for num in lista:
        if num > 0:
            positivo += 1
        elif num < 0:
            negativo += 1
        else:
            zero += 1
    return positivo, negativo, zero

def somar_lista(lista):
    if not lista:
        return 0
    else:
        return lista[0] + somar_lista(lista[1:])
    
