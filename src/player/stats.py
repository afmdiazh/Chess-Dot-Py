from this import d


class Stats:
    """
    Represents the player's stats
    """

    def __init__(self, json):
        """
        Creates sections from the json
        """
        stats = json["stats"]

        # Section names, for example:
        # chess_rapid, chess_bullet, chess_blitz
        existing_sections = stats.keys()

        # Create a list of sections
        self.section_list = []

        # Iterates over all the sections
        for section in existing_sections:
            # Only checks if it's a dictionary, since there
            # are sections (like fide) that contain only ints
            if type(stats[section]) is dict:
                # If a section has "last", "best" and "record" fields,
                # generate a new Section object that will contain that data
                if "last" and "best" and "record" in stats[section]:
                    self.section_list.append(Section(section, stats[section]))

    def print_all_sections(self):
        for section in self.section_list:
            section.print_data()


class Section:
    """
    Represents a section inside the player's stats
    """

    def __init__(self, name, json):
        """
        Obtains the data from the json section
        """
        self.name = name

        # Last: current rating
        last = json["last"]
        self.current_rating = last["rating"]
        self.current_date = last["date"]

        # Best: highest rating
        best = json["best"]
        self.highest_rating = best["rating"]
        self.highest_date = best["date"]

        # Record: wins, loses and draws
        record = json["record"]
        self.wins = record["win"]
        self.loses = record["loss"]
        self.draws = record["draw"]

    def print_data(self):
        """
        Shows the stats in a more readable format
        """
        print("###", self.name)
        print("#", "Current stats: ")
        print(" - Rating:", self.current_rating)
        print(" - Last played:", self.current_date)
        print("#", "Best stats: ")
        print(" - Rating:", self.highest_rating)
        print(" - Last highest:", self.highest_date)
        print("#", "Game stats: ")
        print(" - Total games:", self.get_total_games())
        print(" - Wins:", self.wins)
        print(" - Losses:", self.loses)
        print(" - Draws:", self.draws)
        print(" - Winrate:", self.get_win_rate())

    def get_total_games(self):
        """
        Gets amount of games
        """
        return self.wins + self.loses + self.draws

    def get_win_rate(self):
        """
        Gets % of won games
        """
        total = self.get_total_games()
        return self.wins / total
