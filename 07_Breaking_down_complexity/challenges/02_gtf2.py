# Setze Task 5 - 6 um
from data import get_movie_list
import random
movies = get_movie_list()
already_guessed = []

chosen_movie = random.choice(movies)
chosen_movie_length = len(chosen_movie)
# Task 5 Erstelle eine Liste mit "_" korrespondierend zu der Anzahl an Buchstaben
# Der Unterstrich soll nur gesetzt werden, wenn es sich nicht, um eines der erlaubten Symbole (allowed_symbols) handelt
# Diese Symbole sollen direkt, statt dem Unterstrich angezeigt werden:
# " ", ":", "-", "\'", "ä", "ö", "ü", "ß", "&", "!", "?"


# Task 6 tausche bei einem Treffer den entsprechenden Unterstrich durch den passenden Buchstaben aus
