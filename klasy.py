from random import shuffle

class Card:
    """ Klasa definiuje kartę do gry, przyjmuje 2 argumenty. Pierwszy
        argument to nazwa karty ['9', 10', 'J', 'Q', 'K', 'A'].
        Drugi argument to liczba od 0-3 która definouje kolor karty.
        Kolory kart ['trefl', 'pik', 'kier', 'karo']"""
    
    names = {'9':0, '10':10, 'J':2, 'Q':3, 'K':4, 'A':11}   

    def __init__(self, name, color_nr):
        """Konstruktor klasy, definiuje wartość danej karty oraz kolor. """
        self.name = name
        self.value = self.names[name]
        self.colors = ['trefl', 'pik',
                        'kier', 'karo']
        self.color = self.colors[color_nr]
        
    def __lt__(self, other):
        """ Metoda magiczna, definiuje możliwość porównywania < obiektów karty"""
        if self.value < other.value:
            return True
        return False

    def __gt__(self, other):
        """ Metoda magiczna, definiuje możliwość porównywania > obiektów karty"""
        if self.value > other.value:
            return True
        return False

    def __repr__(self):
        """ Metoda magiczna, zmienia nazwę podczas wywołania obiektu"""
        return self.name+' '+self.color

    def __str__(self):
        """ Metoda magiczna, zmienia nazwę podczas wywołania obiektu w obiekcie print()"""
        return "Nazwa:  {}\nKolor:  {}\nWartoś: {}".format(self.name,
                                                           self.color, self.value)
    def __eq__(self, other):
        """ Metoda magiczna, sprawdza równość wartości obiektów"""
        if self.value == other.value:
            return True
        return False

    def __add__(self, other):
        """ Metoda magiczna, dodaje dwa obiekty"""
        return self.value + other.value

    def __sub__(self, other):
        """ Metoda magiczna, odejmuje dwa obiekty"""
        return self.value - other.value


class Deck:
    """Klasa definiująca talię, tworzy 24 karty do gry w 1000 """
    def __init__(self):
        self.names_c = ['A', 'K', 'Q', 'J', '10', '9']
        self.cards = []
        for j in range(4):
            for i in self.names_c:
                self.cards.append(Card(i,j))

    def __str__(self):
        """ Metoda magiczna, zmienia nazwę podczas wywołania
            obiektu w obiekcie print()"""
        return "Talia 24 kart do gry w tysiąca"

    def __repr__(self):
        """ Metoda magiczna, zmienia nazwę podczas wywołania obiektu"""
        return "TALIA_24_obj"

    def take(self):
        """Metoda pozwala pobrać gotowa talie"""
        return self.cards


class Player:
    """Klasa definiuje gracza, przyjmuje tylko jeden argument, imię. """
    def __init__(self, name, chair):
        self.ID = int()
        self.name = name
        self.chair = chair
        self.tactic = False
        self.cards = []

    def __str__(self):
        return self.name

    def __repr__(self):
        """ Metoda magiczna, wyświetla nazwę podczas wywołania obiektu"""
        return self.name
     
    def build_tactic(self):
        self.tactic = Tactic(self.name)
        return self.tactic
'''
def create_players(tupla):
    list_players = []
    for i in tupla:
        gracz = Player(i[1], i[2])
        list_players.append(gracz)
    return list_players

def gracze_dict(gr):
    result_d = {}
    result_l = []
    for i in range(4):
        result_d[gr[i][2]] = gr[i][1]
    return result_d
'''

