# Do not modify these lines
__winc_id__ = "04da020dedb24d42adf41382a231b1ed"
__human_name__ = "classes"

# Add your code after this line
class Player:
    def __init__(self, name, speed, endurance, accuracy) -> None:
        if speed <= 0 or speed >= 1:
            raise ValueError("Speed must be betweeen 0 and 1")
        if endurance <= 0 or endurance >= 1:
            raise ValueError("Endurance must be betweeen 0 and 1")
        if accuracy <= 0 or accuracy >= 1:
            raise ValueError("Accuracy must be betweeen 0 and 1")
        self.name = name
        self.speed = speed
        self.endurance = endurance
        self.accuracy = accuracy

    def introduce(self):
        return f"Hello everyone, my name is {self.name}."

    def strength(self):
        if self.speed >= self.endurance and self.speed >= self.accuracy:
            return ("speed", self.speed)
        if self.endurance >= self.speed and self.endurance >= self.accuracy:
            return ("endurance", self.endurance)
        if self.accuracy >= self.speed and self.accuracy >= self.endurance:
            return ("accuracy", self.accuracy)


class Commentator:
    def __init__(self, name) -> None:
        self.name = name

    def sum_player(self, player):
        return player.speed + player.endurance + player.accuracy

    def compare_players(self, player1, player2, attr):
        if getattr(player1, attr) > getattr(player2, attr):
            # player1 scores higher
            return player1.name

        if getattr(player2, attr) > getattr(player1, attr):
            # player2 scores higher
            return player2.name

        if getattr(player1, attr) == getattr(player2, attr):
            # both players score equal
            if player1.strength()[1] > player2.strength()[1]:
                # player1 scores better from strength()
                return player1.name
            if player2.strength()[1] > player1.strength()[1]:
                # player2 score better from strength()
                return player2.name
            if player1.strength()[1] == player2.strength()[1]:
                if self.sum_player(player1) > self.sum_player(player2):
                    return player1.name
                if self.sum_player(player2) > self.sum_player(player1):
                    return player2.name
                return "These two players might as well be twins!"
