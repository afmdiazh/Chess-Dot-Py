<p align="center"><img src="https://raw.githubusercontent.com/afmdiazh/Chess-Dot-Py/main/resources/logo.png"
height="130"></p>

<p align="center">ChessDotPy is a simple app that communicates with the <a href="https://www.chess.com/">Chess.com</a> API</p>

<p align="center"><a href="https://github.com/afmdiazh/Chess-Dot-Py/blob/main/README.es.md">README in Spanish</a></p>

<p align="center"><img src="https://img.shields.io/github/languages/top/afmdiazh/Chess-Dot-Py" alt="Top Language Badge"/> <img src="https://img.shields.io/github/last-commit/afmdiazh/Chess-Dot-Py" alt="Last Commit Badge"/></p>

<p align="center"><a href="https://github.com/afmdiazh/Chess-Dot-Py/stargazers"><img src="https://img.shields.io/github/stars/afmdiazh/Chess-Dot-Py" alt="Stars Badge"/> <a href="https://github.com/afmdiazh/Chess-Dot-Py/network/members"><img src="https://img.shields.io/github/forks/afmdiazh/Chess-Dot-Py" alt="Forks Badge"/></a> <a href="https://github.com/afmdiazh/Chess-Dot-Py/pulls"><img  src="https://img.shields.io/github/issues-pr/afmdiazh/Chess-Dot-Py" alt="Pull Requests Badge"/></a> <a href="https://github.com/afmdiazh/Chess-Dot-Py/issues"> <img src="https://img.shields.io/github/issues/afmdiazh/Chess-Dot-Py" alt="Issues Badge"/></a> <a href="https://github.com/afmdiazh/Chess-Dot-Py/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/afmdiazh/Chess-Dot-Py?color=2b9348"></a> <a href="https://github.com/afmdiazh/Chess-Dot-Py/blob/master/LICENSE"><img src="https://img.shields.io/github/license/afmdiazh/Chess-Dot-Py?color=2b9348" alt="License Badge"/></a></p>

## Features

With this tool we can easily access any player's profile and see the leaderboard of any game-mode.

The interface is divided in sections:

- Player:

  - Profile picture

  - Profile information

  - Stats (also divided in categories)

- History:

  - Opponent

  - Piece color

  - Rating

  - Accuracy

  - Time control and rules

- Leaderboard:

  - Profile picture

  - Rank

  - Rating

  - Sorting

  - Wins, losses, draws

  - Nationality and flair

- Puzzle:

  - Daily puzzle

  - Random puzzle (updates every 15 seconds)

  - Solutions

## Installation

### Option 1: Executable ( Windows only )

Download as an automatically generated executable from the [actions page](https://github.com/afmdiazh/Chess-Dot-Py/actions/workflows/pyinstaller.yml) or the lastest released executable from the [releases page](https://github.com/afmdiazh/Chess-Dot-Py/releases) (preferably this, since this versions are manually checked).

Keep in mind that the automatically generated executables in the actions page might not always be as stable as the ones from the releases page.

### Option 2: Manual install

1. Install [Python](https://www.python.org/downloads/)

2. Download the repository or execute the command `git clone https://github.com/afmdiazh/Chess-Dot-Py` (requires [git](https://git-scm.com/downloads)) to clone the repository locally

3. Install the package manager [pip](https://pip.pypa.io/en/stable/) to install the required libraries.

4. Install the required libraries with the command `pip install dependencies.txt` (from the src folder) or executing `dependencies.bat`.

5. Run ChessDotPy with the command `python main.py` (from the src folder) or executing `start.bat`.

## Usage

### Player

To see a player's stats and profile, head to the Player tab and type their name. After that, you can press enter or "Search" and if the player exists their stats will load.

- Double clicking the player's avatar will open their Chess.com profile in the browser.

- Pressing "Reload" or F5 will reload the player's profile.

- Pressing clear will clear the whole section.

### History

To see a player's history, head to the History tab and type their name. After that, you can press enter or "Search" and if the player exists their history will load.

- Double clicking any game will open a menu to search and view the opponent's history directly.

- Pressing "Reload" or F5 will reload the player's history.

- Pressing clear will clear the whole section.

### Leaderboard

To load the leaderboard data, head to the Leaderboard tab and press "Update" or F5. After that, it will take a few moments to download all the leaderboard information and a bit more to download the profile pictures in the background.

- Double clicking any player will open a menu to search and view the player's history directly.

- Double clicking any column name will change the default sorting by that column.

### Puzzle

To load the puzzle data, head to the Puzzle tab and press "Get Daily Puzzle" or "Get Random Puzzle" (random puzzles are updated every 15 seconds or so). After the puzzle loads, you can press "Reveal Solution" to view the moves needed to solve the puzzle.

- Double clicking the Daily Puzzle image will open the puzzle in the browser.

## Screenshots

<p  align="center"><img  src="https://raw.githubusercontent.com/afmdiazh/Chess-Dot-Py/main/resources/s1.png"></p>

<p  align="center"><img  src="https://raw.githubusercontent.com/afmdiazh/Chess-Dot-Py/main/resources/s2.png"></p>

<p  align="center"><img  src="https://raw.githubusercontent.com/afmdiazh/Chess-Dot-Py/main/resources/s3.png"></p>

<p  align="center"><img  src="https://raw.githubusercontent.com/afmdiazh/Chess-Dot-Py/main/resources/s4.png"></p>

<p  align="center"><img  src="https://raw.githubusercontent.com/afmdiazh/Chess-Dot-Py/main/resources/s5.png"></p>

## Modules used

- [Chess.com](https://pypi.org/project/chess.com/ "Chess.com") - API Wrapper for Chess.com

- [PyQt5](https://pypi.org/project/PyQt5/ "PyQt5") - Graphic interface

- [Qt Material](https://pypi.org/project/qt-material/ "Qt Material") - Graphic interface themes

- [Emoji](https://pypi.org/project/emoji/ "Emoji") - Converting text strings to emojis

- [Pyinstaller](https://pypi.org/project/pyinstaller/ "Pyinstaller") - Creating executables from Python source

## Versioning

The versioning used for this project is based on [Semver](https://semver.org/ "Semver"), and it follows this X.Y.Z pattern:

- X: Major version, release or compatibility change

- Y: Functionality and features

- Z: Patches or small changes

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
