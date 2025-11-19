def verificar_estoque(lista, indice=0):
    if indice >= len(lista):
        return 0
    item = lista[indice]
    if isinstance(item, dict):
        produto = item.get('nome', 'Desconhecido')
        quantidade = item.get('quantidade', 0)
    elif isinstance(item, (list, tuple)) and len(item) >= 2:
        produto, quantidade = item[0], item[1]
    else:
        print(f"Item inválido na posição {indice}: {item}. Pulando.")
        return verificar_estoque(lista, indice + 1)
    print(f"Produto: {produto} → {quantidade} unidades")
    return quantidade + verificar_estoque(lista, indice + 1)


def run_tests():
    print('Teste 1: lista de dicionários')
    estoque1 = [
        {'nome': 'Teclado', 'quantidade': 5},
        {'nome': 'Mouse', 'quantidade': 3}
    ]
    total1 = verificar_estoque(estoque1)
    print(f"Total esperado 8, obtido: {total1}")
    assert total1 == 8

    print('\nTeste 2: lista de tuplas')
    estoque2 = [
        ('Teclado', 5),
        ('Mouse', 3)
    ]
    total2 = verificar_estoque(estoque2)
    print(f"Total esperado 8, obtido: {total2}")
    assert total2 == 8

    print('\nTodos os testes passaram!')

if __name__ == '__main__':
    run_tests()
