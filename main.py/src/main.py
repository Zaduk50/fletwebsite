import flet as ft
from storage.data.text import mitteltitel, text1
from storage.data.children import left_children


def main(page: ft.Page):
    page.title = "Website test"



    header = ft.Row(
        controls=[
            ft.Container(
                content=ft.Text("Header", size=20, weight=ft.FontWeight.BOLD),
                bgcolor="lightblue",
                expand=True,
                padding=10,
            )
        ],

    )


    left_bar = ft.Container(width=200 , bgcolor="snow",
                            content= ft.Column(
                                controls=left_children,
                            ))

    middle_bar = ft.Container(expand=True, bgcolor="blue", padding=20,
                              content = ft.Column(
                                  controls=[mitteltitel,text1],
                                  horizontal_alignment=ft.CrossAxisAlignment.CENTER
                              ))

    right_bar = ft.Container(width=200, bgcolor="green",
                             content = ft.Column(
                                 [ft.Text("Right Bar")
                                  ]))



    information_part = ft.Row(controls=[left_bar, middle_bar, right_bar],
                              spacing=0,
                              expand=1,

                              )

    footer = ft.Row(
        controls=[
            ft.Container(
                content=ft.Text("Footer", size=20, weight=ft.FontWeight.BOLD),
                bgcolor="yellow",
                expand=True,
                padding=10,
            )
        ],

    )

    hauptansicht = ft.Column(controls=[header, information_part, footer],
                             spacing=0,
                             )

    page.add(
        ft.SafeArea(
            ft.Container(
                content=hauptansicht,
            ),
            expand=True,
        )
    )

ft.app(main, view=ft.WEB_BROWSER)
# ft.app(
#     main,
#     view=ft.WEB_BROWSER,
#     host="127.0.0.1",
#     port=8080,
#
