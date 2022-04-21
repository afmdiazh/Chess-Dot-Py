import chessdotcom as c


def get_leaderboards():
    return c.get_leaderboards().json


def get_player_profile(username):
    return c.get_player_profile(username)

