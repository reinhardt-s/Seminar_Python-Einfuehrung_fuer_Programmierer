import random

# Blackjack!
# Das Kartendeck hat eine unbegrenzte Größe
# Es gibt keine Joker
# Bube, Dame, König zählen 10
# Ass wird als 11 gezählt. Falls sich der Spieler überkaufen sollte und ein Ass in der Hand hält, wird
# dieses als 1 gezählt
# Du kannst ein Deck wie folgt definieren:
# * cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# Jede Karte in cards hat die gleiche Wahrscheinlichkeit gezogen zu werden
# Da das Deck unendlich ist, werden gezogene Karten nicht aus dem Deck entfernt
# Die Spieler*in verliert, bei Gleichstand mit 21, wenn sie sich überkauft und wenn der Computer näher an der 21
# ist (und sich dabei nicht überkauft hat,
# Die Spielerin gewinnt sofort bei, wenn Sie mit zwei Karten auf 21 kommt
