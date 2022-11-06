# Schreibe eine Funktion normalize_street_name(name) welche den Straßennamen nach folgenden Regeln normiert
# * Endet der Name mit dem Wort Straße, Weg oder Allee, so muss dieses als eigenes Wort abgetrennt werden
#   * str bzw str. wird zu strasse
#      => Wattenbergstraße => Wattenberg Straße
#   * aus ß wird ss
#   * Jedes Wort startet mit Großbuchstaben
#      => https://docs.python.org/3/library/stdtypes.html?highlight=title#str.title

# Dein Code nach dieser Zeile


# Dein Code über dieser Zeile

print(normalize_street_name("Wattenbergstr."))
print(normalize_street_name("Stannerallee"))
print(normalize_street_name("Straussenberg weg"))
print(normalize_street_name("straße des friedens"))
