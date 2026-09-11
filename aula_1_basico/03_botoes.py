import flet as ft

def main(page: ft.Page):

    page.title = "Árvore de controles"

    # Define o tamanho da tela
    page.window_width = 320
    page.window_height = 600

    # Cor de fundo da tela
    page.bgcolor = "#67B9B3"

    # Centra o conteúdo da tela
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Padding interno da tela
    page.padding = ft.Padding(top=60, left=0, bottom=60, right=0)

    # Campo de texto para o nome
    nome = ft.TextField(
        label="Digite seu Nome:",
        width=280, # Largura do campo
        color="#2D3142", # Cor do texto
        # Cor do label ("Seu nome")
        label_style=ft.TextStyle(color="#FFFFFF"), 
        border_color="#ffffff",
        # Cor quando campo em foco (Clicado ou ativado)
        focused_border_color="#5FA8A0",
    )

    # CheckBox de aceite dos termos
    aceite = ft.Checkbox(
        label="Aceito os termos",
        check_color="#FFFFFF",
        active_color="#5FA8A0",
        # Cor do label ("Aceito os termos")
        label_style=ft.TextStyle(color="#2D3142"),
    )

    # Texto de resultado (Após enviar)
    resultado = ft.Text(color="#3E7C7C")

    def enviar(e):
        # Função de envio dos dados com validações
        if not nome.value:
            nome.error_text = "Preencha seu nome"
            page.update()
            return

        nome.error_text = None

        resultado.value = (
            f"Obrigado, {nome.value}!"
            if aceite.value
            else "Você precisa aceitar os termos."
        )

        page.update()

    # Construção dos elementos
    page.add(
        ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                nome,
                ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[aceite], # CheckBox (Caixa para marcar ou não)
                ),
                # Botão "Enviar"
                ft.ElevatedButton(
                    "Enviar",
                    on_click=enviar, # Ao clicar chama a função enviar
                    bgcolor="#5FA8A0",
                    color="#FFFFFF"
                ),
                # Exibição dos resultados
                resultado,
            ],
        )
    )

ft.run(main)
