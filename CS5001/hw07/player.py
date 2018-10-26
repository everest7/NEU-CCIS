

class Player:
    """A class representing a dodgeball player"""
    # TODO: Write a constructor (__init__() method) that
    # will take the necessary values, set them to
    # the player object's attributes, and create the
    # new instance of player. Like all methods, its first
    # parameter must be `self`. The remaining parameters should
    # receive whatever pieces of data are relevant to creating
    # a new Player object.
    def __init__(self, player_name, player_number, player_position):
        """Initializing a Player instance with name, number and position"""
        self.name = player_name
        self.number = player_number
        self.position = player_position
