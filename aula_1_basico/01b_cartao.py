import flet as ft

def main(page: ft.Page):
    page.title = "Cartão de apresentação"

    # Define o tamanho da tela 
    page.window_width = 320
    page.window_height = 600

    # Cor de fundo da tela
    page.bgcolor = "#f2efe5"

    # Centra o conteúdo da tela
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER    

    # Padding interno da tela
    page.padding = ft.Padding(top=60, left=0, bottom=60, right=0)

    # Criação dos elementos da página
    page.add(
        # Nome em destaque
        ft.Text(
            "Travis Scott",
            size=28,
            weight=ft.FontWeight.BOLD,
            color="#755540",
            text_align=ft.TextAlign.CENTER,
        ),
        ft.Text(
            "Estudantes de programação mobile",
            size=14,
            color="#755540",
            text_align=ft.TextAlign.CENTER,
        ),
    )
# Inicia a aplicação 
ft.run(main)
