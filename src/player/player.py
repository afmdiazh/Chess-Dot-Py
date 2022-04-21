from .profile import Profile
from .stats import Stats


class Player:
    """
    Represents a player, contains the profile
    and stats data
    """

    def __init__(self, profile, stats):
        """
        Generates profile and stats objects
        """
        self.profile = Profile(profile["player"])
        self.stats = Stats(stats)
