import flet as ft
import requests

def main(page: ft.Page):
    page.title = "Smart Bar - Cliente"
    esp_ip = "http://192.168.0.45"  # IP do ESP32

    nome = ft.TextField(label="Seu nome:", width=300)
    cb_coca = ft.Checkbox(label="Coca-Cola")
    cb_pepsi = ft.Checkbox(label="Pepsi")
    cb_agua = ft.Checkbox(label="Água")

    def enviar_pedido(e):
        bebidas = []

        if cb_coca.value: bebidas.append("Coca-Cola")
        print("cb_coca.value:", cb_coca.value)
        print("nome.value:", nome.value)
        
        if cb_pepsi.value: bebidas.append("Pepsi")
        print("cb_pepsi.value:", cb_pepsi.value)
        print("nome.value:", nome.value)

        if cb_agua.value: bebidas.append("Água")
        print("cb_agua.value:", cb_agua.value)
        print("nome.value:", nome.value)

        for bebida in bebidas:
            try:
                r = requests.get(f"{esp_ip}/pedido", params={"nome": nome.value, "bebida": bebida})
                print(r.json())
            except Exception as erro:
                page.snack_bar = ft.SnackBar(ft.Text(f"Erro: {erro}"))
                page.snack_bar.open = True
                page.update()
                return

        page.snack_bar = ft.SnackBar(ft.Text("Pedido enviado!"))
        page.snack_bar.open = True
        page.update()

    page.add(
        ft.Text("Smart Bar 🍹", size=30, weight=ft.FontWeight.BOLD),
        nome,
        cb_coca,
        cb_pepsi,
        cb_agua,
        ft.ElevatedButton("Enviar Pedido", on_click=enviar_pedido)
    )

ft.app(target=main)