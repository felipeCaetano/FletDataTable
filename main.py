import flet

dummy_data = {
    0: {"name": "Apple", "description": "Red and Juicy", "quantity": 5,
        "price": 1.99},
    1: {"name": "Bread", "description": "Whole wheat loaf", "quantity": 2,
        "price":
            3.49},
    2: {"name": "Milk", "description": "Organic Whole Milk", "quantity": 1,
        "price": 2.99},
    3: {"name": "Carrot", "description": "Fresh and Crunchy", "quantity": 10,
        "price": 0.99},
    4: {"name": "Eggs", "description": "Free range Brown eggs", "quantity": 5,
        "price": 1.99},
    5: {"name": "Chicken", "description": "Whole wheat loaf", "quantity": 2,
        "price":
            3.49},
    6: {"name": "Banana", "description": "Organic Whole Milk", "quantity": 1,
        "price": 2.99},
}


class Controller:
    items = dummy_data
    counter = len(items)

    @staticmethod
    def get_items():
        return Controller.items

    @staticmethod
    def add_items(item):
        Controller.items[Controller.counter] = item
        Controller.counter += 1


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
        # width=350,
        bgcolor=flet.colors.WHITE10,
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

    def __init__(self, datatable):
        super().__init__(**header_style, on_hover=self.toggle_search)
        self.datable = datatable
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
        for data_rows in self.datable.rows:
            data_cell = data_rows.cells[0]
            data_rows.visible = (
                True
                if e.control.value.lower() in data_cell.content.value.lower()
                else False
            )

            data_rows.update()


form_style = {
    "bgcolor": "white10",
    "border_radius": 8,
    "border": flet.border.all(1, '#ebebeb'),
    "padding": 15,
}


def text_field():
    return flet.TextField(
        border_color="transparent",
        height=20,
        text_size=13,
        content_padding=0,
        cursor_color='black',
        cursor_width=1,
        cursor_height=18,
        color='black'
    )


def text_field_container(expand, name, control):
    return flet.Container(
        expand=expand,
        height=45,
        bgcolor='#ebebeb',
        border_radius=6,
        padding=8,
        content=flet.Column(
            spacing=1,
            controls=[
                flet.Text(
                    value=name,
                    size=9,
                    color='black',
                    width='bold',
                ),
                control
            ]
        )
    )


class Form(flet.Container):
    def __init__(self, datatable):
        super().__init__(**form_style)
        self.datatable = datatable
        self.row1_value = text_field()
        self.row2_value = text_field()
        self.row3_value = text_field()
        self.row4_value = text_field()

        self.row1 = text_field_container(
            True, "Row one", self.row1_value)
        self.row2 = text_field_container(
            3, "Row two", self.row2_value)
        self.row3 = text_field_container(
            1, "Row three", self.row3_value)
        self.row4 = text_field_container(
            1, "Row four", self.row4_value)

        self.submit = flet.ElevatedButton(
            text='Submit',
            style=flet.ButtonStyle(
                shape={"": flet.RoundedRectangleBorder(radius=8)}),
            on_click=self.submit_data
        )

        self.content = flet.Column(
            expand=True,
            controls=[
                flet.Row(controls=[self.row1]),
                flet.Row(controls=[self.row2, self.row3, self.row4]),
                flet.Row(controls=[self.submit], alignment='end'),
            ],
        )

    def submit_data(self, e):
        data = {
            "col1": self.row1_value.value,
            "col2": self.row2_value.value,
            "col3": self.row3_value.value,
            "col4": self.row4_value.value
        }
        Controller.add_items(data)
        self.clear_entries()
        self.datatable.fill_datatable()

    def clear_entries(self):
        self.row1_value.value = ""
        self.row2_value.value = ""
        self.row3_value.value = ""
        self.row4_value.value = ""

        self.content.update()


column_names = [
    "Column one", "Column two", "Column three", "Column four",
]

data_table_style = {
    "expand": True,
    "border_radius": 8,
    "border": flet.border.all(2, "#ebebeb"),
    "horizontal_lines": flet.border.BorderSide(1, '#ebebeb'),
    "columns": [
        flet.DataColumn(
            flet.Text(index, size=12, color='black', weight='bold')
        )
        for index in column_names
    ]
}


class DataTable(flet.DataTable):
    def __init__(self):
        super().__init__(**data_table_style)
        self.df = Controller.get_items()

    def fill_datatable(self):
        self.rows = []
        for values in self.df.values():
            data = flet.DataRow()
            data.cells = [
                flet.DataCell(
                    flet.Text(value, color='black')
                ) for value in values.values()
            ]
            self.rows.append(data)
        self.update()


def main(page: flet.Page):
    page.bgcolor = '#fdfdfd'
    table = DataTable()
    header = Header(datatable=table)
    form = Form(datatable=table)
    page.add(
        flet.Column(
            expand=True,
            controls=[
                header,
                flet.Divider(height=2, color=flet.colors.TRANSPARENT),
                form,
                flet.Column(
                    scroll=flet.ScrollMode.HIDDEN,
                    expand=True,
                    controls=[flet.Row(controls=[table])],
                )
            ]
        )
    )
    table.fill_datatable()


flet.app(main)
