import flet as ft

class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )

        #scelta lingua -> prima riga
        self._dropDownLanguage=ft.Dropdown(  # il controllo Dropdown apre un menù a tendina
            label="Seleziona una lingua",
            options=[
                ft.dropdown.Option("italian"),  # dropdown.Option sono le opzioni selezionabili dal menù
                ft.dropdown.Option("english"),
                ft.dropdown.Option("spanish")
            ], expand=True
        )
        row1=ft.Row(controls=[self._dropDownLanguage]) #si estende per tutto lo spazio disponibile sulla riga
        self.page.add(row1)

        #scelta ricerca
        self._dropDownModality=ft.Dropdown(  # il controllo Dropdown apre un menù a tendina
                label="Seleziona una modalità di ricerca",
                options=[
                    ft.dropdown.Option("Default"),  # dropdown.Option sono le opzioni selezionabili dal menù
                    ft.dropdown.Option("Linear"),
                    ft.dropdown.Option("Dichotomic")
                ]
            )
        self._txtInFrase=ft.TextField(label="Inserisci la tua frase", expand=True)
        self._btnAvviaCorrezione=ft.ElevatedButton(text="Avvia correzione ortografica",
                                                   on_click=self.__controller.handleSpellCheck,
                                                   width=300)
        row2 = ft.Row(controls=[self._dropDownModality, self._txtInFrase, self._btnAvviaCorrezione]) #allinea a sinistra

        self._lvOut=ft.ListView(expand=True)
        self.page.add(row2, self._lvOut)
        self.page.update()

    def update(self):
        self.page.update()
    def setController(self, controller):
        self.__controller = controller
    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        #self.__txt_container.bgcolor = (
         #   ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300)
        """if self.page.theme_mode == ft.ThemeMode.DARK:
            self.__controller.output_frase.color=ft.colors.WHITE
            self.__controller.output_tempo.color=ft.colors.WHITE #le scritte nere diventano bianche quando switcho tema"""
        #quando cambio tema, le scritte nere diventano automaticamente bianche e viceversa
        self.page.update()
