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
        self.player_id = json["player_id"]
        self.api_id = json["@id"]
        self.username = json["username"]
        self.score = json["score"]
        self.rank = json["rank"]
        self.country_api_id = json["country"]
        self.status = json["status"]
        self.avatar_url = json["avatar"]

        # In some cases, players don't have
        # a defined name
        if "name" in json:
            self.name = json["name"]
        else:
            self.name = "Unknown"

    def print_data(self):
        """
        Prints data
        """
        print("Showing player data:", self.name)
        print(self.username)
        print(self.score)
