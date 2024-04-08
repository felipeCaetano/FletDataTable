import flet

header_style = {
    "height": 60,
    "bgcolor": "#081d33",
    "border_radius": flet.border_radius.only(top_left=15, top_right=15),
    "padding": flet.padding.only(left=15, right=15),
}


def search_field(function):
    return flet.TextField(
        border_color=flet.colors.TRANSPARENT,
        height=20,
        text_size=14,
        content_padding=0,
        cursor_color=flet.colors.WHITE,
        cursor_width=1,
        color=flet.colors.WHITE,
        hint_text='Search',
        on_change=function
    )


def search_bar(control):
    return flet.Container(
        width=350,
        bgcolor=flet.colors.WHITE,
        border_radius=6,
        opacity=0,
        animate_opacity=300,
        padding=8,
        content=flet.Row(
            spacing=10,
            vertical_alignment=flet.CrossAxisAlignment.CENTER,
            controls=[
                flet.Icon(
                    name=flet.icons.SEARCH_ROUNDED,
                    size=17,
                    opacity=.85,
                ),
                control,
            ],
        ),
    )


class Header(flet.Container):
    ''' header class'''

    def __init__(self):
        super().__init__(**header_style, on_hover=self.toggle_search)
        self.search_value = search_field(self.filter_dt_rows)
        self.search = search_bar(self.search_value)
        self.name = flet.Text("Line Indent", color='white')
        self.avatar = flet.IconButton("Person")
        self.content = flet.Row(
            alignment='spaceBetween',
            controls=[self.name, self.search, self.avatar]
        )

    def toggle_search(self, e):
        self.search.opacity = 1 if e.data == 'true' else 0
        self.search.update()
    def filter_dt_rows(self, e):
        ...

form_style = {
    "height": 60,
    "bgcolor": "white10",
    "border_radius": 8,
    "padding": 15,
}
class Form(flet.Container):
    def __init__(self):
        super().__init__()
def main(page: flet.Page):
    page.bgcolor = '#fdfdfd'
    header = Header()
    page.add(
        flet.Column(
            expand=True,
            controls=[
                header,
                flet.Divider(height=2, color=flet.colors.TRANSPARENT),
                # forms
                flet.Column(
                    scroll=flet.ScrollMode.HIDDEN,
                    expand=True,
                    controls=[]
                )
            ]
        )
    )


flet.app(main)
