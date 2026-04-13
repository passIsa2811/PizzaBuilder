# Pizza Builder
import flet as ft

def main(page: ft.Page):

    # Functions      
    def add_pepperoni(e):
        pepperoni.visible = pep_switch.value 
        page.update()
    
    def add_ham(e):
        ham.visible = ham_switch.value
        page.update()
               
    def add_onion(e):
        onion.visible = onion_switch.value
        page.update()

    # images
    basePizza = ft.Image(src="assets/images/Recipe_Cheese.webp", height=350, width=350)
    pepperoni = ft.Image(src="assets/images/pepperoni yummm.webp", visible=False, height=350, width=350)
    ham = ft.Image(src="assets/images/hammmmm.webp", visible=False, height=350, width=350)
    onion = ft.Image(src="assets/images/onion.webp", visible=False, height=350, width=350)

    #switches

    pep_switch = ft.Switch(label="pepperoni", on_change=add_pepperoni)
    ham_switch = ft.Switch(label="ham", on_change=add_ham)
    onion_switch = ft.Switch(label="onion", on_change=add_onion)

    pizza = ft.Stack([
        basePizza,
        pepperoni,
        ham,
        onion
    ])

    controls = ft.Column(
        controls=[
            pep_switch,
            ham_switch,
            onion_switch
        ],
        width=250,
        height=250
    )

    # Page Setup 
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT
    page.add(pizza, controls)

ft.run(main)