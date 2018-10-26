from player import Player


class Team:
    """A class representing a dodgeball team"""
    # All methods in Python include arguments representing the object
    # itself. In the method definition, this is represented by the
    # `self` parameter.

    def __init__(self):
        """Initializing a Team instance with default name,
        and a empty list of players"""
        self.name = "Anonymous Team"
        self.players = []

    # Another example of self. The method call only passes one argument,
    # the 'name; value. But the method definition must always include the
    # self parameter.
    def set_team_name(self, name):
        # TODO: set the team name
        """Set the team name

        Args:
            name: Team's name
        """
        self.name = name

    # Note again that `self` is the first parameter.
    def add_player(self, player_name, player_number, player_position):
        # TODO: call the Player class constructor with the appropriate
        # values to create a new player object, then add that
        # player object to the team's players list.
        """ Add player to the players list in Team instance

        Args:
            player_name: parameter needed to create a new Player instance
            player_number: parameter needed to create a new Player instance
            player_position: parameter needed to create a new Player instance
        """
        new_player = Player(player_name, player_number, player_position)
        self.players.append(new_player)

    def cut_player(self, player_name):
        # TODO: Remove the player with the name player_name
        # from the players list.
        """Cut player from the players list

        Args:
            player_name: player who is about to be removed
        """
        for player in self.players:
            if (player.name == player_name):
                self.players.remove(player)
                print(player_name, 'has been cut')

    def is_position_filled(self, position):
        # TODO: Write the method that checks whether
        # there is currently at least one player on the team
        # occupying the requested position
        """ Check if a specified position is currently filled

        Args:
            positoin: specified position you want to check
        """
        positions = [player.position for player in self.players]
        if position in positions:
            print("Occupied")
        else:
            print("Vacant")

    # TODO: Write any necessary methods to support the methods
    # above, and write the method that will display (print to screen)
    # the full team roster in the following format:

    #    The lineup for Seattle Scorpions is:
    #    15       Garcia          catcher
    #    55       Wiggins         corner
    #    99       McCann          sniper
    def do_show_team_roster(self):
        """ Show current team roster """
        print('The lineup for', self.name, 'is:')
        for player in self.players:
            print(str(player.number) + '       ' + player.name + '          ' +
                  player.position)
