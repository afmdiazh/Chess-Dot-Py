from operator import indexOf
from util import format_date, read_field
import re


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
            # Obtain data from json
            self.title = read_field(puzzle, "title")
            self.url = read_field(puzzle, "url")
            self.publish_time = read_field(puzzle, "publish_time")
            self.fen = read_field(puzzle, "fen")
            self.pgn = read_field(puzzle, "pgn")
            self.image_url = read_field(puzzle, "image")
            self.extra_data = {}

            # Obtain rest of data
            if self.pgn:
                lines = self.pgn.splitlines()
                for line in lines:
                    # Find all the entries that contain data in brackets
                    fields = re.findall(r'"([^"]*)"', line)
                    if len(fields) > 0:
                        data = fields[0]
                        # Replaces characters that aren't needed
                        title = line.replace(data, "")
                        title = title.replace('"', "")
                        title = title.replace('[', "")
                        title = title.replace(']', "")
                        title = title.strip()
                        # Add to dictionary
                        self.extra_data[title] = data

    def get_extra_data(self):
        """
        Formats the extra_data dictionary into a 
        readable string containing all the data
        """
        data_titles = self.extra_data.keys()
        formatted_string = ""
        for title in data_titles:
            formatted_string += "%s: %s\n" % (title, self.extra_data[title])
        return formatted_string

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
        # Split lines
        lines = self.pgn.splitlines()

        # Trying to find by line that starts with number and dot
        for line in lines:
            if re.match(r"[0-9]+\.", line):
                pass
                return line

        # If not found previous way, it's usually FEN + 2
        for line in lines:
            if "FEN" in line:
                return lines[lines.index(line) + 2]

    def get_title(self):
        """
        Obtains formatted title and date
        """
        return "%s: %s" % (self.title, format_date(self.publish_time))
