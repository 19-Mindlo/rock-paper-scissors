import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    their_move = ""
    my_move = ""

    def __init__(self):
        self.my_move = random.choice(moves)
        self.their_move = random.choice(moves)

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class AllRockPlayer(Player):
    def move(self):
        move = 'rock'
        return move


class RandomPlayer(Player):
    def move(self):
        select = random.choice(moves)
        return select


class HumanPlayer(Player):
    def move(self):
        while True:
            choose = input("\nrock, paper, scissors ?\n\n").lower()
            if choose in moves:
                return choose
            else:
                print(f"\n {choose} is invalid, Please choose again\n\n")


class ReflectPlayer(Player):
    def move(self):
        if self.their_move in moves:
            return self.their_move
        else:
            return random.choice(moves)

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move == 'rock':
            return 'paper'
        elif self.my_move == 'paper':
            return 'scissor'
        elif self.my_move == 'scissors':
            return 'rock'
        else:
            return random.choice(moves)

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.player1_score = 0
        self.player2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2):
            self.player1_score += 1
            print("\nThe score is:"
                  f"Player 1 : {self.player1_score}"
                  f"Player 2 : {self.player2_score}")
            print("\nPlayer 1 Wins!")
        elif beats(move2, move1):
            self.player2_score += 1
            print("\nThe score is:"
                  f"Player 1 : {self.player1_score}"
                  f"Player 2 : {self.player2_score}")
            print("Player 2 Wins!")
        else:
            self.player1_score = self.player2_score
            print("\nThe score is:\n\n"
                  f"Player 1 : {self.player1_score}\\n\n"
                  f"Player 2 : {self.player2_score}\n\n")
            print("\nIt's a tie!\n\n")

    def play_game(self):
        print("\nGame start!")
        self.rounds = 4
        for round in range(self.rounds):
            print(f"Round {round}:")
            self.play_round()
        if self.player1_score > self.player2_score:
            print(f"\nThe game ended in score : {self.player1_score}\n\n"
                  "for player 1 and in score: "
                  f"{self.player2_score} for player 2")
            print("\nPlayer 1 wins the game!")
        elif self.player1_score < self.player2_score:
            print(f"\nThe game ended in score : {self.player1_score}"
                  "for player 1 and in score: "
                  f"{self.player2_score} for player 2")
            print("\nPlayer 2 wins the game!")
        elif self.player1_score == self.player2_score:
            print(f"Player 1 score is: {self.player1_score}")
            print(f"Player 2 score is: {self.player2_score}")
            print("It's a tie!")
        print("Game over!")


if __name__ == '__main__':
    players = [
        AllRockPlayer(),
        RandomPlayer(),
        ReflectPlayer(),
        CyclePlayer()
    ]

    p1 = HumanPlayer()
    p2 = RandomPlayer()
    game = Game(p1, p2)
    game.play_game()
