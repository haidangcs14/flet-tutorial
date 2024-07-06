import flet as ft
from flet import *

def main(page: Page):
    page.title = "Flet App" 
    page.vertical_alignment = "center"

    txt_num = TextField(value="0", text_align="right", width=100)

    def minus_click(e):
        txt_num.value  = int(txt_num.value) - 1
        page.update()

    def plus_click(e):
        txt_num.value  = int(txt_num.value) + 1
        page.update()
    
    page.add(
        Row(
            [
                IconButton(icons.REMOVE, on_click=minus_click), 
                txt_num,
                IconButton(icons.ADD, on_click=plus_click),
            ],
            alignment="center"
        )
    )

if __name__ == "__main__":
    ft.app(target=main)