'''
class Table:
    """ Klasa definiująca stół. Stół tworzy talię kart, pobiera graczy {list},
        rozdaje karty, tworzy licytację, komunikacja z taktyką gracza.""" 
    def __init__(self, players:list):
        self.players = players
        self.cards = Deck()
        #self.auction = int()
        self.auction = [120, self.players[0]] # do wykasowania
        self.movement = ''
        self.trumf = ''
        self.musik = []

    def __str__(self):
        """ Metoda magiczna, wyświetla graczy w obiekcie print()"""
        return "Stół do gry:\n Gracze: {}".format(self.players)

    def __repr__(self):
        """ Metoda magiczna, wyświetla informacje o graczach"""
        return "Stół: {}".format(self.players)


    def expand(self):
        """ Metoda rozdaje karty graczom oraz 4 szt do self.musik."""
        for i in range(4):
            self.players[i].ID = i
        for i in self.players:
            tact = i.build_tactic()
            tact.clear_hand()
        cards = self.cards.take()
        shuffle(cards)
        self.get_music(cards[::6])
        list_list = [[cards[1], cards[2], cards[10], cards[11], cards[20]],
                     [cards[3], cards[4], cards[13], cards[14], cards[21]],
                     [cards[5], cards[7], cards[15], cards[16], cards[22]],
                     [cards[8], cards[9], cards[17], cards[19], cards[23]], ]
        for i in range(4):
            self.players[i].tactic.get_cards(list_list[i])
            self.players[i].tactic.sum_points()

    def get_music(self, card):
        """ Metoda pozwala dodac kartę graczowi."""
        self.musik.append(card)

    def reset_musik(self):
        """ Metoda czyszczenia danych"""
        self.musik = []

    def take_musik(self, stan:list):
        cards = stan[0]
        ID = int(stan[1])
        if ID == 0:
            self.players[1].tactic.get_cards([cards[0]])
            self.players[2].tactic.get_cards([cards[1]])
            self.players[3].tactic.get_cards([cards[2]])
        elif ID == 1:
            self.players[2].tactic.get_cards([cards[0]])
            self.players[3].tactic.get_cards([cards[1]])
            self.players[0].tactic.get_cards([cards[2]])
        elif ID == 2:
            self.players[3].tactic.get_cards([cards[0]])
            self.players[0].tactic.get_cards([cards[1]])
            self.players[1].tactic.get_cards([cards[2]])
        elif ID == 3:
            self.players[0].tactic.get_cards([cards[0]])
            self.players[1].tactic.get_cards([cards[1]])
            self.players[2].tactic.get_cards([cards[2]])

    def auct(self):
        """ Metoda wywołująca licytację graczy"""
        def dec(var):
            res = var%10
            return var - res
        players = self.players
        best = int()
        bp = None
        a = []
        while len(a)<3:
            for i in range(4):
                if players[i].licit == False:
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
                     


    def start(self):
        """ Metoda wywołująca start rozgrywki. Do skończenia!!!"""
        self.expand()
        #self.auct()
        # self.auction[1].tactic.get_cards(self.musik[0])
        # res = self.auction[1].tactic.play(0)
        # res = [res, self.auction[1].ID]
        # self.take_musik(res)
        self.reset_hands()
'''

class Tactic:
    """ Klasa definiuje taktykę gracza"""
    def __init__(self, name):
        self.player_name = name
        self.ID = int()
        self.colors = {'trefl': 0, 'pik': 0, 'kier': 0, 'karo': 0}
        self.cards = []
        self.licit = False
        self.hand = []
        self.musik_status = False
        self.trumf = False
        self.motion = False

    def check_stan(self):
        if self.musik_status == True:
            print(self.player_name, 'dodano karty z musika.', '\nTwój ruch.')
            self.take_musik()
        if self.motion == True:
            print(self.player_name, 'Twój ruch')

    def get_cards(self, cards:list):
        """ Metoda  pobierająca listę kart, przypisuje otrzymane karty do self.cards"""
        for i in cards:
            self.cards.append(i)

    def clear_hand(self):
        self.cards = []
        self.hand = []
        self.colors = {'trefl': 0, 'pik': 0, 'kier': 0, 'karo': 0}
        self.licit = False
        self.trumf = False

    def count_cards(self):
        """ Metoda sortująca karty, sumowania punktów {self.sum_cards},
            sprawdza karty "Q" i "K" z tego samego koloru {self.master}"""
        def sort(cards:list):
            color = ['A', 'K', 'Q', 'J', '10', '9']
            bufor = []
            for i in color:
                for j in range(len(cards)):
                    if i == cards[j].name:
                        bufor.append(cards[j])
            return bufor

        if len(self.cards) > 0:
            trefl = []
            pik = []
            kier = []
            karo = []
            self.hand = []
            for i in self.cards:
                if i.color == 'trefl':
                    trefl.append(i)
                elif i.color == 'pik':
                    pik.append(i)
                elif i.color == 'kier':
                    kier.append(i)
                else:
                    karo.append(i)
            alls = [sort(trefl), sort(pik), sort(kier), sort(karo)]
            for i in alls:
                self.hand.append(i)
            self.sum_cards = 0
            for i in alls:
                points = 0
                for j in i:
                    data = j.color
                    self.colors[data] += j.value
                    if (j.name == 'K'):
                        points =+ 1
                    if j.name == 'Q':
                        points = points +1
                if points == 2:
                    if j.color == 'trefl':
                        self.colors[j.color] = 100
                    elif j.color == 'pik':
                        self.colors[j.color] = 80
                    elif j.color == 'kier':
                        self.colors[j.color] = 60
                    elif j.color == 'karo':
                        self.colors[j.color] = 40       
            for i in self.cards:
                self.sum_cards += i.value
##            self.show_hand()
            self.hand = alls        
        else:
            return "Brak kart na ręce"


    def take_musik(self):
        self.sort_cards()
        
        def get_best_color():
            pass
           

        def get_bad_color():
            pass

        def get_first_c():
            pass

        
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
