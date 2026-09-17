
import flet as ft

def main(page: ft.Page):
    # Título que aparece na barra da janela/aba
    page.title = "Lista de Compras"

    # Cor de fundo da página inteira
    page.bgcolor = "#0F2E1D"

    # Centraliza os controles no eixo horizontal da página
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Padding vertical de 60px
    page.padding = ft.Padding(top=60, bottom=60, left=0, right=0)

    # Local para guardar os itens da lista
    itens = ["Leite", "Pão", "Café"]

    # Rolagem vertical
    list_view = ft.ListView(expand=True, spacing=8, width=320)

    # Campo de texto para adicionar novos itens
    campo = ft.TextField(
        label="Novo item",
        expand=True,
        color="#ffffff",
        label_style=ft.TextStyle(color="#8FD9B6"),
        border_color="#3F8F6C",
        focused_border_color="#5FE0A0",
    )

    def build_item(nome):
        # Cria uma linha com a tarefa
        def remover(e):
            itens.remove(nome)
            atualizar_lista()

        return ft.Row(
            controls=[
                ft.Text(nome, expand=True, color="#E5F5EC"),
                ft.IconButton(
                    ft.Icons.DELETE,
                    on_click=remover,
                    icon_color="#FF8585"
                )
            ]
        )

    def atualizar_lista():
        # Limpa e reconstrói a ListView
        list_view.controls.clear()

        for nome in itens:
            list_view.controls.append(build_item(nome))

        page.update()

    def adicionar(e):
        # Insere um novo item na lista
        if campo.value:
            itens.append(campo.value)
            campo.value = ""
            atualizar_lista()

    # Construção do layout da tela
    page.add(
        ft.Row(
            width=320,
            controls=[
                campo,
                ft.ElevatedButton(
                    "Adicionar",
                    on_click=adicionar,
                    bgcolor="#5FE0A0",
                    color="#0F2E1D"
                ),
            ],
        ),
        list_view
    )

    # Constrói a lista inicial
    atualizar_lista()

# Roda a aplicação
ft.run(main)