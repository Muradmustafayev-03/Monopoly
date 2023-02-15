from cell import Cell
from player import Player


class Monopoly:
    def __init__(self, players: list[Player]):
        self.players = players

    def play_game(self):
        while True:
            for player in self.players:
                self.play_turn(player)

    def play_turn(self, player: Player):
        loan_repay = player.handle_loans()
        player.print_stats()
        if loan_repay:
            print(f'Repaid a loan {loan_repay}$')

        cell = player.roll_dice_and_move()

        self.collect_rent(player, cell)
        self.buy_property(player, cell)

        while True:
            action = input('Press Enter to finish your turn\n'
                           'Input "s" to sell a property\n'
                           'Input "l" to take a loan\n')
            if not action:
                break
            if action.lower() == 's':
                self.handle_sell(player)
            if action.lower() == 'l':
                player.take_loan()

    @staticmethod
    def collect_rent(player: Player, cell: Cell):
        if cell.owner is None or cell.owner == player:
            return
        rent = cell.get_rent(collection=player.count_collection(cell))
        player.money -= rent
        cell.owner.money += rent
        print(f'{player} paid {rent} to {cell.owner}')

    def buy_property(self, player: Player, cell: Cell):
        if cell.value == 0 or cell.owner is not None:
            return
        choice = input(f'Do you want to buy {cell} for {cell.value}? (y/n): ')
        if choice.lower() != 'y':
            print(f'{player.name} decided not to buy {cell}')
            return
        while player.money < cell.value:
            print(f"{player}, you don't have enough money to buy {cell} for {cell.value}")
            action = input(f'Press Enter to cancel or you can take a loan("l") or sell your property("s")\n')
            if not action:
                return
            if action.lower() == 's':
                self.handle_sell(player)
            if action.lower() == 'l':
                player.take_loan()

        player.money -= cell.value
        player.property.append(cell)
        cell.owner = player
        print(f'{player.name} has just bought the {cell}')

    def handle_sell(self, player: Player):
        if not player.property:
            print("You don't posses any property")
            return
        for i, prop in enumerate(player.property):
            print(f'{i + 1}. {prop}')
        choice = int(input('Enter the number of the property you want to sell: ')) - 1
        if choice >= len(player.property) or choice < 0:
            print('Wrong input')
            return
        self.sell_property_auction(player, player.property[choice])

    def sell_property_auction(self, player: Player, cell: Cell):
        if cell not in player.property:
            return

        print(f'{player} is selling {cell} on auction starting bid is {cell.value}')

        bidder, bid = self.recursive_auction(None, cell.value, player, cell)

        if not bidder:
            return

        bidder.money -= bid
        player.money += bid
        cell.owner = bidder
        player.property.remove(cell)
        bidder.property.append(cell)
        print(f'{bidder.name} bought {cell} for {bid} from {player}')

    def recursive_auction(self, bidder: Player or None, bid: int, player: Player, cell: Cell):
        current_bid = bid
        current_bidder = bidder

        for p in self.players:
            if p == player or p == current_bidder:
                continue
            if p.money < current_bid:
                print(f"{p} doesn't have enough money to bid")
                continue
            bid = input(
                f'{p}, do you want to bid on {cell}? Current bid is {current_bid}. '
                f'Enter your bid or skip to pass: ')
            if bid == '':
                continue
            bid = int(bid)
            if bid <= current_bid:
                print(f'{p}, your bid must be higher than {current_bid}')
                continue
            current_bid = bid
            current_bidder = p
            print(f'{p} bid {bid} on {cell}')

        if current_bidder is None:
            print(f'No one bid on {cell}, auction ended')
            return None, 0
        if current_bid <= cell.value:
            print(f'{cell} auction ended as no one bid higher than the starting bid')
            return None, 0
        if current_bid == bid:
            return current_bidder, current_bid
        return self.recursive_auction(current_bidder, current_bid, player, cell)
