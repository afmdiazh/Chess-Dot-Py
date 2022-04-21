from .profile import Profile
from .stats import Stats


class Player:
    def __init__(self, profile, stats):
        self.profile = Profile(profile["player"])
        self.stats = Stats(stats)
