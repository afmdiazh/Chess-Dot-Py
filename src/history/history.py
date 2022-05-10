from util import format_date, format_date_time, read_field


class History:
    """
    Represents a player's match history, contains
    a list of games the player has participated in
    """

    def __init__(self, json: dict, username: str):
        """
        Constructor
        """
        self.username = username
        self.game_list = []
        games = json["games"]

        # Generate game objects
        for game_json in games:
            self.game_list.append(Game(game_json, self.username))

    def print_all_games(self):
        for game in self.game_list:
            game.print_all_data()


class Game:
    """
    Represents a completed chess game, contains
    data about the player's performance
    """

    def __init__(self, json: dict, username: str):
        """
        Constructor
        """
        # Base data
        self.own_username = username
        self.url = read_field(json, "url")
        self.pgn = read_field(json, "pgn")
        self.time_control = read_field(json, "time_control")
        self.end_time = read_field(json, "end_time")
        self.rated = read_field(json, "rated")
        self.tcn = read_field(json, "tcn")
        self.uuid = read_field(json, "uuid")
        self.initial_setup = read_field(json, "initial_setup")
        self.fen = read_field(json, "fen")
        self.time_class = read_field(json, "time_class")
        self.rules = read_field(json, "rules")

        # Players
        white = read_field(json, "white")
        black = read_field(json, "black")

        accuracies = read_field(json, "accuracies")

        self.white = Player(white, read_field(accuracies, "white"))
        self.black = Player(black, read_field(accuracies, "black"))

        # Other
        if self.black.username.lower() == self.own_username.lower():
            self.own_player = self.black
            self.own_color = "Black"
            self.opponent_player = self.white
            self.opponent_color = "White"
        else:
            self.own_player = self.white
            self.own_color = "White"
            self.opponent_player = self.black
            self.opponent_color = "Black"

    def get_winner(self):
        """
        Obtains winner of the game
        """
        if self.white.result == "win":
            return "White"
        elif self.black.result == "win":
            return "Black"
        else:
            return "Draw"

    def get_accuracies(self):
        """
        Obtains the players' accuracies as a string
        """
        try:
            return "W: %s%, B: %s%" % (str(round(self.white.accuracy, 2)), str(round(self.black.accuracy, 2)))
        except:
            return "Unknown"

    def get_own_accuracy(self):
        """
        Obtains the player's own accuracy as a string
        """
        try:
            return "%s%" % str(round(self.own_player.accuracy, 2))
        except:
            return "Unknown"

    def get_ratings(self):
        """
        Obtains the players' ratings as a string
        """
        try:
            return "W: %d, B: %d" % (self.white.rating, self.black.rating)
        except:
            return "Unknown"

    def get_own_rating(self):
        """
        Obtains the player's own ratings as a string
        """
        try:
            return "%d" % self.own_player.rating
        except:
            return "Unknown"

    def get_format(self):
        """
        Obtains the game's time and ruleset as a string
        """
        try:
            return "%s - %s" % (self.rules, self.time_control)
        except:
            return "Unknown"

    def get_date(self):
        """
        Obtains the date of the game as a string
        """
        return format_date_time(self.end_time)

    def print_all_data(self):
        """
        Shows the data of both players inside the game
        """
        print("### Game")
        print("## White:")
        self.white.print_all_data()
        print("## Black:")
        self.black.print_all_data()
        print("## Other:")
        print(" - Rated:", self.rated)
        print(" - Rules:", self.rules)
        print(" - Time control:", self.time_control)
        print(" - End time:", self.end_time)
        print(" - Initial setup:", self.initial_setup)


class Player:
    """
    Represents a player inside a match, only contains
    very basic player data
    """

    def __init__(self, json: dict, accuracy: float):
        """
        Constructor
        """
        self.rating = read_field(json, "rating")
        self.result = read_field(json, "result")
        self.id = read_field(json, "@id")
        self.username = read_field(json, "username")
        self.uuid = read_field(json, "uuid")
        self.accuracy = accuracy

    def print_all_data(self):
        """
        Shows the player data
        """
        print("# Player data:")
        print(" - Name:", self.username)
        print(" - Rating:", self.rating)
        print(" - Result:", self.result)
        print(" - Accuracy:", self.accuracy)
