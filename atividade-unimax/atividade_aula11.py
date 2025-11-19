# ==============================
# SISTEMA DE CONTROLE DE ESTOQUE
# ==============================

# ------------------------------
# Função recursiva para exibir a lista
# ------------------------------
def exibir_lista(lista, i=0):
    if i == len(lista):
        return
    print(f"[{i}] - Nome: {lista[i]['nome']} | Quantidade: {lista[i]['quantidade']} | Preço: R$ {lista[i]['preco']:.2f}")
    exibir_lista(lista, i + 1)


# ------------------------------
# Gerar relatório txt
# ------------------------------
def gerar_relatorio(lista, nome_arquivo="relatorio_estoque.txt"):
    with open(nome_arquivo, "w") as arquivo:
        arquivo.write("RELATÓRIO DE ESTOQUE\n")
        arquivo.write("=====================\n\n")
        
        for item in lista:
            arquivo.write(f"Produto: {item['nome']}\n")
            arquivo.write(f"Quantidade: {item['quantidade']}\n")
            arquivo.write(f"Preço: R$ {item['preco']:.2f}\n")
            arquivo.write("----------------------\n")

    print(f"\nRelatório gerado com sucesso: {nome_arquivo}")


# ------------------------------
# Busca recursiva
# ------------------------------
def buscar_produto(lista, nome, i=0):
    if i >= len(lista):
        return None
    if lista[i]['nome'].lower() == nome.lower():
        return lista[i]
    return buscar_produto(lista, nome, i + 1)


# ------------------------------
# Cadastro de produto
# ------------------------------
def cadastro_produto():
    nome = input("Nome do produto: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço: R$ "))

    return {'nome': nome, 'quantidade': quantidade, 'preco': preco}


# ------------------------------
# Soma recursiva das quantidades
# ------------------------------
def somatoria_das_quantidades_dos_produtos(lista, i=0):
    if i >= len(lista):
        return 0
    return lista[i]['quantidade'] + somatoria_das_quantidades_dos_produtos(lista, i + 1)


# ------------------------------
# Funções de arquivo (salvar e carregar)
# ------------------------------
def salvar_arquivo(lista, arquivo="estoque.txt"):
    with open(arquivo, "w") as f:
        for item in lista:
            f.write(f"{item['nome']};{item['quantidade']};{item['preco']}\n")


def carregar_arquivo(arquivo="estoque.txt"):
    lista = []
    try:
        with open(arquivo, "r") as f:
            for linha in f:
                nome, qtd, preco = linha.strip().split(";")
                lista.append({
                    'nome': nome,
                    'quantidade': int(qtd),
                    'preco': float(preco)
                })
    except FileNotFoundError:
        pass  # Se não existe arquivo ainda
    return lista


# ------------------------------
# MENU PRINCIPAL
# ------------------------------
def menu():
    produtos = carregar_arquivo()

    while True:
        print("\n=== SISTEMA DE CONTROLE DE ESTOQUE ===")
        print("1 - Cadastrar produto")
        print("2 - Exibir lista de produtos")
        print("3 - Total de itens no estoque")
        print("4 - Gerar relatório .txt")
        print("5 - Buscar produto pelo nome")
        print("6 - Sair")
        
        opc = input("Escolha uma opção: ")

        if opc == "1":
            produto = cadastro_produto()
            produtos.append(produto)
            salvar_arquivo(produtos)
            print("\nProduto cadastrado com sucesso!\n")

        elif opc == "2":
            if produtos:
                print("\nLISTA DE PRODUTOS:")
                exibir_lista(produtos)
            else:
                print("\nNenhum produto cadastrado.")

        elif opc == "3":
            total = somatoria_das_quantidades_dos_produtos(produtos)
            print(f"\nTotal de itens armazenados: {total}")

        elif opc == "4":
            gerar_relatorio(produtos)

        elif opc == "5":
            nome = input("Digite o nome do produto para buscar: ")
            resultado = buscar_produto(produtos, nome)
            if resultado:
                print("\nProduto encontrado:")
                print(resultado)
            else:
                print("\nProduto não encontrado.")

        elif opc == "6":
            print("Saindo do programa...")
            break

        else:
            print("Opção inválida. Tente novamente.\n")


# ------------------------------
# Executa o programa
# ------------------------------
menu()
