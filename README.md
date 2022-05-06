<p align="center"><img src="https://raw.githubusercontent.com/mgldz/Chess-Dot-Py/main/resources/logo.png"
height="130"></p>

<p align="center">ChessDotPy is a simple app to access the <a href="https://www.chess.com/">Chess.com</a> API</p>

<p align="center"><a href="https://github.com/mgldz/Chess-Dot-Py/blob/main/README.es.md">README in Spanish</a></p>

<p align="center"><img src="https://img.shields.io/github/languages/top/mgldz/Chess-Dot-Py" alt="Top Language Badge"/> <img src="https://img.shields.io/github/last-commit/mgldz/Chess-Dot-Py" alt="Top Last Commit Badge"/></p>

<p align="center"><a href="https://github.com/mgldz/Chess-Dot-Py/stargazers"><img src="https://img.shields.io/github/stars/mgldz/Chess-Dot-Py" alt="Stars Badge"/> <a href="https://github.com/mgldz/Chess-Dot-Py/network/members"><img src="https://img.shields.io/github/forks/mgldz/Chess-Dot-Py" alt="Forks Badge"/></a> <a href="https://github.com/mgldz/Chess-Dot-Py/pulls"><img  src="https://img.shields.io/github/issues-pr/mgldz/Chess-Dot-Py" alt="Pull Requests Badge"/></a> <a href="https://github.com/mgldz/Chess-Dot-Py/issues"> <img src="https://img.shields.io/github/issues/mgldz/Chess-Dot-Py" alt="Issues Badge"/></a> <a href="https://github.com/mgldz/Chess-Dot-Py/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/mgldz/Chess-Dot-Py?color=2b9348"></a> <a href="https://github.com/mgldz/Chess-Dot-Py/blob/master/LICENSE"><img src="https://img.shields.io/github/license/mgldz/Chess-Dot-Py?color=2b9348" alt="License Badge"/></a></p>

## Features

With this tool we can easily access any player's profile and see the leaderboard of any game-mode.

The interface is divided in sections:

- Player:

  - Profile

  - Stats (also divided in categories)

- Leaderboard:

  - Rank

  - Rating

  - Sorting

  - Wins, losses, draws

  - Nationality and flair

## Installation

### Option 1: Executable ( Windows only )

Download as an automatically generated executable from the [actions page](https://github.com/mgldz/Chess-Dot-Py/actions/workflows/pyinstaller.yml) or the lastest released executable from the [releases page](https://github.com/mgldz/Chess-Dot-Py/releases) (preferably this, since this versions are manually checked).

Keep in mind that the automatically generated executables in the actions page might not always be as stable as the ones from the releases page.

### Option 2: Manual install

1. Install [Python](https://www.python.org/downloads/)

2. Download the repository or execute the command `git clone https://github.com/mgldz/Chess-Dot-Py` (requires git) to clone the repository locally

3. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required libraries.

4. Install the required libraries with the command `pip install dependencies.txt` (from the src folder) or executing `dependencies.bat`.

5. Run ChessDotPy with the command `python main.py` (from the src folder) or executing `start.bat`.

## Usage

### Player

To see a player's stats, head to the Player tab and type their name. After that, you can press enter or "Search" and if the player exists their stats will load.

Double clicking the player's avatar will open their Chess.com profile in the browser.

Pressing "Reload" will reload the player's profile.

Pressing clear will clear the whole section.

### Leaderboard

To load the leaderboard data, head to the Leaderboard tab and press "Update". After that, it will take a few moments to download all the leaderboard information and a bit more to download the profile pictures in the background.

Double clicking the player's username will redirect to the Player tab and will load the player's profile.

Double clicking any column name will change the default sorting by that column.

## Screenshots

<p align="center"><img src="https://raw.githubusercontent.com/mgldz/Chess-Dot-Py/main/resources/s1.png"></p>

<p align="center"><img src="https://raw.githubusercontent.com/mgldz/Chess-Dot-Py/main/resources/s2.png"></p>

## Modules used

- [Chess.com](https://pypi.org/project/chess.com/ "Chess.com") - API Wrapper for Chess.com
- [PyQt5](https://pypi.org/project/PyQt5/ "PyQt5") - Graphic interface

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
