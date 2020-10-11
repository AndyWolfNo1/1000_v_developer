from klasy import *
import pandas as pd
from random import shuffle


gracze = ['Buczo', 'Tomek', 'Sebix', 'Marcin']
    
gra = Game(gracze)

print('\n', 'X'*50, '\n')

gracz1 = gra.players[0]
gracz2 = gra.players[1]
gracz3 = gra.players[2]
gracz4 = gra.players[3]

def show_gamer_card(value):
    for i in range(4):
        print('Gracz: ', gra.players[i].name, list(filter(lambda x: x.value == value, gra.players[i].tactic.cards)))

print('Funkcja "show_gamer_card" przyjmuje argument punktu karty i wyświetla tą kartę u graczy')
print('Np: "show_gamerr_card(11)"' )
show_gamer_card(11)


print('\n', 'X'*50, '\n')

print('Obiekt Gracza posiada taktykę a taktyka karty, np: \ngracz1.tactic.cards\n')
print(gracz1.tactic.cards, '\n')
print('Obiekt Gracza posiada inne ciekawe metody jak np: \ngracz1.tactic.colors\n')
print(gracz1.tactic.colors, '\n')
print('Lub np player_name albo ID gracza:')
print(gracz1.tactic.player_name, gracz1.tactic.ID)

