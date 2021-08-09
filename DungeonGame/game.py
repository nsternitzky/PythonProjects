import random
from player import Player

class Game:
    def __init__(self):
        self.size = 4
        self.columns = ['A','B','C','D']
        self.locations = []

        for col in self.columns:
            for num in range(1, self.size + 1):
                self.locations.append(f'{col}{num}')

        self.set_player()
        self.set_exit_location()
        self.set_monster_location()
        self.create_grid()

    def set_player(self):
        player_start_location = random.choice(self.locations)
        self.player = Player("Dante", player_start_location)

    def set_exit_location(self):
        exit_location = random.choice(self.locations)
        while exit_location == self.player.location:
            exit_location = random.choice(self.locations)
        self.exit_location = exit_location

    def set_monster_location(self):
        monster_location = random.choice(self.locations)
        while monster_location == self.player.location or monster_location == self.exit_location:
            monster_location = random.choice(self.locations)
        self.monster_location = monster_location

    def create_row(self, num):
        row = []
        for col in self.columns:
            if self.player.location == f'{col}{num}':
                row.append('X')
            else:
                row.append(' ')
        return row

    def create_grid(self):
        header = ' | ' + ' | '.join(self.columns) + (' |')
        print(header)
        for row_num in range(1, self.size + 1):
            printable_row = f'{row_num}| '
            row = self.create_row(row_num)
            printable_row += ' | '.join(row) + ' |'
            print(printable_row)

game = Game()
print(f'Player at {game.player.location}, exit at {game.exit_location}, monster at {game.monster_location}')