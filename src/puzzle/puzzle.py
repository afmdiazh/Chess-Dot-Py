import re

from const import html_end, html_start, html_title
from util import format_date, read_field


class Puzzle:
    """
    Represents a daily puzzle, containing puzzle data
    """

    def __init__(self, json: dict, is_random: bool = False):
        """
        Obtains the data from the json object
        """
        puzzle = read_field(json, "puzzle")
        self.is_random = is_random

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
                    try:
                        # Find all the entries that contain data in brackets
                        fields = re.findall(r'"([^"]*)"', line)
                        if len(fields) > 0:
                            # Value of the field
                            data = fields[0]

                            # Title of the field
                            title = line

                            # Replaces characters that aren't needed
                            characters_to_remove = [data, "[", "]", '"']
                            for char in characters_to_remove:
                                title = title.replace(char, "")

                            # Remove spaces
                            title = title.strip()

                            # Add to dictionary if not FEN
                            if title != "FEN":
                                self.extra_data[title] = data
                    except:
                        pass

    def get_extra_data(self):
        """
        Formats the extra_data dictionary into a 
        readable string containing all the data
        """
        # Obtain all the keys inside the object
        data_titles = self.extra_data.keys()

        # If no keys, return
        if len(data_titles) == 0:
            return "No extra data"

        # For security
        try:
            # Create the html string
            html = html_start
            for title in data_titles:
                # Title
                html += "<p>" + html_title % title
                # Value
                html += ": %s" % self.extra_data[title] + "</p>"
            html += html_end
            return html
        except:
            return "Error parsing extra data"

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
