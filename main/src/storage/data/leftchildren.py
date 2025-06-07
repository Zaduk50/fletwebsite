import flet as ft

arrow_down = ft.Icons.ARROW_DROP_DOWN
arrow_up = ft.Icons.ARROW_DROP_UP_SHARP

def unfold_subtopics(klicked_button, page):
    subtopics = dependencies.get(klicked_button, [])

    is_opening = any(not s.visible for s in subtopics)

    if is_opening:
        klicked_button.content.controls[1].name = arrow_up
    else:
        klicked_button.content.controls[1].name = arrow_down

    for sub in subtopics:
        sub.visible = is_opening

    for key in dependencies:
        if key != klicked_button:
            key.content.controls[1].name = arrow_down
            for sub in dependencies.get(key, []):
                sub.visible = False

    page.update()


maintopic1 = ft.TextButton(
    content=ft.Row(
        controls=[
            ft.Text("Main Topic 1"),
            ft.Icon(arrow_down)]), on_click=lambda e: unfold_subtopics(maintopic1, e.page))

maintopic2 = ft.TextButton(
    content=ft.Row(
        controls=[
            ft.Text("Main Topic 2"),
            ft.Icon(arrow_down)]), on_click=lambda e: unfold_subtopics(maintopic2, e.page))

maintopic3 = ft.TextButton(
    content=ft.Row(
        controls=[
            ft.Text("Main Topic 3"),
            ft.Icon(arrow_down)]), on_click=lambda e: unfold_subtopics(maintopic3, e.page))



suptopic11 = ft.Container(ft.TextButton(text="Support Topic 1.1", on_click=lambda e: show_selection(suptopic11, e.page)),
                          padding=ft.padding.only(left=30), visible=False, animate_opacity=300, animate_size=300)
suptopic21 = ft.Container(ft.TextButton(text="Support Topic 2.1"), padding=ft.padding.only(left=30), visible=False, animate_opacity=300, animate_size=300)
suptopic22 = ft.Container(ft.TextButton(text="Support Topic 2.2"), padding=ft.padding.only(left=30), visible=False, animate_opacity=300, animate_size=300)
suptopic23 = ft.Container(ft.TextButton(text="Support Topic 2.3"), padding=ft.padding.only(left=30), visible=False, animate_opacity=300, animate_size=300)
suptopic31 = ft.Container(ft.TextButton(text="Support Topic 3.1"), padding=ft.padding.only(left=30), visible=False, animate_opacity=300, animate_size=300)
suptopic32 = ft.Container(ft.TextButton(text="Support Topic 3.1"), padding=ft.padding.only(left=30), visible=False, animate_opacity=300, animate_size=300)



dependencies = {
    maintopic1: [suptopic11],
    maintopic2: [suptopic21, suptopic22, suptopic23],
    maintopic3: [suptopic31, suptopic32],
}

left_children = [maintopic1, suptopic11, suptopic21,
                 maintopic2, suptopic21, suptopic22, suptopic23,
                 maintopic3, suptopic31, suptopic32]