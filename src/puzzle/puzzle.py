from util import format_date, read_field


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
        print(" - PGN: ", self.pgn)

    def get_solution(self):
        """
        Obtains the puzzle solution, which is usually
        the last line of the PGN
        """
        lines = self.pgn.splitlines()
        return lines[-1]

    def get_title(self):
        """
        Obtains formatted title and date
        """
        return "%s: %s" % (self.title, format_date(self.publish_time))
