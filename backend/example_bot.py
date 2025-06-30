from abstract_bot import AbstractBot


class ExampleBot(AbstractBot):
    """A bot that plays a trivial strategy."""

    def game_init(
        self,
        num_of_players: int,
        my_index: int,
        hand: list,
        kozar_card: tuple,
        first_player: int,
        lowest_kozar: int,
    ):
        self.log("game_init called")
        ordered_suits = [0, 1, 2, 3]
        ordered_suits[self.get_kozar_suit()] = 3
        ordered_suits[3] = self.get_kozar_suit()
        # ordering the cards in an increasing order (one of a few possible orders).
        self.card_order = [(i, suit) for suit in ordered_suits for i in range(13)]

    def optional_attack(self):
        for card in self.get_hand():
            for table_card in self.get_table_attack() + self.get_table_defence():
                if table_card is None:
                    continue
                if table_card[0] == card[0]:
                    self.log(f"Joining attack with: {card}")
                    return [card]
        self.log("Passing on joining attack.")
        return []

    def first_attack(self):
        self.log(f"Starting attack with {self.get_hand()[0]}")
        return self.get_hand()[0:1]

    def defence(self):
        defending_cards, indexes = [],[]
        # if possible to forward
        if all(card is None for card in self.get_table_defence()):
            num = [card for card in self.get_table_attack()+self.get_table_defence() if card is not None][0][0]
            for card in self.get_hand():
                if card[0] == num:
                    # forward
                    self.log(f"Forwarding {card}")
                    return [card],[]
        for index,attacking_card in enumerate(self.get_table_attack()):
            if attacking_card is None or self.get_table_defence()[index] is not None:
                continue
            flag: bool = False
            for card in self.get_hand():
                if self.card_order.index(attacking_card) < self.card_order.index(card):
                    defending_cards.append(card)
                    indexes.append(index)
                    flag = True
                    break
            # failed to defend
            if not flag:
                self.log("Taking cards.")
                return [],[]
        self.log(f"Defending with {defending_cards}, {indexes}")
        return defending_cards, indexes
    
    def notify_burn(self, card_list):
        self.log(f"burn: {card_list}")

    def notify_cards_drawn_to_hand(self, card_list):
        self.log(f"cards drawn to hand: {card_list}")
    
    def notify_winner(self, winner_index):
        self.log(f"Winner: {winner_index}")
    
    def notify_pass(self, player_index):
        self.log(f"Player {player_index} passed")
    
    def notify_optional_attack(self, player_index, cards):
        self.log(f"Player {player_index} optional attack with cards: {cards}")
    
    def notify_first_attack(self, player_index, cards):
        self.log(f"Player {player_index} first attack with cards: {cards}")
    
    def notify_defence(self, player_index, defending_cards, indexes):
        self.log(f"Player {player_index} defended with cards: {defending_cards} at indexes: {indexes}")
    
    def notify_forward(self, forwarder_index, card_list):
        self.log(f"Player {forwarder_index} forwarded with cards: {card_list}")
    
    def notify_take(self, defender_index, card_list):
        self.log(f"Player {defender_index} took cards: {card_list}")
    
    



bot: ExampleBot = ExampleBot()
