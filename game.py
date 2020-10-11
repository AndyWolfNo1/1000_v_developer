from klasy import *
import pandas as pd
from random import shuffle


gracze = ['Buczo', 'Tomek', 'Sebix', 'Marcin']

class Game:
    '''Klasa gry w tysiąca'''

    def __init__(self,name:list):
        self.player1 = Player(name[0], 1)
        self.player2 = Player(name[1], 2)
        self.player3 = Player(name[2], 3)
        self.player4 = Player(name[3], 4)
        self.deck = Deck()
        self.players = self.gen_list_players()
        self.auction = [120, self.players[0]] # do okodowania
        self.musik = []
        self.build_tactic()
        self.expand()
        self.reset_hands()
        self.show_table()
        #self.auct()

    def __str__(self):
        """ Metoda magiczna, do użycia w print()"""
        return "Stół do gry:\n Gracze: {}".format(self.players)

    def __repr__(self):
        """ Metoda magiczna, wyświetla informacje o graczach"""
        return "Stół: {}".format(self.players)

    def gen_list_players(self):
        buf = []
        buf.append(self.player1)
        buf.append(self.player2)
        buf.append(self.player3)
        buf.append(self.player4)
        return buf

    def run_stan(self):
        for i in range(4):
            self.players[i].tactic.check_stan()

    def get_music(self, card):
        """ Metoda pozwala dodac kartę graczowi."""
        self.musik.append(card)

    def expand(self):
        """ Metoda rozdaje karty graczom oraz 4 szt do self.musik."""
        for i in range(4):
            self.players[i].ID = i
        for i in self.players:
            i.tactic.clear_hand()
        cards = self.deck.take()
        shuffle(cards)
        shuffle(cards)
        shuffle(cards)
        self.get_music(cards[::6])
        list_list = [[cards[1], cards[2], cards[10], cards[11], cards[20]],
                     [cards[3], cards[4], cards[13], cards[14], cards[21]],
                     [cards[5], cards[7], cards[15], cards[16], cards[22]],
                     [cards[8], cards[9], cards[17], cards[19], cards[23]], ]
        for i in range(4):
            self.players[i].tactic.get_cards(list_list[i])
##            self.players[i].tactic.sum_points()

    def build_tactic(self):
        for i in self.players:
            i.tactic = Tactic(i.name)

    def show_table(self):
        for i in range(4):
            print('Gracz ', self.players[i].name, self.players[i].tactic.hand)
        print('Musik' , self.musik)

    def take_musik(self, player:int):
        self.players[player].tactic.get_cards(self.musik[0])
        self.players[player].tactic.musik_status = True
        self.musik = []
        self.reset_hands()
        self.run_stan()
            
    def reset_hands(self):
        for i in range(4):
            self.players[i].tactic.count_cards()

    def clear_hands(self):
        for i in range(4):
            self.players[i].tactic.clear_hand()

    def auct(self):
        """ Metoda wywołująca licytację graczy (dopracować)"""
        def dec(var):
            res = var%10
            return var - res
        players = self.players
        best = int()
        bp = None
        a = []
        while len(a)<3:
            for i in range(4):
                if players[i].tactic.licit == False:
                    res = input('Licytuje {}:\n'.format(players[i].name))
                    try:
                        res = int(res)
                        res = dec(res)
                        if res < best:
                            print('Za mało!')
                        elif res == best:
                            print('Za mało!')
                            players[i].licit = False
                        if res > best:
                            best = res
                            players[i].licit = best
                            bp = players[i]
                            print('Najlepsza', best)
                    except:
                        if res == 'p':
                            players[i].licit = 'p'
                            a.append('p')
                            if len(a)==4:
                                print('Gra zakończona')
                                a = []
                                for e in range(4):
                                    players[e].licit = False
                            elif len(a)==3:
                                best = input('{} daje swoją wartość:\n'.format(players[i+1].name))
                                bests = [best, players[i+1]]
                                self.auction = bests
                                return
                                                  
                elif players[i].licit != 'p' :
                        res = input('Aktualna wartość: {}\nLicytuje {}, {}:\n'.format(best, players[i].name, players[i].licit))
                        try:
                            res = int(res)
                            res = dec(res)
                            if res < best:
                                print('Za mało!')
                            elif res == best:
                                print('Tyle już ktoś dał')
                            elif res > best:
                                best = res
                                players[i].licit = res
                                bp = players[i]
                        except:
                            if res == 'p':
                                players[i].licit = 'p'
                                a.append('p')
                if len(a)==3:
                    best = [best, bp]
                    self.auction = best
    
gra = Game(gracze)


gracz1 = gra.players[0]
gracz2 = gra.players[1]
gracz3 = gra.players[2]
gracz4 = gra.players[3]

def show_gamer_card(value):
    for i in range(4):
        print('Gracz: ', gra.players[i].name, list(filter(lambda x: x.value == value, gra.players[i].tactic.cards)))
