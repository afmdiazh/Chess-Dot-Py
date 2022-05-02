from data import get_player, get_leaderboard

# Obtain player profile
player = get_player("fabianocaruana")

# Show basic profile data
print(player.profile.print_basic_info())

# Show all sections
print(player.stats.print_all_sections())

# Obtain leaderboard
leaderboard = get_leaderboard()
