import random


class Mastermind:
    COLOR_LETTERS = "rgbypo"
    
    def __init__(self, random_seed = None) -> None:
        if random_seed is not None:
            random.seed(random_seed)
        
    def __generate_random_code(self) -> str:
        return "".join(random.choices(self.COLOR_LETTERS, k=4))
    
    def play(self) -> None:
        code = self.__generate_random_code()
        # The rest of this method needs to be implemented
        # You are probably going to want to divide it up into several smaller methods

if __name__ == "__main__":
    game = Mastermind(random_seed=1337)
    play_again = "y"
    while play_again == "y":
        game.play()
        play_again = input("Would you like to play again (y/n)? ").lower()