# Schreibe ein Programm, welches folgende Funktionen erfüllt:
# * Anzeigen der Kontoübersicht mit get_overview()
#   * Je Zeile steht Links die Beschreibung und rechts der Betrag
#     Netflix                                 -14.20 €
# * Ausgabe des aktuellen Kontostandes mit get_balance()
# * new_entry(transaction_type, amount, description) erzeugt Dictionary
#   * Mit z.B. account.append(new_entry("Abbuchung", 14.20, "Netflix")) kann dieser der Liste account hinzugefügt werden

account = []

# Dein Code unter dieser Zeile


# Dein Code über dieser Zeile


account.append(new_entry("Abbuchung", 14.20, "Netflix"))
account.append(new_entry("Einzahlung", 3244.60, "Lohn Juni"))
account.append(new_entry("Abbuchung", 35.77, "Amazon"))
account.append(new_entry("Abbuchung", 97.60, "Amazon"))
account.append(new_entry("Abbuchung", 260.26, "Hotel Waschbär"))
account.append(new_entry("Abbuchung", 870.40, "Miete"))
account.append(new_entry("Abbuchung", 460.14, "Leasing"))

print(get_overview())
print("Kontostand:" + f"{get_balance()} €".rjust(29))




