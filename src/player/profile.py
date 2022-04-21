

class Profile:
    """
    Player profile
    """

    def __init__(self, json):
        """
        Obtains the data from the json object that
        contains the unprocessed profile data
        """
        player = json["player"]
        self.avatar_url = player["avatar"]
        self.player_id = player["player_id"]
        self.api_id = player["@id"]
        self.profile_url = player["url"]
        self.name = player["name"]
        self.username = player["username"]
        self.title = player["title"]
        self.followers = player["followers"]
        self.country_api_id = player["country"]
        self.last_online = player["last_online"]
        self.joined = player["joined"]
        self.status = player["status"]
        self.is_streamer = player["is_streamer"]

    def print_basic_info(self):
        """
        Shows basic player information
        """
        print("Name:", self.name)
        print("Username:", self.username)
        print("Player ID:", self.player_id)
