from .stats import Stats
from util import read_field


class Player:
    """
    Represents a player, contains the profile and stats data
    """

    def __init__(self, profile, stats):
        """
        Generates profile and stats objects
        Takes the data from the profile and stats json objects
        that are generated directly by the api
        """
        self.profile = Profile(profile)
        self.stats = Stats(stats)


class Profile:
    """
    Player profile
    """

    def __init__(self, json):
        """
        Obtains the data from the json object that
        contains the unprocessed profile data
        """
        player = read_field(json, "player")
        if player:
            self.avatar_url = read_field(player, "avatar")
            self.player_id = read_field(player, "player_id")
            self.api_id = read_field(player, "@id")
            self.profile_url = read_field(player, "url")
            self.username = read_field(player, "username")
            self.name = read_field(player, "name")
            self.title = read_field(player, "title")
            self.followers = read_field(player, "followers")
            self.country_api_id = read_field(player, "country")
            self.last_online = read_field(player, "last_online")
            self.joined = read_field(player, "joined")
            self.status = read_field(player, "status")
            self.is_streamer = read_field(player, "is_streamer")

    def print_basic_info(self):
        """
        Shows basic player information
        """
        print("Name:", self.name)
        print("Username:", self.username)
        print("Player ID:", self.player_id)
