from pair_of_dice import PairOfDice


class GameController:
    """Manage the rolling, scoring, and user interaction"""
    def __init__(self):
        self.the_pair = PairOfDice()

    def start_play(self):
        points = 0
        self.the_pair = PairOfDice()
        text = input("Press enter to roll the dice...\n")
        if text == "":
            self.the_pair.roll_dice()
            first_roll = self.the_pair.current_value()
            if (first_roll == 2 or first_roll == 3 or first_roll == 12):
                print("You rolled", first_roll, ". You lose!")
            elif (first_roll == 7 or first_roll == 11):
                print("You rolled", first_roll, ". You win!")
            else:
                points = self.the_pair.current_value()
                print("Your point is", points)
                self.the_pair.roll_dice()
                next_roll = self.the_pair.current_value()
                while (next_roll != points or next_roll != 7):
                    text = input("Press enter to roll the dice...\n")
                    if text == "":
                        self.the_pair.roll_dice()
                        next_roll = self.the_pair.current_value()
                        if next_roll == points:
                            print("You rolled", next_roll, ". You win.")
                            break
                        elif next_roll == 7:
                            print("You rolled 7. You lose.")
                            break
                        else:
                            print("You rolled", next_roll, ".")
                    else:
                        print("Press enter to roll the dice...\n")
        else:
            print("Press enter to roll the dice...\n")
