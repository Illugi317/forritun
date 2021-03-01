'''
In a game of rock, paper, scissors, the following rules apply:

    Scissors cut paper
    Rock smashes scissors
    Paper wraps rock

Write a program that, when given the choices of two players, determines which of them wins or whether it's a draw.
Examples

Input:
 - Player 1's move: rock
 - Player 2's move: scissors
Output:
Winner: Player 1

Input:
 - Player 1's move: rock
 - Player 2's move: paper
Output:
Winner: Player 2

Input:
 - Player 1's move: scissors
 - Player 2's move: scissors
Output:
It's a draw
'''

p1_move = input("Player 1's move: ")
p2_move = input("Player 2's move: ")

# ...now fill in the rest

if p1_move == "rock":
    if p2_move == "rock":
        print("It's a draw")
    elif p2_move == "paper":
        print("Winner: Player 2")
    elif p2_move == "scissors":
        print("Winner: Player 1")

elif p1_move == "paper":
    if p2_move == "rock":
        print("Winner: Player 1")
    elif p2_move == "paper":
        print("It's a draw")
    elif p2_move == "scissors":
        print("Winner: Player 2")

elif p1_move == "scissors":
    if p2_move == "rock":
        print("Winner: Player 2")
    elif p2_move == "paper":
        print("Winner: Player 1")
    elif p2_move == "scissors":
        print("It's a draw")
