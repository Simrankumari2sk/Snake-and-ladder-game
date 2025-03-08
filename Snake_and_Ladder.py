import random

class SnakeAndLadders:
    def __init__(self):
        self.board = [i for i in range(101)]
        self.snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
        self.ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

    def roll_dice(self):
        return random.randint(1, 6)

    def play(self):
        player_position = 0
        moves = []
        while player_position < 100:
            dice_value = self.roll_dice()
            player_position += dice_value
            if player_position in self.snakes:
                player_position = self.snakes[player_position]
            elif player_position in self.ladders:
                player_position = self.ladders[player_position]

            moves.append(f'Rolled a {dice_value}, moved to {player_position}')
            
            if player_position >= 100:
                moves.append('Congratulations! You have won the game.')
                break
        return moves

if __name__ == '__main__':
    number_of_games = int(input("Enter the number of games to play: "))
    for i in range(number_of_games):
        game = SnakeAndLadders()
        print(f'Game {i + 1} Output:')
        result = game.play()
        for move in result:
            print(move)
        print()
