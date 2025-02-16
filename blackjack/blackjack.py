import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'
os.environ['NSApplicationSupportsSecureRestorableState'] = 'NO'

import tkinter as tk
from tkinter import messagebox
import random

# Constants
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranking = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
card_val = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

# Classes
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace = False

    def __str__(self):
        hand_comp = ""
        for card in self.cards:
            hand_comp += " " + card.__str__()
        return 'The hand has %s' % hand_comp

    def card_add(self, card):
        self.cards.append(card)
        if card.rank == 'A':
            self.ace = True
        self.value += card_val[card.rank]

    def calc_val(self):
        if self.ace and self.value < 12:
            return self.value + 10
        else:
            return self.value

class Deck:
    def __init__(self):
        self.deck = [Card(suit, rank) for suit in suits for rank in ranking]

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

# Game Functions
def deal_initial_cards(deck, player_hand, dealer_hand):
    player_hand.card_add(deck.deal())
    player_hand.card_add(deck.deal())
    dealer_hand.card_add(deck.deal())
    dealer_hand.card_add(deck.deal())

def hit(deck, hand):
    hand.card_add(deck.deal())

def check_bust(hand):
    return hand.calc_val() > 21

class BlackjackApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack Game")
        self.deck = Deck()
        self.deck.shuffle()
        self.players = []
        self.current_player = None
        self.player_hand = None
        self.dealer_hand = None
        self.bet = 0

        self.setup_ui()

    def setup_ui(self):
        self.intro_frame = tk.Frame(self.root)
        self.intro_frame.pack()

        self.intro_label = tk.Label(self.intro_frame, text="Welcome to Blackjack!")
        self.intro_label.pack()

        self.num_players_label = tk.Label(self.intro_frame, text="Enter the number of players:")
        self.num_players_label.pack()

        self.num_players_entry = tk.Entry(self.intro_frame)
        self.num_players_entry.pack()

        self.start_button = tk.Button(self.intro_frame, text="Start Game", command=self.start_game)
        self.start_button.pack()

    def start_game(self):
        try:
            num_players = int(self.num_players_entry.get())
            if num_players <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number of players.")
            return

        self.intro_frame.pack_forget()
        self.players = []
        for i in range(num_players):
            name = f"Player {i+1}"
            chips = self.get_starting_chips(name)
            self.players.append({'name': name, 'chips': chips})
        self.current_player = 0

        self.game_frame = tk.Frame(self.root)
        self.game_frame.pack()

        self.update_player_info()

    def get_starting_chips(self, name):
        while True:
            try:
                chips = int(input(f"Enter the starting amount of dollars for {name}: "))
                if chips > 0:
                    return chips
                else:
                    print("Please enter a positive amount.")
            except ValueError:
                print("Please enter a valid integer.")

    def update_player_info(self):
        self.game_frame.pack_forget()
        self.game_frame = tk.Frame(self.root)
        self.game_frame.pack()

        self.player_label = tk.Label(self.game_frame, text=f"{self.players[self.current_player]['name']}'s turn:")
        self.player_label.pack()

        self.chips_label = tk.Label(self.game_frame, text=f"You have ${self.players[self.current_player]['chips']} chips.")
        self.chips_label.pack()

        self.bet_label = tk.Label(self.game_frame, text="Enter your bet:")
        self.bet_label.pack()

        self.bet_entry = tk.Entry(self.game_frame)
        self.bet_entry.pack()

        self.bet_button = tk.Button(self.game_frame, text="Place Bet", command=self.place_bet)
        self.bet_button.pack()

    def place_bet(self):
        try:
            self.bet = int(self.bet_entry.get())
            if self.bet <= 0 or self.bet > self.players[self.current_player]['chips']:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Bet", "Please enter a valid bet amount.")
            return

        self.game_frame.pack_forget()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        deal_initial_cards(self.deck, self.player_hand, self.dealer_hand)

        self.play_frame = tk.Frame(self.root)
        self.play_frame.pack()

        self.dealer_label = tk.Label(self.play_frame, text="Dealer's hand:")
        self.dealer_label.pack()

        self.dealer_hand_label = tk.Label(self.play_frame, text=str(self.dealer_hand.cards[0]) + " XX")
        self.dealer_hand_label.pack()

        self.player_hand_label = tk.Label(self.play_frame, text=f"Your hand: {self.player_hand}")
        self.player_hand_label.pack()

        self.hit_button = tk.Button(self.play_frame, text="Hit", command=self.hit)
        self.hit_button.pack(side=tk.LEFT)

        self.stand_button = tk.Button(self.play_frame, text="Stand", command=self.stand)
        self.stand_button.pack(side=tk.LEFT)

        self.double_button = tk.Button(self.play_frame, text="Double Down", command=self.double_down)
        self.double_button.pack(side=tk.LEFT)

        self.quit_button = tk.Button(self.play_frame, text="Quit", command=self.quit_game)
        self.quit_button.pack(side=tk.LEFT)

    def hit(self):
        hit(self.deck, self.player_hand)
        self.player_hand_label.config(text=f"Your hand: {self.player_hand}")
        if check_bust(self.player_hand):
            messagebox.showinfo("Busted", "You busted!")
            self.players[self.current_player]['chips'] -= self.bet
            self.next_player()

    def stand(self):
        self.dealer_turn()
        self.next_player()

    def double_down(self):
        self.bet *= 2
        hit(self.deck, self.player_hand)
        self.player_hand_label.config(text=f"Your hand: {self.player_hand}")
        if check_bust(self.player_hand):
            messagebox.showinfo("Busted", "You busted!")
            self.players[self.current_player]['chips'] -= self.bet
        else:
            self.dealer_turn()
        self.next_player()

    def dealer_turn(self):
        while self.dealer_hand.calc_val() < 17:
            hit(self.deck, self.dealer_hand)
        self.dealer_hand_label.config(text=str(self.dealer_hand))
        if check_bust(self.dealer_hand):
            messagebox.showinfo("Dealer Busted", "Dealer busted! You win!")
            self.players[self.current_player]['chips'] += self.bet
        elif self.dealer_hand.calc_val() > self.player_hand.calc_val():
            messagebox.showinfo("Dealer Wins", "Dealer wins!")
            self.players[self.current_player]['chips'] -= self.bet
        elif self.dealer_hand.calc_val() < self.player_hand.calc_val():
            messagebox.showinfo("Player Wins", "You win!")
            self.players[self.current_player]['chips'] += self.bet
        else:
            messagebox.showinfo("Push", "It's a push!")

    def next_player(self):
        self.play_frame.pack_forget()
        self.current_player += 1
        if self.current_player >= len(self.players):
            self.current_player = 0
        if self.players[self.current_player]['chips'] <= 0:
            messagebox.showinfo("Game Over", f"{self.players[self.current_player]['name']} is out of chips! Game over.")
            self.players.pop(self.current_player)
            if not self.players:
                messagebox.showinfo("Game Over", "All players are out of chips! Game over.")
                self.root.quit()
                return
        self.update_player_info()

    def quit_game(self):
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = BlackjackApp(root)
    root.mainloop()
