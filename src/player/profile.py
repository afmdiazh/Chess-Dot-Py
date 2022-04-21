

class Profile:
    """
    Player profile
    """

    def __init__(self, json):
        """
        Obtains the data from the json object that
        contains the unprocessed profile data
        """
        self.avatar_url = json["avatar"]
        self.player_id = json["player_id"]
        self.api_id = json["@id"]
        self.profile_url = json["url"]
        self.name = json["name"]
        self.username = json["username"]
        self.title = json["title"]
        self.followers = json["followers"]
        self.country_api_id = json["country"]
        self.last_online = json["last_online"]
        self.joined = json["joined"]
        self.status = json["status"]
        self.is_streamer = json["is_streamer"]

    def print_basic_info(self):
        """
        Shows basic player information
        """
        print("Name:", self.name)
        print("Username:", self.username)
        print("Player ID:", self.player_id)
