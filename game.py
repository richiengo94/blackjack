from shoe import Shoe

class Game:

    def __init__(self):
        self.game_over = False
        self.remaining_credit = 500

    def get_remaining_credit(self) -> int:

        return self.remaining_credit
    
    def set_remaining_credit(self, credit: int) -> None:

        self.remaining_credit = credit

game = Game()

while(not game.game_over):
    if(game.get_remaining_credit() <= 0):
       game.game_over = True

    game.set_remaining_credit(game.get_remaining_credit() - 10)
    print(game.get_remaining_credit())