from util import read_field


class Puzzle:
    """
    Represents a daily puzzle, containing puzzle data
    """

    def __init__(self, json: dict):
        """
        Obtains the data from the json object
        """
        puzzle = read_field(json, "puzzle")

        if puzzle:
            self.title = read_field(puzzle, "title")
            self.url = read_field(puzzle, "url")
            self.publish_time = read_field(puzzle, "publish_time")
            self.fen = read_field(puzzle, "fen")
            self.pgn = read_field(puzzle, "pgn")
            self.image_url = read_field(puzzle, "image")

    def print_data(self):
        """
        Shows the puzzle data
        """
        print("# Daily puzzle data:")
        print(" - Title:", self.title)
        print(" - URL:", self.url)
