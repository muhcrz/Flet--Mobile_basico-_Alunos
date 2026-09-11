import flet as ft


def main(page: ft.Page):

    # Título que aparece na barra da janela/aba
    page.title = "Contador"

    # Define o tamanho da tela
    page.window.width = 320
    page.window.height = 600

    # Cor de fundo da página inteira
    page.bgcolor = "#3D0E0E"

    # Padding vertical de 60px (topo e base)
    page.padding = ft.Padding(top=60, bottom=60, left=0, right=0)

    # Texto que exibe o valor atual do contador
    contador = ft.Text(
        "0",
        size=40,
        color="#FF6B6B",
        weight=ft.FontWeight.BOLD
    )

    # Variável para guardar a contagem
    valor = 0

    # Funcionalidades
    def somar(e):
        nonlocal valor
        valor += 1
        contador.value = str(valor)
        page.update()

    def subtrair(e):
        nonlocal valor
        valor -= 1
        contador.value = str(valor)
        page.update()

    def resetar(e):
        nonlocal valor
        valor = 0
        contador.value = str(valor)
        page.update()

    # Montagem da página do app
    page.add(
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.IconButton(
                    ft.Icons.REMOVE,
                    on_click=subtrair,
                    icon_color="#FF6B6B"
                ),
                contador,
                ft.IconButton(
                    ft.Icons.ADD,
                    on_click=somar,
                    icon_color="#FF6B6B"
                ),
            ],
        ),
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.TextButton(
                    "Resetar",
                    icon=ft.Icons.RESTART_ALT,
                    on_click=resetar,
                    style=ft.ButtonStyle(color="#FFB4B4")
                )
            ]
        )
    )


ft.run(main)
