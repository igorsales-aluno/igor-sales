import flet as ft

# ==============================
# SISTEMA DE CONTROLE DE ESTOQUE (FLET)
# ==============================


# ------------------------------
# Função recursiva para exibir a lista
# ------------------------------
def exibir_lista(lista, i=0, result=""):
    if i == len(lista):
        return result
    result += f"[{i}] - Nome: {lista[i]['nome']} | Quantidade: {lista[i]['quantidade']} | Preço: R$ {lista[i]['preco']:.2f}\n"
    return exibir_lista(lista, i + 1, result)


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
                lista.append({'nome': nome, 'quantidade': int(qtd), 'preco': float(preco)})
    except FileNotFoundError:
        pass
    return lista


# ------------------------------
# APLICATIVO FLET
# ------------------------------
def main(page: ft.Page):
    page.title = "Sistema de Controle de Estoque"
    page.scroll = "auto"

    produtos = carregar_arquivo()

    # Inputs
    nome_input = ft.TextField(label="Nome do produto")
    qtd_input = ft.TextField(label="Quantidade", keyboard_type=ft.KeyboardType.NUMBER)
    preco_input = ft.TextField(label="Preço", keyboard_type=ft.KeyboardType.NUMBER)

    buscar_input = ft.TextField(label="Buscar produto pelo nome")

    output = ft.Text(value="", size=16)

    # ------------------------------
    # Funções dos botões
    # ------------------------------
    def cadastrar_produto(e):
        try:
            produto = {
                'nome': nome_input.value,
                'quantidade': int(qtd_input.value),
                'preco': float(preco_input.value),
            }
            produtos.append(produto)
            salvar_arquivo(produtos)

            output.value = "✔ Produto cadastrado com sucesso!"
            nome_input.value = qtd_input.value = preco_input.value = ""
            page.update()
        except:
            output.value = "❌ Erro: Verifique os valores digitados."
            page.update()

    def mostrar_lista(e):
        if produtos:
            output.value = exibir_lista(produtos)
        else:
            output.value = "Nenhum produto cadastrado."
        page.update()

    def mostrar_total(e):
        total = somatoria_das_quantidades_dos_produtos(produtos)
        output.value = f"Total de itens em estoque: {total}"
        page.update()

    def gerar_relatorio_btn(e):
        gerar_relatorio(produtos)
        output.value = "✔ Relatório gerado: relatorio_estoque.txt"
        page.update()

    def buscar_btn(e):
        nome = buscar_input.value
        resultado = buscar_produto(produtos, nome)
        if resultado:
            output.value = f"Produto encontrado:\n{resultado}"
        else:
            output.value = "Produto não encontrado."
        page.update()

    # ------------------------------
    # Layout da interface
    # ------------------------------
    page.add(
        ft.Text("📦 Sistema de Controle de Estoque", size=30, weight="bold"),
        ft.Divider(),

        ft.Text("Cadastrar Produto", size=20, weight="bold"),
        nome_input,
        qtd_input,
        preco_input,
        ft.ElevatedButton("Cadastrar", on_click=cadastrar_produto),

        ft.Divider(),
        ft.Text("Consultas", size=20, weight="bold"),
        ft.Row([
            ft.ElevatedButton("Exibir Lista", on_click=mostrar_lista),
            ft.ElevatedButton("Total de Itens", on_click=mostrar_total),
            ft.ElevatedButton("Gerar Relatório", on_click=gerar_relatorio_btn),
        ]),

        buscar_input,
        ft.ElevatedButton("Buscar Produto", on_click=buscar_btn),

        ft.Divider(),
        output
    )


ft.app(target=main)