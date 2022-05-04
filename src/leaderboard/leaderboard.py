import os.path
import emoji

from util import find_emoji, read_field


class Leaderboard:
    """
    Represents the game's leaderboard
    """

    def __init__(self, json):
        """
        Generates a list of section items
        """
        leaderboards = json["leaderboards"]

        # Get all the section names
        self.section_names = leaderboards.keys()

        # List of sections
        self.section_list = []

        # Generate objects for all sections
        for section in self.section_names:
            self.section_list.append(LSection(section, leaderboards[section]))

    def print_data(self):
        """
        Prints data of all sections
        """
        print("Showing loaderboard data")
        for section in self.section_list:
            section.print_data()

    def print_section_names(self):
        """
        Prints all section names
        """
        for section in self.section_list:
            print(section.name)


class LSection:
    """
    Represents one section inside the game's leaderboard
    """

    def __init__(self, name, json):
        """
        Generates a list of leaderboard player items
        """
        self.name = name
        self.player_list = []

        # Generate objects for all players
        for player in json:
            self.player_list.append(LPlayer(player))

    def print_data(self):
        """
        Prints data of all players
        """
        print("Showing section data:", self.name)
        for player in self.player_list:
            player.print_data()

    def get_formatted_name(self):
        """
        Obtains formatted name
         - Sets first letter to uppercase
         - Replaces underscores with spaces
        """
        formatted = self.name.capitalize().replace("_", " ")
        return formatted


class LPlayer:
    """
    Represents one player inside a leaderboard section
    """

    def __init__(self, json):
        """
        Obtains the player data from json
        """
        self.player_id = read_field(json, "player_id")
        self.api_id = read_field(json, "@id")
        self.username = read_field(json, "username")
        self.score = read_field(json, "score")
        self.rank = read_field(json, "rank")
        self.country_api_id = read_field(json, "country")
        self.status = read_field(json, "status")
        self.avatar_url = read_field(json, "avatar")
        self.flair = read_field(json, "flair_code")
        self.name = read_field(json, "name", "Unknown")
        self.wins = read_field(json, "win_count")
        self.losses = read_field(json, "loss_count")
        self.draws = read_field(json, "draw_count")

    def print_data(self):
        """
        Prints data
        """
        print("Showing player data:", self.name)
        print(self.username)
        print(self.score)

    def get_country(self):
        """
        Returns country code
        """
        if self.country_api_id == None: return "?"
        return os.path.basename(self.country_api_id)

    def get_flair(self):
        """
        Returns flair (emoji)
        """
        if self.flair == None: return ""
        flair = find_emoji(self.flair)
        return emoji.emojize(":%s:" % flair)

    def get_formatted_stats(self):
        """
        Returns a formatted string with the format
        W: wins, L: losses, D: draws
        """
        return "W: %d L: %d D: %d" % (self.wins, self.losses, self.draws)
