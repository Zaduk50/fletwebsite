import flet as ft

titel1 = ft.Row(controls=[ft.Text(value="Titel 1",
                                  theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM,
                                  style=ft.TextStyle(weight=ft.FontWeight.BOLD))], wrap=True)

text1 = ft.Text(value="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore"
              " et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea"
              " rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.")

titel2 = ft.Row(controls=[ft.Text(value="Titel 2",
                                       theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM,
                                       style=ft.TextStyle(weight=ft.FontWeight.BOLD))], wrap=True)

text2 = ft.Text(value="Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt"
                      " ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo"
                      " dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor"
                      " sit amet.. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie"
                      " consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio"
                      " dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla"
                      " facilisi.. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit"
                      " lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit"
                      " in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis.. Nam"
                      " liber tempor cum soluta nobis eleifend option congue nihil imperdiet doming id quod mazim"
                      " placerat facer possim assum. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam"
                      " nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.. Duis autem vel"
                      " eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu"
                      " feugiat nulla facilisis.. At vero eos et accusam et justo duo dolores et ea rebum.")

text_subtopic11 = [titel1, text1, titel2, text2]

