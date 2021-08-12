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

    def check_for_win(self):
        return (self.player.location == self.exit_location)

    def check_for_loss(self):
        return (self.player.location == self.monster_location)

    def run_game(self):
        print("\nWelcome to the dungeon! Look for the exit, but don't run into the hungry monster!\n")
        game_running = True
        while game_running:
            self.create_grid()
            direction = input("\nWhich direction do you want to move in? (up/down/left/right) ")
            self.move_player(direction)
            if self.check_for_win():
                print("Congratulations, you found the exit!")
                game_running = False
            if self.check_for_loss():
                print("Oh no, the monster got you! Game over.")
                game_running = False

    def move_player(self, direction):
        player_col = self.player.location[0]
        player_row = self.player.location[1]

        if direction.lower() == 'up':
            if player_row == '1':
                print("Sorry, you can't move off the grid.")
            else:
                new_location = f'{player_col}{int(player_row) - 1}'
                self.player.move(new_location)
        if direction.lower() == 'down':
            if player_row == str(self.size):
                print("Sorry, you can't move off the grid.")
            else:
                new_location = f'{player_col}{int(player_row) + 1}'
                self.player.move(new_location)
        if direction.lower() == 'left':
            if player_col == self.columns[0]:
                print("Sorry, you can't move off the grid.")
            else:
                new_location = f'{self.columns[self.columns.index(player_col) - 1]}{player_row}'
                self.player.move(new_location)
        if direction.lower() == 'right':
            if player_col == self.columns[len(self.columns) - 1]:
                print("Sorry, you can't move off the grid.")
            else:
                new_location = f'{self.columns[self.columns.index(player_col) + 1]}{player_row}'
                self.player.move(new_location)

game = Game()
print(f'Player at {game.player.location}, exit at {game.exit_location}, monster at {game.monster_location}')
game.run_game()