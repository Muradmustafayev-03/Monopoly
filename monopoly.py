from board import BOARD
from cell import Cell
from player import Player


class Monopoly:
    def __init__(self, players: list[Player]):
        self.players = players

    @staticmethod
    def collect_rent(player: Player, cell: Cell):
        if cell.owner is None:
            return
        if cell.owner == player:
            return
        player.money -= cell.rent
        cell.owner.money += cell.rent
        print(f'{player.name} paid {cell.rent} to {cell.owner.name}')

    @staticmethod
    def buy_property(player: Player, cell: Cell):
        if cell.value == 0:
            return
        if player.money < cell.value:
            print(f"{player.name}, you don't have enough money to buy {cell.name} for {cell.value}")
            return
        if cell.owner is not None:
            return
        choice = input(f'Do you want to buy {cell.name} for {cell.value}? (y/n): ')
        if choice.lower() == 'y':
            player.money -= cell.value
            player.property.append(cell)
            cell.owner = player
            print(f'{player.name} bought {cell.name}')
        else:
            print(f'{player.name} decided not to buy {cell.name}')

    def recursive_auction(self, bidder: Player or None, bid: int, player: Player, cell: Cell):
        current_bid = bid
        current_bidder = bidder

        for p in self.players:
            if p == player or p == current_bidder:
                continue
            if p.money < current_bid:
                print(f"{p.name} doesn't have enough money to bid")
                continue
            bid = input(
                f'{p.name}, do you want to bid on {cell.name}? Current bid is {current_bid}. '
                f'Enter your bid or skip to pass: ')
            if bid.lower() == '':
                continue
            bid = int(bid)
            if bid <= current_bid:
                print(f'{p.name}, your bid must be higher than {current_bid}')
                continue
            current_bid = bid
            current_bidder = p
            print(f'{p.name} bid {bid} on {cell.name}')

        if current_bidder is None:
            print(f'No one bid on {cell.name}, auction ended')
        elif current_bid <= cell.value:
            print(f'{cell.name} auction ended as no one bid higher than the starting bid')
        elif current_bidder == bidder:
            return current_bidder, current_bid
        else:
            return self.recursive_auction(current_bidder, current_bid, player, cell)

    def sell_property_auction(self, player: Player, cell: Cell):
        if cell not in player.property:
            return

        print(f'{player.name} is selling {cell.name} on auction starting bid is {cell.value}')

        bidder, bid = self.recursive_auction(None, cell.value, player, cell)

        bidder.money -= bid
        player.money += bid
        cell.owner = bidder
        player.property.remove(cell)
        bidder.property.append(cell)
        print(f'{bidder.name} bought {cell.name} for {bid} from {player.name}')

    def play_turn(self, player: Player):
        print(f'\n{player.name}\nMoney: {player.money}\nProperty: {player.property}')
        input('Press enter to roll the dice: ')
        old_position = player.position
        dice_roll = player.roll_dice()
        player.move(dice_roll)
        cell = BOARD[player.position]
        print(f'{player.name} rolled a {dice_roll} and landed on {cell.name}')

        if player.position < old_position:
            print(f'{player.name} passed GO and collected $200')
            player.money += 200

        self.collect_rent(player, cell)
        self.buy_property(player, cell)

        while True:
            action = input('Press Enter to finish your turn or input "s" to sell a property: ')

            if not action:
                break
            if action == 's':
                if not player.property:
                    print("You don't posses any property")
                    continue
                for i, prop in enumerate(player.property):
                    print(f'{i + 1}. {prop.name}')
                choice = int(input('Enter the number of the property you want to sell: ')) - 1
                if choice >= len(player.property) or choice < 0:
                    print('Wrong input\n')
                    continue

                self.sell_property_auction(player, player.property[choice])

    def play_game(self):
        while True:
            for player in self.players:
                self.play_turn(player)
