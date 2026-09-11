import flet as ft

def main(page: ft.Page):

    page.title = "Árvore de controles"

    # Define o tamanho da tela
    page.window_width = 320
    page.window_height = 600

    # Cor de fundo da tela
    page.bgcolor = "#0B3D3A"

    # Centra o conteúdo da tela
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Padding interno da tela
    page.padding = ft.Padding(top=60, left=0, bottom=60, right=0)

    # Criação dos elementos da página
    cartao = ft.Container(

        # Conteúdo do cartão organizado em coluna
        content=ft.Column(

            horizontal_alignment=ft.CrossAxisAlignment.CENTER,

            controls=[

                # Título do cartão
                ft.Text(
                    "Travis Scott",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color="#1FE0C4",
                ),

                # Texto descritivo
                ft.Text(
                    "Descrição do cartão",
                    color="#CFEFE9",
                ),

                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,

                    controls=[
                        ft.ElevatedButton(
                            "Ação 1",
                            bgcolor="#1FE0C4",
                            color="#0B3D3A",
                        ),

                        # Botão secundário
                        ft.OutlinedButton("Ação 2"),
                    ]
                ),
            ]
        ),

        padding=16,
        bgcolor="#123C3C",
        border_radius=12,
    )

    # Adiciona o cartão à página
    page.add(cartao)


# Inicia a aplicação
ft.run(main)