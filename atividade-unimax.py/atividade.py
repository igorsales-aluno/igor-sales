# recursividade - função que calcula o fatorial de um número.
#  Desafio 1 – Função com múltiplos retornos e escopo 

# Crie uma função analisar_numeros(lista) que: 
# Retorne três valores: quantidade de positivos, negativos e zeros. 
# Teste o comportamento ao usar uma variável global chamada total_elementos e mostre
# como o escopo interfere no resultado. 
# Desafio extra: reescreva sem variável global, usando apenas parâmetros e retornos.

# minhas funções:]

def analisar_numeros(lista):
    positivos = 0
    negativos = 0
    zeros = 0
    for numero in lista:
        if numero > 0:
            positivos += 1
        elif numero < 0:
            negativos += 1
        else:
            zeros += 1
    return positivos, negativos, zeros

def soma_lista(lista):
    if not lista:
        return 0
    else:
        return lista[0] + soma_lista(lista[1:])

def buscar_maior(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        maior_dos_restantes = buscar_maior(lista[1:])
        if lista[0] > maior_dos_restantes:
            print(f"Comparando {lista[0]} com {maior_dos_restantes}: {lista[0]} é maior")
            return lista[0]
        else:
            print(f"Comparando {lista[0]} com {maior_dos_restantes}: {maior_dos_restantes} é maior")
            return maior_dos_restantes
def fibonacci_recursivo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)
def fibonacci_iterativo(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
# Testando a função analisar_numeros

input_lista = input("Informe uma lista de números separados por espaço: \n")
numeros = list(map(int, input_lista.split()))
positivos, negativos, zeros = analisar_numeros(numeros)
print(f"Quantidade de positivos: {positivos}")
print(f"Quantidade de negativos: {negativos}")
print(f"Quantidade de zeros: {zeros}")

# Variável global (não utilizada na função, apenas para demonstração)

total_elementos = len(numeros)
print(f"Total de elementos na lista (variável global): {total_elementos}")
def potencia(base, expoente):
    if expoente == 0:
        return 1
    else:
        return base * potencia(base, expoente - 1)
def eh_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
#  Desafio 2 - Soma recursiva 