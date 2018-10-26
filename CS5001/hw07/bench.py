import queue
from team import Team


class Bench:
    """A class representing a sidelines bench"""

    def __init__(self):
        # TODO: Initialize the bench object with whatever
        # attributes and values it will need
        """ Initialize the bench with an empty list of bench players"""
        self.bench_players = []  # Using list as a Queue

    def send_to_bench(self, team, bench, player_name):
        # TODO: Put the player "onto the bench"
        """ Send a specified player from team to the bench

        Args:
            team: team where player currently stays in
            bench: the bench where player is about to sent to
            player_name: player who sent to the bench
        """
        players = [player.name for player in team.players]
        if player_name in players:
            for player in team.players:
                if player.name == player_name:
                    bench.bench_players.append(player)
                    team.players.remove(player)
                    print("Sent", player_name, "to bench.")
        else:
            print(player_name, 'is not on the team.')

    def get_from_bench(self):
        # TODO: Return the name of the player who has
        # been on the bench longest.
        """ Retrieve the player who has been on the bench longest """
        if (len(self.bench_players) == 0):
            print("The bench is empty")
        else:
            player = self.bench_players.pop()
            print(player.name)

    # TODO: Write the function that will display the
    # current list of players on the bench
    def show_bench_player(self):
        """ Show the list of bench players """
        if (len(self.bench_players) == 0):
            print("The bench is empty.")
        else:
            for i in range(len(self.bench_players)):
                print(self.bench_players[i].name)

    # TODO: Write any other methods that might be used
    # by the methods above.
