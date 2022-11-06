# Wir definieren gemeinsam die verschiedenen Module
# Aufgaben der module
# und schreiben unserer eigene class CoffeeMachine


class CoffeeMachine:

    count = 0

    def __init__(self, brand):
        print("Erstelle Kaffee-Maschine")
        self.brand = brand

    def __del__(self):
        print("Kaffee-Maschine wir außer Dienst gestellt.")

    def make_coffee(self, coffee_type):
        print(f"Brühe Kaffee: {coffee_type}")
        self.count += 1
        print("Kaffee ist fertig.")


cm = CoffeeMachine("Krupps")

cm.make_coffee("Latte Macchiato")
